from Car import Car
import readchar
import cv2

if __name__ == '__main__':
    car = Car()
    left = 72
    right = 75

    cap = cv2.VideoCapture(0)  # Use 0 as the argument for the primary camera


    if not cap.isOpened():
        print("Error: Could not open camera.")
    else:
    # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change the codec to your preference (e.g., 'XVID', 'MJPG', 'H264', etc.)
        out = cv2.VideoWriter('circuit.avi', fourcc, 20.0, (640, 480))  # Adju
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        out.write(frame)
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

    # Write the frame to the video
    cap.release()
    out.release()
    cv2.destroyAllWindows()# Release the VideoWriter object when done
