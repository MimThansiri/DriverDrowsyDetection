# DriverDrowsyDetection
Robot Lab Final project 

Abstract:
Driver drowsiness is a significant contributor to road accidents, posing a threat to both the driver
and other road users. This report presents an analysis of a comprehensive dataset specifically
collected for driver drowsiness detection research. The dataset provides a valuable resource for
developing and evaluating effective drowsiness detection algorithms. In this report, we describe
the dataset, its characteristics, data collection process, preprocessing step, and ethical
consideration. Furthermore, we outline the subsequent steps taken to train and evaluate a
drowsiness detection model using this dataset, with the aim of contributing to the advancement
of driver safety systems.
Dataset description:
In this section, we provide an overview of the dataset used for driver drowsiness detection. wWe
describe its source, size, and specific characteristics, along with any unique attributes. The
dataset does not include any augmentation techniques applied to the original images. The
images showcase drivers in different scenarios, such as day and night driving, varying lighting
conditions, and diverse driver demographics.


Labeling and annotation process
We did a labeling and annotation in Roboflow, we carefully analyzed the dataset that we
obtained through extensive searching and browsing. Each image was cropped and we
employed out expertise to label the data for our drowsiness project. The objective of this project
is to develop a model that can accurately identify whether a drier is drowsy or not based on
specific features. We divided the photo into four categories: open eye, closing eye, no yawn and
yawn, to ensure accurate categorization. These characteristics record several drowsiness
related visual indicators in driers. We developed a comprehensive dataset that includes a
variety of settings and variations in sleepless levels by accurately categorizing each image.
Lot of caution was taken through the annotation process to correctly identify and indicate the
important characteristics of each image. Our goal was to give our model the accurate data it
needed to learn and generalize through the training phase through this strict labeling.
Lastly we can move onto training a reliable drowsiness detection model by utilizing the labeled
dataset produced by this careful procedure. By alerting people or appropriate systems when
indicators of sleepiness are found, this model will play a critical role in improving driver safety by
potentially reducing the risks connected with fatigue related incidents on the road.


Augmentation steps:
The augmentations applied during the training process involve generating multiple outputs per
training example. These augmentations contribute to enhancing the diversity and robustness of
the dataset. The horizontal flip augmentation is employed, which creates a mirror image of the
original sample. Additionally, a crop augmentation is applied, ranging from no minimum zoom to
a maximum zoom of 20%. This cropping helps introduce variations in the scale and perspective
of the images. Rotation augmentation is incorporated , randomly rotating the images within a
range of -15° to +15° to simulate different orientations. SHear augmentation is also employed,
with a dataset to encompass a wider range of horizontal and vertical perspectives. Finally,
brightness augmentation is applied, adjusting the brightness of the image byu a factor ranging
from -25% to 25%. These augmentations collectively contribute to training a more robust and
versatile model capable of handling variations in orientation, scale, and lighting conditions.


Training the data:
In our dataset, we trained by using the ratio of training 88%, validation of 8% and testing of 4%, the
reason for these ratio is
Limited data size which allows us to increase the amount of information available for training by
allocating a larger portion of the dataset (88%) to training,
sufficient training data, which allows our model to learn from a large amount of data,
adequate validation data, which is used to tune hyperparameters like learning rates and evaluate the
model's performance during training. The testing set serves as an objective assessment of the
performance of the out-trained model, while an 8% validation set offers a reasonable sample to
compare various configurations and make wise decisions on model changes and fair performance
evaluation.
Lastly, we can obtain an accurate estimation by allocating 4% of the data to testing.performance. By
allocating 4% of the data to testing we can get a reliable estimate of how well our model generalizes
to new and unseen data.
In model training, we use Ultralytics YOLO v8 to train the dataset, open cv to detect the face to show
the features.
The result of model after training: the features that we have trained is detected correctly.

Code for model prediction process:
After we get the model from the training dataset, we need to use yolo from the Ultralytics library
to import the model. Then we can use the predict function to get the predicted frame from input
which we set the source to 0, as be use the webcam. Show as false because we don’t want to
show the YOLO part but show it as cv instead. After, we set the loop if the system detect close
eye and yawn more than 5 frames it will shown as drowsy and if the system detect open eye it
will change to awake.
Hardware connection and inference produced by model:
Firstly, flash SD card with Raspberry Pi Image then instored with Raspberry Pi 64 bit, instored a
suitable environment.


