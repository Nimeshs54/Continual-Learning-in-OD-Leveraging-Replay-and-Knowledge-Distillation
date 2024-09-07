import os
import shutil

# Path to the main folders
main_folder = '/home/nimesh/yolov5/bunddel'
images_folder = os.path.join(main_folder, 'JPEGImages')
labels_folder = os.path.join(main_folder, 'labels')

# Mapping of class labels for YOLO format
class_mapping = {0: 'aeroplane', 1: 'bicycle', 2: 'bird', 3: 'boat', 4: 'bottle',
                 5: 'bus', 6: 'car', 7: 'cat', 8: 'chair', 9: 'cow',
                 10: 'diningtable', 11: 'dog', 12: 'horse', 13: 'motorbike',
                 14: 'person', 15: 'pottedplant', 16: 'sheep', 17: 'sofa',
                 18: 'train', 19: 'tvmonitor'}

def organize_images_and_labels():
    # Iterate through each image
    for img_name in os.listdir(images_folder):
        if img_name.endswith('.jpg'):
            img_label_name = img_name[:-4] + '.txt'
            
            class_labels_path = os.path.join(labels_folder, img_label_name)

            # Check if the label file exists
            if os.path.exists(class_labels_path):
                with open(class_labels_path, 'r') as label_file:
                    labels_content = label_file.read().strip().split('\n')

                    # Iterate through each class
                    for class_label, class_name in class_mapping.items():
                        class_folder = os.path.join(main_folder, class_name)
                        os.makedirs(class_folder, exist_ok=True)

                        images_subfolder = os.path.join(class_folder, 'images')
                        labels_subfolder = os.path.join(class_folder, 'labels')
                        os.makedirs(images_subfolder, exist_ok=True)
                        os.makedirs(labels_subfolder, exist_ok=True)

                        # Check if the current class label is present in any of the label entries
                        for label_entry in labels_content:
                            if label_entry.startswith(f'{class_label} '):
                                # Copy image to 'images' folder
                                shutil.copy(os.path.join(images_folder, img_name), os.path.join(images_subfolder, img_name))
                                # Copy label to 'labels' folder
                                shutil.copy(class_labels_path, os.path.join(labels_subfolder, img_label_name))
                                break

# Organize images and labels into separate class folders
organize_images_and_labels()
