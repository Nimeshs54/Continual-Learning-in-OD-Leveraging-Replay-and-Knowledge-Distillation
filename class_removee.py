import os

# Set the path to your labels folder
# label_folder_path = '/home/nimesh/yolov5/SynData/replay/R4/test/labels'
label_folder_path = '/home/nimesh/yolov5/SynData/KD/KD5/val/labels'

# names: 0: aeroplane 1: bicycle 2: bird 3: boat 4: bottle 5: bus 6: car 7: cat 8: chair 9: cow 10: diningtable 11: dog 12: horse 13: motorbike 
# 14: person 15: pottedplant 16: sheep 17: sofa 18: train 19: tvmonitor


# class_mapping = {
#     'BlackLid': 0,
#     'BlackTrailer': 1,
#     'FUEHRERHAUS_B_ROT_ANBINDUNG_OBEN': 2,
#     'GlueGun':3,
#     'INCORAP_DECKEL_VIERECKE': 4,
#     'INCORAP_TRAILER_BODY_WHITE': 5,
#     '_98_CAB_CHASSIS': 6,
#     '_98_SEMITRAILER_CHASSIS': 7
# }

# Classes to keep
classes_to_keep = {7}
# classes_to_keep = {0, 1, 2, 3, 4, 5, 6}

# Iterate through the label files
for label_filename in os.listdir(label_folder_path):
    label_filepath = os.path.join(label_folder_path, label_filename)

    if os.path.isfile(label_filepath):
        # Read the content of the label file
        with open(label_filepath, 'r') as label_file:
            lines = label_file.readlines()

        # Filter out lines corresponding to classes to be removed
        filtered_lines = [line for line in lines if int(line.split()[0]) in classes_to_keep]

        # Write the filtered content back to the label file
        with open(label_filepath, 'w') as label_file:
            label_file.writelines(filtered_lines)

print("Classes removed from label files.")
