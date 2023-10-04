import pandas as pd
import json

# Load your CSV data into a DataFrame
data = pd.read_csv('/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/object_task_train_10_VVG_anonated.csv')

# Load the class-descriptions-boxable.csv file
class_descriptions = pd.read_csv('/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/class-descriptions-boxable.csv', names=['LabelName', 'Class'])

# Assuming the 'region_shape_attributes' column contains JSON strings in CSV
data['region_shape_attributes'] = data['region_shape_attributes'].apply(json.loads)

# Extract XMin, XMax, YMin, YMax into separate columns
data['XMin'] = data['region_shape_attributes'].apply(lambda x: x.get('x'))
data['XMax'] = data.apply(lambda row: row['XMin'] + row['region_shape_attributes'].get('width', 0), axis=1)
data['YMin'] = data['region_shape_attributes'].apply(lambda x: x.get('y'))
data['YMax'] = data.apply(lambda row: row['YMin'] + row['region_shape_attributes'].get('height', 0), axis=1)

# Drop the original 'region_shape_attributes' column
data.drop(columns=['region_shape_attributes'], inplace=True)

# Assuming the 'region_attributes' column contains JSON strings in CSV
data['region_attributes'] = data['region_attributes'].apply(json.loads)

# Drop the "class_name" key from 'region_attributes' while keeping the rest of the JSON
data['LabelName'] = data['region_attributes'].apply(lambda x: x.get('class_name'))

# Merge with class descriptions to get the "class" column
data = data.merge(class_descriptions, on='LabelName', how='left')

# Drop the original 'region_attributes' column
data.drop(columns=['region_attributes'], inplace=True)

# Save the modified DataFrame back to a CSV file
data.to_csv('output_data.csv', index=False)



