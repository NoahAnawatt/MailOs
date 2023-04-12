import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load the model
model = tf.keras.models.load_model("fmodel.h5")

# Set up the image processing parameters
img_width, img_height = 128, 128
classes = ["business","junk"]

# Process each image in the training directory
train_dir = "./data_scans/"
if not os.path.exists(train_dir):
    raise ValueError("Training directory does not exist!")
true_counts = 0
total_counts = 0
for class_name in classes:
    class_dir = os.path.join(train_dir, class_name)
    for img_file in os.listdir(class_dir):
        img_path = os.path.join(class_dir, img_file)
        img = image.load_img(img_path, target_size=(img_width, img_height))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        pred = model.predict(images)
        class_idx = int(np.round(pred[0]))
        class_name = classes[class_idx]
        print(f"Predicted class for image {img_path}: {class_name}")
        total_counts += 1
        if class_name in img_path:
            true_counts += 1
print(f'---DONE--- Results: {true_counts}/{total_counts}; {(true_counts/total_counts)*100}%')
