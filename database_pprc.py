import os
import csv

root_folder = '/Users/Vante/Library/CloudStorage/OneDrive-UniversityofToronto/Meltzer Lab/NIH_MEG/sc_cate/prepro_image_10'
image_data = []

# Function to extract time in seconds from the filename
def extract_time(filename):
    parts = filename.split('_')
    if len(parts) >= 2:
        time_info = parts[1].split('.')[0]
        return float(time_info)
    return 0.0

# Iterate through image files in the root folder
for filename in os.listdir(root_folder):
    if filename.endswith(".jpg"):
        class_label = ""  # Initialize class label, you can fill this based on your object detection results
        time_in_seconds = extract_time(filename)
        image_info = {
            "file_path": os.path.join(root_folder, filename),
            "class_label": class_label,
            "time_info_in_seconds": time_in_seconds
        }
        image_data.append(image_info)

# Sort the image_data list based on time_info_in_seconds
image_data.sort(key=lambda x: x["time_info_in_seconds"])

# Define the CSV file
csv_file = "image_data.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["file_path", "time_info_in_seconds", "class_label"])
    writer.writeheader()
    writer.writerows(image_data)
