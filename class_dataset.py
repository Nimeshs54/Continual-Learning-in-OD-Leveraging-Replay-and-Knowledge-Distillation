import os
import xml.etree.ElementTree as ET
from shutil import copyfile

# Path to the Pascal VOC 2007 dataset
voc_path = '/home/nimesh/yolov5/T6_CF/train'

# Output directories to save the filtered images and annotations for "tvmonitor" class
output_image_path = '/home/nimesh/yolov5/T6_CF/train/images'
output_annotation_path = '/home/nimesh/yolov5/T6_CF/train/anno'

# Create output directories if they don't exist
os.makedirs(output_image_path, exist_ok=True)
os.makedirs(output_annotation_path, exist_ok=True)

def filter_tvmonitor_images_and_annotations():
    # Iterate through each image annotation file
    for root, dirs, files in os.walk(os.path.join(voc_path, 'Annotations')):
        for file in files:
            if file.endswith('.xml'):
                xml_path = os.path.join(root, file)
                image_path = os.path.join(voc_path, 'JPEGImages', file.replace('.xml', '.jpg'))

                # Parse XML file
                tree = ET.parse(xml_path)
                xml_root = tree.getroot()

                # Extract classes from the XML file
                classes = [obj.find('name').text for obj in xml_root.findall('.//object')]

                # Check if the image contains the "tvmonitor" class
                if 'tvmonitor' in classes:
                    # Copy the image to the output directory
                    output_image = os.path.join(output_image_path, file.replace('.xml', '.jpg'))
                    copyfile(image_path, output_image)

                    # Save the corresponding annotation in the new annotation folder
                    output_annotation = os.path.join(output_annotation_path, file)
                    copyfile(xml_path, output_annotation)

# Run the filtering process
filter_tvmonitor_images_and_annotations()
