from Car import Car
import readchar
import cv2

if __name__ == '__main__':
    car = Car()
    left = 72
    right = 75
    #initialize recording of video to save in a file
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video2.avi', fourcc, 20.0, (640, 480))

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