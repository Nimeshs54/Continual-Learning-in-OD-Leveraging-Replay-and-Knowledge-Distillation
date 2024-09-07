import os

# Path to the main folders
main_folder = '/home/nimesh/yolov5/bund_1'

# Classes to be removed
classes_to_remove = {17: 'sofa', 18: 'train', 19: 'tvmonitor'}

# List of remaining classes
remaining_classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
                     'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep']

def remove_classes_from_folders():
    # Iterate through each remaining class
    for class_name in remaining_classes:
        class_folder = os.path.join(main_folder, class_name)

        # Check if the class folder exists
        if os.path.exists(class_folder):
            images_subfolder = os.path.join(class_folder, 'images')
            labels_subfolder = os.path.join(class_folder, 'labels')

            # Iterate through each file in 'images' folder and 'labels' folder
            for img_name in os.listdir(images_subfolder):
                img_label_name = img_name[:-4] + '.txt'

                # Check if the current class is not in classes_to_remove
                if class_name not in classes_to_remove.values():
                    # Remove image and label files
                    os.remove(os.path.join(images_subfolder, img_name))
                    os.remove(os.path.join(labels_subfolder, img_label_name))

# Remove images and labels for specified classes
remove_classes_from_folders()
