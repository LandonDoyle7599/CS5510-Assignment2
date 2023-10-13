import cv2

# Create a VideoCapture object to access the camera
cap = cv2.VideoCapture(0)  # Use 0 as the argument for the primary camera

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    ret, frame = cap.read()  # Read a frame from the camera

    if ret:
        # Save the captured frame as an image (e.g., "captured_image.jpg")
        cv2.imwrite("captured_image.jpg", frame)
        print("Image captured and saved as 'captured_image.jpg'")
    else:
        print("Error: Could not capture an image.")

    # Release the VideoCapture object
    cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
