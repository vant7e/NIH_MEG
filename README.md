# NIH_MEG

## Overview
This repository contains code and data for object detection tasks and eye movement experiments. It includes manual annotations for a subset of images from the Open Images Dataset V3 and V6 and instructions on training a Faster R-CNN model for object detection using TensorFlow and Torch.

TEST_TRAINED_ANONATED_ IAMGES = 50 ('prepro_image_10.zip') : 50 manual pre-processed frames from video

## Preprocessing
Before training the object detection model, ensure that the input images are of the appropriate size for your chosen Faster R-CNN model. You can use the provided image preprocessing function to resize and normalize images.


      # Define image preprocessing function
      def preprocess_image(image, target_size=(512, 512)):
          # Resize the image to match the model input size (e.g., 640x640)
          image = cv2.resize(image, target_size)
          # Ensure the image has three channels (RGB)
          if image.shape[-1] != 3:
              image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
          # Normalize pixel values to the range [0, 1]
          image = image.astype(np.float32) / 255.0
          return image

# Annotations

        Prepared Training data = 'object_task_train_10_VVG_anonated.csv' as 'Human_anonated.csv'
        
  manual_label_anonated.cvs = (selected LabelName ('Image_Label_Name, Class_name') to generate Xmin, Ymin, Xmax, and Ymax for bounding box ('bbx')  : 
      
      # The CSV file includes the following attributes:
      
       = {
    
    filename: Image file name
    
    file_size: File size
    region_count: Number of regions (bounding boxes)
    region_id: Region ID
    region_shape_attributes: Attributes of the region's shape
    region_attributes: Region attributes, including class labels
      }
      
    ATTRIBUTION SET VALUE = {' 
      NAME = Class_Name
      ASSIGNED_ID =  Label_used_in_Annotations = 26 #Can be changed as need
          {
          Description of ID # An identifier for the object class;
          Definition of ID  #Use this attribute to specify the type of object present in the region
          /m/03jm5 House
          /m/0k4j Car
          /m/07j7r Tree
          /m/01g317 Person
          /m/0138tl Toy
          /m/02s195 Vase
          /m/0h8n5zk Kitchen & dining room table
          /m/0fszt Cake
          /m/01mzpv Chair
          /m/03fp41 Houseplant
          /m/06z37_ Picture Frame
          /m/02dgv Door
          /m/03_wxk Kitchenware
          /m/07c52  Television
          /m/02x984l Mechanical fan
          /m/01s55n Suitcase
          /m/0fqfqc Drawer
          /m/0bt_c3 Book
          /m/0dtln Lamp
          /m/031b6r WindowBlind
          /m/0d4v4 Window
          /m/03m3pdh SofaBed
          /m/02wbm Food
          /m/025nd Christmas tree
          /m/04169hn Wood-burning stove
          /m/0gjbg72 Shelf
          }
      DEFINITION = 'YES' OR 'NO'
      TPYE: DROPDPOWN (since you want annotators to select from predefined classes).
      
    filename,file_size,file_attributes,region_count,region_id,region_shape_attributes,region_attributes...
    e.g.,
    frame_10.0.jpg,70421,"{}",4,0,"{"name"":""rect"",""x"":187,""y"":258,""width"":61,""height"":43}","{""class_name"":""/m/01g317"}"#
    Openimage_label_Name = ('class-descriptions-boxable.csv')

        Export_Annotations_pathway = ('object_task_train_10_VVG_anonated.csv'}
    attributes:

 
  ***Label_Name**:  
  
  represents the class label or category of an object in an image. It is often associated with a unique identifier (e.g., "/m/05_4_") that corresponds to a specific object category.*
  
    Each LabelName indicates what kind of object is present in the image. For example, "/m/05_4_" might correspond to "Car," and "/m/04hgtk" might correspond to "House." 

  ***Confidence***: 
  
  indicates the level of confidence or certainty associated with the assigned label or category. It's typically a value between 0 and 1, where 0 indicates low confidence, and 1 indicates high confidence.*
  
    A high confidence value suggests that the label is considered reliable, while a low confidence value might indicate uncertainty.

  ***Source**: 
  
  attribute indicates how the annotation was created:
  
        "machine" indicates machine-generated labels.

  ***Bounding Box**: 
  
  Attributes (XMin, XMax, YMin, YMax): define the coordinates of bounding boxes around objects in the images & Specify the location and size of objects within the image.
    
    XMin and YMin =  the minimum x and y coordinates of the bounding box, while XMax and YMax represent the maximum x and y coordinates.

  ***Additional Bounding Box Attributes (IsOccluded, IsTruncated, IsGroupOf, IsDepiction, IsInside)***: 
  
  attributes provide additional information about the bounding boxes:
      
      IsOccluded: Indicates if the object is occluded by another object.
      IsTruncated: Indicates if the object extends beyond the image boundary.
      IsGroupOf: Indicates that the bounding box contains a group of objects.
      IsDepiction: Indicates that the object is a depiction, such as a drawing or cartoon.
      IsInside: Indicates if the image was taken from inside the object.

# Combine Human Annotation with Open Images Dataset V3

  *IMPORTANT* Merge the annotations while ensuring there are no naming conflicts or duplicates with Open Images Dataset V3 & V6:

      REAL_COORDINATES_PATHWAY = 'real_coordinates.py'

      # Assuming the 'region_shape_attributes' column contains JSON strings in CSV

              data['region_shape_attributes'] = data['region_shape_attributes'].apply(json.loads)
              
              # Extract XMIN, XMAX, YMIN, YMAX into separate columns
              data['XMIN'] = data['region_shape_attributes'].apply(lambda x: x.get('x'))
              data['YMIN'] = data['region_shape_attributes'].apply(lambda x: x.get('y'))
              data['XMAX'] = data.apply(lambda row: row['XMIN'] + row['region_shape_attributes'].get('width', 0), axis=1)
              data['YMAX'] = data.apply(lambda row: row['YMIN'] + row['region_shape_attributes'].get('height', 0), axis=1)
              
              # Drop the original 'region_shape_attributes' column
              data.drop(columns=['region_shape_attributes'], inplace=True)
              
              # Assuming the 'region_attributes' column contains JSON strings in CSV
              data['region_attributes'] = data['region_attributes'].apply(json.loads)
              
              # Extract the "class_name" value and rename the column to "LabelName"
              data['LabelName'] = data['region_attributes'].apply(lambda x: x.get('class_name'))
              
              # Drop the original 'region_attributes' column
              data.drop(columns=['region_attributes'], inplace=True)
              
              # Save the modified DataFrame back to a CSV file
              data.to_csv('output_data.
              CSV, index=False)

  * Open Images Dataset V3 & V6 FOR LABEL ARE TOO LARGE SO I CANNOT COMPLETELY RUN IN MY COMPUTER; (*

  COMPARISON: 
  Before merging the annotations and open image datasets; 
  
    HUMAN_ANONATED_LABEL =  
      /m/01g317 Person ('LabelName'; 'Class_name')

  AFRER MERGE the annotations: 

   NEW Image-level labels with high accuracy (one file each for training, validation, and testing):
    
    final_merged_annotations.cvs(Unsuccessfully completed BUT) = 
    
    { 
    image id, Source, LabelName, Confidence,

    000a1249af2bc5f0,verification,/m/014sv8,0,Human eye
    000ada55d36b4bcb,crowdsource-verification,/m/02wbm,1,Food
    
    000a1249af2bc5f0,verification,/m/01g317,1,Person FURTHER EXPAND INTO = {
  
        000a1249af2bc5f0,verification,/m/0283dt1,0,Human mouth
        000a1249af2bc5f0,verification,/m/03bt1vf,1,Woman
        000a1249af2bc5f0,verification,/m/04hgtk,0,Human head
        000a1249af2bc5f0,verification,/m/0dzct,0,Human face
        000a1249af2bc5f0,verification,/m/0k0pj,0,Human nose
      },

    00b4064b073e51f3,verification,/m/05s2s,0,Plant
    00b562abdf5766d3,verification,/m/07mhn,0,Trousers
    00b562abdf5766d3,verification,/m/09j2d,0,Clothing
    00b562abdf5766d3,verification,/m/0fly7,0,Jeans
    00b4064b073e51f3,verification,/m/0c9ph5,0,Flower
    00b4064b073e51f3,verification,/m/02wbm,0,Food
    00b4064b073e51f3,verification,/m/0f4s2w,1,Vegetable
    00b585e025287555,verification,/m/01j51,1,Balloon
    ...
    }

  
# Training_Environment 

The training environment ('Pre_trained.py') = 0.7 (Test) & 0.15 (Train) & 0.15 (Validation)
  Data split: 70% for testing, 15% for training, and 15% for validation.
  Loading weights
  Optimizer settings
  Loss function
  
 Loading Weights =?
 optimizer = 
 function loss = 
            
               x_img: image data after resized and scaling (smallest size = 300px)
               Y: [y_rpn_cls, y_rpn_regr]
               img_data_aug: augmented image data (original image with augmentation)
               debug_img: show image for debug
               num_pos: show the number of positive anchors for debug
 
 The Threshold of Object recognition = {
   Fine-tune the model or adjust hyperparameters as needed to improve performance

# Important Note

Please note that the Open Images Dataset V3 and V6 contain a large number of labels and data, which may require significant computational resources to process completely.
For Growth_cropped.mp4, Human_annotation = 1000 to 2000 manually annotated can yield a highly accurate model.

TOTAL_FRAME = 12,699
TEST = (1905) as 0.15 (Train)
VALIDATION (1905) = as 0.15 (VALIDITATION)
TEST = 8889


    
