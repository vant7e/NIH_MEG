import json
import cv2
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppress TensorFlow warnings

# Disable SSL certificate verification for model download (not recommended for production)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Load the VGG16 model
model = VGG16(weights='imagenet')

# Load the JSON file containing extracted frames
with open('/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/frames.json', 'r') as json_file:
    frames_data = json.load(json_file)

def preprocess_frame(frame):
    # Ensure that the frame is not empty
    if frame is None:
        return None

    # Ensure that the frame has three channels (RGB)
    if frame.shape[-1] != 3:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Calculate the dimensions for cropping a central 224x224 portion
    new_height = min(height, 224)
    new_width = min(width, 224)
    crop_y = (height - new_height) // 2
    crop_x = (width - new_width) // 2

    # Crop the central portion of the frame
    frame = frame[crop_y:crop_y + new_height, crop_x:crop_x + new_width]

    # Resize the cropped frame to 224x224
    frame = cv2.resize(frame, (224, 224))

    # Normalize pixel values to the range expected by VGG16
    frame = preprocess_input(frame)

    return frame

# Preprocess all frames and filter out any invalid frames
preprocessed_frames = [preprocess_frame(np.array(frame)) for frame in frames_data if preprocess_frame(np.array(frame)) is not None]

# Check if there are any frames left after preprocessing
if not preprocessed_frames:
    print("No valid frames found after preprocessing.")
else:
    # Load the pre-trained VGG16 model
    model = VGG16(weights='imagenet')

    # Make predictions on the frames
    predictions = model.predict(np.array(preprocessed_frames))

    # Decode and print the top-5 predicted classes for each frame
    for i, prediction in enumerate(predictions):
        decoded_predictions = decode_predictions(np.expand_dims(prediction, axis=0), top=5)[0]
        print(f"Predictions for Frame {i}:")
        for j, (imagenet_id, label, score) in enumerate(decoded_predictions):
            print(f"{j + 1}: {label} ({score:.2f})")
