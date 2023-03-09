# import the opencv library
import cv2 as cv

# set the number of cameras here
num_cameras = 3

# we create an empty list to hold the VideoCapture() objects
video_capture_objects = []

# we create some video capture objects
for camera_index in range(num_cameras):
    print("now using", camera_index)
    video_capture_objects.append(cv.VideoCapture(camera_index))

    print("properties of cap", camera_index, "are:")
    print()
    for j in range(20):
        print("cap", camera_index, ":", video_capture_objects[camera_index].get(j))
    print()

# we select a codec here
fourcc = cv.VideoWriter_fourcc(*'XVID')

# we create an empty list to hold the VideoOutput() objects
video_output_objects = []

# we create some video output objects
for camera_index in range(num_cameras):
    output_file_name = "output" + str(camera_index) + ".avi"
    video_output_objects.append(cv.VideoWriter(output_file_name, fourcc, 30.0, (640, 480), True))

# we now start our capture loop
while True:
#while cap0.isOpened() and cap1.isOpened():

    rets = []
    frames = []
     
    # Capture the video frame by frame
    for i in range(len(video_capture_objects)):
        rets.append(video_capture_objects[i].read()[0])
        frames.append(video_capture_objects[i].read()[1])

    # if the camera isn't working, break it all
    for ret in rets:
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
 
    # Display the resulting frame
    for i in range(len(frames)):
        cv.imshow("frame" + str(i), frames[i])

    # write the flipped frame
    for i in range(len(video_output_objects)):
        video_output_objects[i].write(frames[i])
     
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
 
# after recording, release all video capture objects
for cap in video_capture_objects:
    cap.release()

# after recording, release all video output objects
for out in video_output_objects:
    out.release()

# Destroy all the windows
cv.destroyAllWindows()
