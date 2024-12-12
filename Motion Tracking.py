import cv2
import numpy as np

# Initialize the video capture object (use 0 for webcam, or provide a video file path)
cap = cv2.VideoCapture(0)

# Read the first frame
ret, frame1 = cap.read()
if not ret:
    print("Failed to read video feed.")
    cap.release()
    exit()

# Convert the first frame to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    # Read the next frame
    ret, frame2 = cap.read()
    if not ret:
        print("Video feed ended or failed.")
        break

    # Convert the current frame to grayscale
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the current frame and the previous frame
    diff = cv2.absdiff(gray1, gray2)

    # Apply a threshold to highlight significant differences
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Dilate the threshold image to fill gaps
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=2)

    # Find contours of the moving objects
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around detected motion
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue  # Skip small movements
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the processed video
    cv2.imshow('Motion Tracking', frame2)

    # Update the previous frame
    gray1 = gray2

    # Exit if 'q' is pressed
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
