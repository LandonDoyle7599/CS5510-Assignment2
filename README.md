# CS5510 Assignment 2

Landon Doyle, Max Edwards, Jared Hansen

## Odometry

For the visual odometry we used the monocular visual odometry implementation found in this github repo https://github.com/alishobeiri/Monocular-Video-Odometery. To run the visual odometry you must download opencv-python version 3.4.17 with pip. You then must go to the test.py file and change the image and pose paths to their absolute path on your machine, escaping each \ as already present in the file. The image path should point to the captured_video subdirectory and the pose path should point to the tmp.txt file in the posedata directory. After making those changes running 'python test.py' in the terminal will perform the visual odometry on the sample video we provided 'captured_video.avi'. The algorithm references the captured_video subdirectory as that is where the pngs of each of the frames of the video are housed. The odometry output trajectory of the sample video can be found in the file trajectory.png, our estimated trajectory can be found in estimatedTrajectory.png.

## Circuit navigation and video recording

The navigation and recording code are in the file teleop.py. This file also imports the Car.py file which houses the basic implementation of some commands on the robot. This program allows you to teleoperate the robot using the keyboard. While driving, it will record video and save it to the output path you specify in the teleop.py file line 18. To stop teleoperation and exit recording press x. The controls are w for forward, s for backward, a for left, d for right, and x to stop. The robot will continue to move in the last direction you pressed until you press another direction or x. The space button will stop the robot, and have it wait for the next command, this will not stop the video. To capture the video and perform the odometry we used the teleop.py program to drive in a circuit and record video, and then transferred that video to an external computer to perform the odometry.

## Analysis and report

The report is in the file report.pdf.
