import cv2
import json

video_path = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/Growth_cropped.mp4'

cap = cv2.VideoCapture(video_path)  # Corrected the variable name

frame_interval = 10  # Extract a frame every 10 seconds
frames = []
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % (frame_interval * int(cap.get(cv2.CAP_PROP_FPS))) == 0:
        # Convert the frame to a JSON-friendly format (e.g., list of lists)
        frame_data = frame.tolist()
        frames.append(frame_data)

cap.release()

output_json_file = 'frames.json'
with open(output_json_file, 'w') as json_file:
    json.dump(frames, json_file)
