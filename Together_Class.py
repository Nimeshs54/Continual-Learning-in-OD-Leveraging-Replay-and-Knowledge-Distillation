import os
import shutil

# Set the paths to your image and label folders
image_folder_path = '/home/nimesh/yolov5/KG-M2/val/img'
label_folder_path = '/home/nimesh/yolov5/KG-M2/val/lab'

# Set the class mapping
# class_mapping = {
#     'aeroplane': 0,
#     'bicycle': 1,
#     'bird': 2,
#     'boat': 3,
#     'bottle': 4,
#     'bus': 5,
#     'car': 6,
#     'cat': 7,
#     'chair': 8,
#     'cow': 9,
#     'diningtable': 10,
#     'dog': 11,
#     'horse': 12,
#     'motorbike': 13,
#     'person': 14,
#     'pottedplant': 15,
#     'sheep': 16,
#     'sofa': 17,
#     'train': 18,
#     'tvmonitor': 19
# }

class_mapping = {
    'BlackLid': 0,
    'BlackTrailer': 1,
    'FUEHRERHAUS_B_ROT_ANBINDUNG_OBEN': 2,
    'GlueGun':3,
    'INCORAP_DECKEL_VIERECKE': 4,
    'INCORAP_TRAILER_BODY_WHITE': 5,
    '_98_CAB_CHASSIS': 6,
    '_98_SEMITRAILER_CHASSIS': 7
}

# Create a list to store file names with both "car" and "person" classes
selected_files = []

# Iterate through the image folder
for image_filename in os.listdir(image_folder_path):
    image_name, image_extension = os.path.splitext(image_filename)

    # Check if corresponding label file exists
    label_filename = image_name + '.txt'
    label_filepath = os.path.join(label_folder_path, label_filename)

    if os.path.exists(label_filepath):
        # Read the content of the label file
        with open(label_filepath, 'r') as label_file:
            labels = label_file.readlines()

            # Extract class numbers from the label file
            classes = [int(label.split()[0]) for label in labels]

            # Check if both "car" and "person" classes are present
            if 6 in classes and 14 in classes:
                selected_files.append(image_filename)

# Create new folders if they don't exist
output_image_folder = '/home/nimesh/yolov5/KG-M2/val/images'
output_label_folder = '/home/nimesh/yolov5/KG-M2/val/labels'

os.makedirs(output_image_folder, exist_ok=True)
os.makedirs(output_label_folder, exist_ok=True)

# Copy selected files to new folders
for selected_file in selected_files:
    shutil.copy(os.path.join(image_folder_path, selected_file), output_image_folder)
    shutil.copy(os.path.join(label_folder_path, selected_file.replace('.jpg', '.txt')), output_label_folder)

print("Selected files have been copied to the new folders.")
