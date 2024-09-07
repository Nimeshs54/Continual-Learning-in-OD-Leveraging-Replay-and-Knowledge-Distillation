import os

# Class mapping
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

# Define classes to include
included_classes = set([0, 1, 2, 3, 4])

# Directories
images_dir = "SynData/KD-1/train/images-old"
labels_dir = "SynData/KD-1/train/labels-old"

# Output directories
output_images_dir = "SynData/KD-1/train/images"
output_labels_dir = "SynData/KD-1/train/labels"

# Create output directories if they don't exist
os.makedirs(output_images_dir, exist_ok=True)
os.makedirs(output_labels_dir, exist_ok=True)

# Iterate through image and label files
for img_file in os.listdir(images_dir):
    if img_file.endswith(".jpg"):
        label_file = img_file.replace(".jpg", ".txt")
        img_label_path = os.path.join(labels_dir, label_file)
        
        # Read labels
        with open(img_label_path, "r") as f:
            labels = f.readlines()
        
        # Check if labels contain only included classes
        keep_image = True
        for label in labels:
            class_id = int(label.split()[0])
            if class_id not in included_classes:
                keep_image = False
                break
        
        if keep_image:
            # Copy image
            img_src_path = os.path.join(images_dir, img_file)
            img_dest_path = os.path.join(output_images_dir, img_file)
            os.system(f"cp {img_src_path} {img_dest_path}")
            
            # Copy label
            label_src_path = os.path.join(labels_dir, label_file)
            label_dest_path = os.path.join(output_labels_dir, label_file)
            os.system(f"cp {label_src_path} {label_dest_path}")
