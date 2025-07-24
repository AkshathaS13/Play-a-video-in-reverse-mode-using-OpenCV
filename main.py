# Python program to play a video in reverse mode using OpenCV

# Import cv2 library
import cv2

# Pass absolute address of video file 
cap = cv2.VideoCapture("C:/simple Project/reversevideo.mp4")

# Initialize the value of check variable
check = True

# List to store frames
frame_list = []

# Keep looping until we get False value of check
while check:
    # Read a frame from the video
    check, vid = cap.read()
    
    # If frame is read successfully, append it to the list
    if check:
        frame_list.append(vid)

# Release the video capture object
cap.release()

# Reverse the order of the frames in the list
frame_list.reverse()

# Looping through the reversed list of frames
for frame in frame_list:
    # Show the frame
    cv2.imshow("Frame", frame)
    
    # Wait for a key press; if 'q' is pressed, exit the loop
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Close any open windows
cv2.destroyAllWindows()
