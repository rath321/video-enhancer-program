import cv2

# Load video
video = cv2.VideoCapture('video.mp4')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('enhanced_video.mp4', fourcc, 20.0, (640, 480))

while(video.isOpened()):
    # Read frame
    ret, frame = video.read()

    if ret == True:
        # Apply enhancement filter
        # for example, let's increase the brightness of the frame by 30%
        frame = cv2.convertScaleAbs(frame, alpha=2, beta=5)

        # Write the output frame
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Enhanced video',frame)
        
        # Press Q on keyboard to stop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
video.release()
out.release()
cv2.destroyAllWindows()