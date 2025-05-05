import cv2
import os

output_folder = "add_ox"

video_name = "output_video.avi"
images = sorted(os.listdir(output_folder))

# Read the first image to get dimensions
frame = cv2.imread(os.path.join(output_folder, images[0]))
height, width, layers = frame.shape

# Create a video writer
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

# Add images to the video
for image in images:
    video.write(cv2.imread(os.path.join(output_folder, image)))

# Release the video writer
cv2.destroyAllWindows()
video.release()
