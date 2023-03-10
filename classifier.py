import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

epochs = 220
batch_size = 5
train_dir = './data_scans/'

# Define the input shape of the images
input_shape = (128, 128, 3)

# Define the model
model = Sequential([
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(1, activation="sigmoid")
])

# Compile the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Set up the data generator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128, 128),
    batch_size=batch_size,
    class_mode="binary",
    classes=["business", "junk"]
)

# Train the model
print(str(train_generator.samples)+' images')
steps_per_epoch = train_generator.samples // batch_size
history = model.fit(
    train_generator,
    epochs=epochs,
    steps_per_epoch=steps_per_epoch
)
history = history.history['loss']
print(history)

# Save the model
model.save("model.h5")

import matplotlib.pyplot as plt
plt.plot(history)
plt.ylabel('Validation Loss')
plt.xlabel('Epochs')
plt.show

plt.show()
