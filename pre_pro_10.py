import os
import cv2
import json
import numpy as np

# Define the input JSON file and output directory
json_file = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/frames.json'
output_directory = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/prepro_image_10'

# Define image preprocessing function
def preprocess_image(image, target_size=(512, 512)):
    # Calculate the desired size for the image
    target_height, target_width = target_size

    # Calculate the aspect ratio of the original image
    original_height, original_width, _ = image.shape
    aspect_ratio = original_width / original_height

    # Determine which dimension to use for resizing without distortion
    if aspect_ratio >= 1.0:
        new_width = target_width
        new_height = int(target_width / aspect_ratio)
    else:
        new_height = target_height
        new_width = int(target_height * aspect_ratio)

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (new_width, new_height))

    # Create a blank square canvas of the target size
    canvas = np.zeros((target_height, target_width, 3), dtype=np.uint8)

    # Calculate the position to paste the resized image on the canvas
    x_offset = (target_width - new_width) // 2
    y_offset = (target_height - new_height) // 2

    # Paste the resized image onto the canvas
    canvas[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = resized_image

    # Ensure the image has three channels (RGB)
    if canvas.shape[-1] != 3:
        canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)

    # Normalize pixel values to the specified range [0, 1]
    canvas = canvas.astype(np.float32) / 255.0

    return canvas

# Load the JSON file containing frame data
with open(json_file, 'r') as json_file:
    data = json.load(json_file)

# Loop through all frames in the JSON data
for frame_info in data['frames']:
    # Load the original image data from frame_info
    image_data = frame_info['frame_data']

    # Convert the image data to a NumPy array
    image_np = np.array(image_data, dtype=np.uint8)

    # Preprocess the image
    preprocessed_image = preprocess_image(image_np)

    # Construct the output path with the frame's time in seconds
    time_in_seconds = frame_info['time_in_seconds']
    output_filename = f'frame_{time_in_seconds:.1f}.jpg'
    output_path = os.path.join(output_directory, output_filename)

    # Save the preprocessed image
    cv2.imwrite(output_path, (preprocessed_image * 255).astype(np.uint8))

    print(f"Preprocessed and saved: {output_path}")

