# NIH_MEG_MELTZER
Object_detection_task &amp; eye_movement_experiment
# Image Classification and Object Detection

This repository contains code for object detection and eye movement experiments using video stimuli.

## Table of Contents
- [Introduction](#introduction)
- [Scripts](#scripts)
  - [sc_10sec.py](#sc_10secpy)
  - [VGG_dl.py](#vgg_dlpy)
  - [sc_10sec_10.py](#sc_10sec_10py)
  - [database_pprc.py](#database_pprcpy)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction

This project focuses on object detection tasks and eye movement experiments using video stimuli. The scripts are provided to extract features from video frames and classify them using the VGG16 model, object detection based on the TF_Lite3&4 model, and deep training of the modified model on labeled VGG dataset and Growth_cropped. mp4.

# 1 sc_10sec.py: Extract features from frames of the video stimuli presented to participants, 
 	# Extract a frame every 10 seconds, Change as Need
 	frame_interval = 10 
 	frames = []
	frame_count = 0

	saved as JSON.file; AS 
	output_json_file = 'frames.json'
	with open(output_json_file, 'w') as json_file:
  	json.dump(frames, json_file)
	Result_Pathway = '/IMAGE_CLASSIFICATION/FRAME_TEST.JSO.FILE'
	
 	# saved as JPGfile (pathway = Frame_Extraction.py);   # Save the frame with a filename including the time for the further interpreter
	# Calculate the time in seconds for the current frame # Extract a frame every 1 second
  	  time_in_seconds = frame_count / cap.get(cv2.CAP_PROP_FPS)

   	 # Save the frame with a filename including the time
   	 frame_filename = os. path.join(output_directory, f'frame_{time_in_seconds:.2f}.jpg')
    	cv2.imwrite(frame_filename, frame)

   	 frame_count += 1
	# Release the video capture object and close the windows
	cap. release()
	cv2.destroyAllWindows()
	# Results: Example = 'Frame_Extraction.py'

    
# 2 VVG_dl.py: Each frame of the video can be passed through the VGG16 model to obtain a feature vector representing the content of that frame
 	
	# Decode and print the top-5 predicted classes for each frame; change as the need
 
  	  for i, prediction in enumerate(predictions):
        decoded_predictions = decode_predictions(np.expand_dims(prediction, axis=0), top=5)[0]
        print(f"Predictions for Frame {i}:")
        for j, (imagenet_id, label, score) in enumerate(decoded_predictions):
            print(f"{j + 1}: {label} ({score:.2f})")
	    
  	# results.txt: These feature vectors can then be used as input features for further MEG data analysis, for example; 
	Predictions for Frame 0:
	1: thatch (0.99)
	2: boathouse (0.00)
	3: yurt (0.00)
	4: barn (0.00)
	5: picket_fence (0.00)
	  *NEED TO BE MANUALLY CORRECT*

# 3 sc_10sec_10.py: Extracted from Growth_cropped.mo4 video every 10 seconds* Extension for sc_10_sec_10.py:
  	# the image filenames to be in the format of frame_time_in_second.jpg,
   	# can be saved as the results as a JSON file and exported as a CSV or text file indicating the further recognized object classes in each frame, easier for post-processing.
	# Applied to next steps database_for_post_processing_pathway = 'database_pprc.py'
 
# 4 database_pprc.py: containing frames.json file from video, which includes class labels for further object recognition task in annotated images, and export a CSV or text file indicating what kind of object class is recognized in each frame
	#Create a list to store frame-to-class mapping
 	frame_to_class = []
 	for result in detection_results:
    frame_number = result['frame_number']  # Assuming 'frame_number' is present
    class_label = result['class_label']    # Assuming 'class_label' is present
    frame_to_class.append({'frame_number': frame_number, 'class_label': class_label})
	can access object detection results like bounding box coordinates and class labels for each frame in your loop, and also access the frame-to-class mapping from the exported CSV or text file as needed for further analysis or reporting.
 	# result_pathway = 'image_data.csv'

# Results 
	# 1: VVG_16_IMAGE_CLASSIFICATION = 'Results.txt'
 	# 2: sc_10sec_10.py = 'frames.json'
  	# 3. sc_10sec.py = 'frames_test.json
   	# 4. database_pprc.py = image_data.csv'
