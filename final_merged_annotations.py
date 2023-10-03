import os
import pandas as pd

base_path = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cat'

# Load VGG Annotations
vvg_annotations_file = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/output_data.csv'
vvg_annotations = pd.read_csv(os.path.join(base_path, vvg_annotations_file))

# Load Open Images Annotations
images_boxable_file = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/human_anotation/train/annotations-human.csv'
images_boxable = pd.read_csv(os.path.join(base_path, images_boxable_file))

# Merge Annotations
annotations_bbox_file = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/human_anotation/validation/annotations-human.csv'
annotations_bbox = pd.read_csv(os.path.join(base_path, annotations_bbox_file))

# Load Class Descriptions
class_description_file = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/class-descriptions-boxable.csv'
class_description = pd.read_csv(os.path.join(base_path, class_description_file))

# Merge Annotations with Class Descriptions
merged_annotations = pd.merge(annotations_bbox, class_description, left_on='LabelName', right_on='LabelName', how='left')

# Merge Additional Attributes (XMin, YMin, XMax, YMax, IsOccluded, IsTruncated, IsGroupOf, IsDepiction, IsInside)


# Step 4: Save the Merged Annotations
merged_annotations.to_csv('final_merged_annotations.csv', index=False)




