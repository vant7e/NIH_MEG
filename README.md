# image_classification
Object_detection_task &amp; eye_movement_experiment
# Image Classification and Object Detection

This repository contains code for object detection and eye movement experiments using video stimuli.

## Table of Contents
- [Introduction](#introduction)
- [Scripts](#scripts)
  - [sc_10sec.py](#sc_10secpy)
  - [VGG_dl.py](#vgg_dlpy)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction

This project focuses on object detection tasks and eye movement experiments using video stimuli. The scripts are provided to extract features from video frames and classify them using the VGG16 model, object detection based on the TF_Lite3&4 model & Deep training of the modified model on labeled VGG dataset and Growth_cropped. mp4.

#1 sc_10sec.py: 
Extract features from frames of the video stimuli presented to participants, 
	frame_interval = 10  # Extract a frame every 10 seconds, Change as Need
frames = []
frame_count = 0

#saved as JSON.file; AS 
output_json_file = 'frames.json'
with open(output_json_file, 'w') as json_file:
    json.dump(frames, json_file)
Result_Pathway = '/IMAGE_CLASSIFICATION/FRAME.JSO.FILE'

#saved as JPGfile;   # Save the frame with a filename including the time for further interpreter
	# Calculate the time in seconds for the current frame
  	  time_in_seconds = frame_count / cap.get(cv2.CAP_PROP_FPS)

    # Save the frame with a filename including the time
   	 frame_filename = os. path.join(output_directory, f'frame_{time_in_seconds:.2f}.jpg')
    	cv2.imwrite(frame_filename, frame)

   	 frame_count += 1
	# Release the video capture object and close the windows
	cap. release()
	cv2.destroyAllWindows()
#Example = '/IMAGE_CLASSIFICATION/Frame_Extraction.py'
    
#2 VVG_dl.py: 
Each frame of the video can be passed through the VGG16 model to obtain a feature vector representing the content of that frame
 # Decode and print the top-5 predicted classes for each frame; change as need
    for i, prediction in enumerate(predictions):
        decoded_predictions = decode_predictions(np.expand_dims(prediction, axis=0), top=5)[0]
        print(f"Predictions for Frame {i}:")
        for j, (imagenet_id, label, score) in enumerate(decoded_predictions):
            print(f"{j + 1}: {label} ({score:.2f})")
  #results.txt
  These feature vectors can then be used as input features for further MEG data analysis, for example; 
	Predictions for Frame 0:
	1: thatch (0.99)
	2: boathouse (0.00)
	3: yurt (0.00)
	4: barn (0.00)
	5: picket_fence (0.00)
  *NEED TO BE MANUALLY CORRECT*
