import cv2

# Create a VideoCapture object to access the camera
cap = cv2.VideoCapture(0)  # Use 0 as the argument for the primary camera

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change the codec to your preference (e.g., 'XVID', 'MJPG', 'H264', etc.)
    out = cv2.VideoWriter('captured_video.avi', fourcc, 20.0, (640, 480))  # Adjust the filename, frame rate, and resolution as needed

    while True:
        ret, frame = cap.read()  # Read a frame from the camera

        if not ret:
            print("Error: Could not read frame.")
            break

        # Write the frame to the video file
        out.write(frame)

        # Display the frame (optional)
        # cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()
