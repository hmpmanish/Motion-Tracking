import cv2
import numpy as np
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
import time
import json

app = Flask(__name__)
socketio = SocketIO(app)
#hmpmanish
# Initialize the webcam
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

sensitivity = 500  # Default sensitivity

@app.route('/')
def index():
    return render_template('index.html')

# WebSocket to handle sensitivity change
@socketio.on('message')
def handle_message(message):
    global sensitivity
    message = json.loads(message)
    if message.get("type") == "set_sensitivity":
        sensitivity = int(message.get("value"))
#hmpmanish
def generate_frames():
    first_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        #hmpmanish
        fgmask = fgbg.apply(frame)  # Apply background subtraction
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) < sensitivity:
                continue
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion_detected = True
        #hmpmanish
        # Send motion detection alert
        if motion_detected:
            socketio.emit("motion detected", "motion detected")
        
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#hmpmanish
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
#hmpmanish
if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
