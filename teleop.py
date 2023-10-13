from Car import Car
import readchar
import cv2

if __name__ == '__main__':
    car = Car()
    left = 72
    right = 75

    camera = cv2.VideoCapture(0)  # Use the correct camera index if needed (e.g., 0, 1, or a camera address)

    # Define the VideoWriter object to save video
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter('circuit.avi', fourcc, 20.0, (640, 480)) # You may need to adjust frame size (640x480) and frame rate (20.0) to your requirements

    while True:
        car.stop()
        key = readchar.readkey()
        if key == 'w':
            car.control_car(left, right)
        elif key == "s":
            car.control_car(-left, -right)
        elif key == "a":
            car.control_car(-left, right)
        elif key == "d":
            car.control_car(left, -right)
        elif key == "+":
            left += 25
            right += 25
        elif key == "-":
            left -= 25
            right -= 25
        elif key == "space":
            car.stop()
        elif key == "x":
            car.stop()
            break
        else:
            car.stop()

        # Capture a frame from the camera and write it to the video file
        ret, frame = camera.read()
        if not ret:
            break

    # Write the frame to the video
    out.release()
    camera.release()
    cv2.destroyAllWindows()# Release the VideoWriter object when done
