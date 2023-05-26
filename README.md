# Driver Drowsy Detection

## Abstract
Driver drowsiness is a significant contributor to road accidents, posing a threat to both the driver and other road users. This repository presents an analysis of a comprehensive dataset specifically collected for driver drowsiness detection research. The dataset provides a valuable resource for developing and evaluating effective drowsiness detection algorithms. In this repository, we describe the dataset, its characteristics, data collection process, preprocessing steps, and ethical considerations. Furthermore, we outline the subsequent steps taken to train and evaluate a drowsiness detection model using this dataset, with the aim of contributing to the advancement of driver safety systems.

## Dataset Description
In this section, we provide an overview of the dataset used for driver drowsiness detection. The dataset includes images showcasing drivers in different scenarios, such as day and night driving, varying lighting conditions, and diverse driver demographics. The dataset does not include any augmentation techniques applied to the original images.

## Labeling and Annotation Process
We performed labeling and annotation using Roboflow. Each image was carefully cropped and labeled for our drowsiness project. The dataset includes four categories: open eye, closing eye, no yawn, and yawn, ensuring accurate categorization. Our goal was to develop a comprehensive dataset that includes a variety of settings and variations in sleepiness levels. Through the annotation process, we accurately identified and indicated the important characteristics of each image to provide the model with accurate data for learning and generalization.

## Augmentation Steps
During the training process, we applied augmentations to enhance the diversity and robustness of the dataset. These augmentations included horizontal flip, crop, rotation, shear, and brightness adjustments. These techniques collectively contribute to training a more robust and versatile model capable of handling variations in orientation, scale, and lighting conditions.

## Training the Data
In our dataset, we allocated 88% for training, 8% for validation, and 4% for testing. This ratio was chosen based on limited data size, sufficient training data, and adequate validation data. We used Ultralytics YOLO v8 for model training and OpenCV for face detection. The trained model accurately detects the features it was trained on.

## Code for Model Prediction Process
After training the model, we utilize YOLO from the Ultralytics library to import the model. The predict function is then used to obtain predicted frames from the input, which is set to the webcam source. The YOLO part is hidden, and the output is shown using OpenCV. The system detects closed eyes and yawns for consecutive frames to determine drowsiness, and if open eyes are detected, it is classified as awake.

## Hardware Connection and Inference Produced by Model
To use the model, first, flash an SD card with the Raspberry Pi image and insert it into a Raspberry Pi 64-bit device. Connect a monitor using an HDMI cable, and connect a webcam, mouse, and keyboard to the USB ports.




