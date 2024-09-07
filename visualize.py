import cv2
import os

def visualize_object_detection(images_folder, labels_folder, destination_folder):
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Get list of image files
    image_files = os.listdir(images_folder)
    image_files = [file for file in image_files if file.endswith('.jpg') or file.endswith('.png')]

    # Loop through each image
    for image_file in image_files:
        image_path = os.path.join(images_folder, image_file)
        label_path = os.path.join(labels_folder, os.path.splitext(image_file)[0] + '.txt')

        # Read image
        image = cv2.imread(image_path)

        # Read labels
        with open(label_path, 'r') as f:
            labels = f.readlines()

        # Loop through each label
        for label in labels:
            class_id, x_center, y_center, width, height = map(float, label.split())
            
            # Convert YOLO format to coordinates
            height, width, _ = image.shape
            x_center *= width
            y_center *= height
            width *= width
            height *= height

            # Calculate bounding box coordinates
            x1 = int(x_center - width / 2)
            y1 = int(y_center - height / 2)
            x2 = int(x_center + width / 2)
            y2 = int(y_center + height / 2)

            # Draw bounding box on image
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Save visualized image
        destination_path = os.path.join(destination_folder, image_file)
        cv2.imwrite(destination_path, image)

if __name__ == "__main__":
    images_folder = "rand_test/images"
    labels_folder = "rand_test/labels"
    destination_folder = "rand_test/viz"
    
    visualize_object_detection(images_folder, labels_folder, destination_folder)
