import cv2
import numpy as np
from keras.models import load_model

# Load the pre-trained Keras model
model = load_model('./model.h5')

# Define the labels for the classes
labels = ['business', 'junk']

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    print(ret,frame)

    # Preprocess the frame for the model
    img = cv2.resize(frame, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = img/255.0

    # Make a prediction using the model
    pred = model.predict(img)
    class_idx = np.argmax(pred[0])
    class_label = labels[class_idx]

    # Overlay the predicted class on the input window
    cv2.putText(frame, class_label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the input window with the overlay
    cv2.imshow('Input Window', frame)

    # Exit the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

