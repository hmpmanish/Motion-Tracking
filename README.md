# Motion Detection Web App

This is a web application that uses Python, OpenCV, Flask, and WebSockets to detect motion via webcam. The app provides real-time video streaming and alerts the user when motion is detected. The sensitivity of the motion detection can be adjusted through a slider on the web interface.

## Features:
- **Real-time Video Feed**: Displays live webcam feed on the web page.
- **Motion Detection**: Detects motion using background subtraction and contour analysis.
- **Motion Alerts**: Notifies the user with an alert box when motion is detected.
- **Adjustable Sensitivity**: The user can adjust the sensitivity of the motion detection through a slider.
- **WebSocket Communication**: Real-time communication between the backend (Python) and frontend (JavaScript) using WebSockets.

## Requirements:
- Python 3.x
- Flask
- OpenCV
- Flask-SocketIO

## Installation and Setup:

1. Clone the repository or download the project files.

2. Install the required dependencies:
    ```bash
    pip install flask opencv-python flask-socketio
    ```

3. Run the Python server:
    Navigate to the project folder and run the Python server:
    ```bash
    python motion_tracker.py
    ```
    This will start the Flask server on `http://127.0.0.1:5000/`.

4. Open the web app in your browser:
    Open your browser and go to `http://127.0.0.1:5000/` to see the motion detection in action.

## Usage:
- **Start the motion tracking**: Click the "Start Motion Tracking" button to begin capturing the webcam feed.
- **Adjust Sensitivity**: Use the slider to change the sensitivity of the motion detection. Higher values will detect smaller movements.
- **Motion Detection Alerts**: When motion is detected, the app will display an alert at the top of the page.

## Project Structure:


. ├── index.html # Frontend HTML ├── motion_tracker.py # Backend Python script (Flask server) ├── script.js # JavaScript for frontend interaction └── style.css # CSS for styling the page

vbnet
Copy code

### Explanation of Files:
- **`index.html`**: The HTML structure of the webpage, including the video feed and controls for adjusting the sensitivity.
- **`style.css`**: Basic styling for the page, including layout and alert box styles.
- **`script.js`**: JavaScript handling the interaction with the backend (motion detection alerts and sensitivity control).
- **`motion_tracker.py`**: Python script that handles motion detection using OpenCV and Flask. It streams video and detects motion, sending alerts via WebSockets.

## How Motion Detection Works:
1. **Webcam Feed**: The webcam feed is accessed using OpenCV (`cv2.VideoCapture`).
2. **Background Subtraction**: Motion is detected by subtracting the current frame from a background model (`cv2.createBackgroundSubtractorMOG2`).
3. **Contour Analysis**: The contours of detected areas are examined, and if they surpass a certain size (based on the sensitivity setting), motion is flagged.
4. **Real-Time Updates**: When motion is detected, a WebSocket message is sent to the frontend, triggering an alert.
5. **Sensitivity Adjustment**: The user can adjust the sensitivity using a slider, which changes the minimum area for detecting motion.

## Troubleshooting:
- **No Webcam Feed**: Make sure your webcam is working and accessible. If you are using a laptop, ensure the camera is not being used by other applications.
- **App Not Running**: Ensure that the required Python libraries are installed and that there are no errors in the console when running the server.
- **Motion Not Detected**: Try adjusting the sensitivity slider. A higher sensitivity value will detect smaller movements.

## License:
This project is open-source and available under the MIT License.
Key Points:
This single-page README includes all the information for setting up, using, and understanding the project in a concise manner.
It explains the dependencies, how to run the project, the structure, and the features of the motion detection system.
Troubleshooting tips are included to help users solve common issues they might encounter.
