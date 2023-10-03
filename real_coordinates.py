import pandas as pd
import json

# Load your CSV data into a DataFrame
data = pd.read_csv('/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/object_task_train_10_VVG_anonated.csv')

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
data.to_csv('output_data.csv', index=False)


