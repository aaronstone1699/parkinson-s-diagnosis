# parkinson-s-diagnosis

Parkinson’s disease is a neurological disorder with more than 6 million people worldwide
suffering from it.It is commonly diagnosed using clinical assessments and progression scale
which usually depends on the medical practitioner’s expertise ,and accuracy varies greatly
between various examiners which also takes a long time to accurately diagnose.This paper
proposes to develop a computer aided diagnostic method to diagnose PD patients using MRI
images of the brain ,thus reducing cross examiner variability and the time required to accurately
differentiate between PD and Control subjects.

## Image Enhancement:
The images present in the dataset have varying brightness,colour and noise ,to remove these
unwanted elements from our training and testing images ,we apply image filtering operations
and histogram equalisation for contrast enhancement ,for better identifiable features.
In our study the image enhancement pipeline consists of converting the RGB image to YUV
colour space, for accurate colour and features ,then the Luminance channel is filtered using
gaussian blur to reduce the noise and pixelation,then contrast limited adaptive histogram
equalisation is applied on the Y channel to improve the local image contrast while keeping the
noise low.
finally the the 3 channels Y,U and V are merged and converted to RGB colorspace for further
processing

 note: to use the image enhancement technique please go to either parkisinsons_first_stage.ipynb or parkinsons_final_stage.ipynb and in the calling of the dataset functio change th eparameter enhance to true
 
 ## First stage :
 
### region of interest extraction

The images that the MRI dataset provides contain multiple slides of the brain and different
studies might use different thickness of the slides . the most influencing region of the brain in the
detection of Parkinson’s is the SN region , we localize the sn region to classify between pd
and no pd ,to improve the accuracy of the localization we separate the images containing the SN
region ,In this study we use a custom CNN for automatically differentiating SN in image and no
sn in image


 ## Final stage stage :
 
### classification

final stage of the process is the classification of the Substantia nigra region as belonging to a
Parkinson’s patient or a control. A modified version of the Alex Net with activation at the last
fully connected layer having a sigmoid activation for the 2 classes and 6 convolutional layers ,to
improve the feature vectors as compared to manually selected vectors, which are prone to
changes in orientation and intensity.
An image of the Substantia Nigra region in the MRI of size 512x512 is taken as an input by the
convolutional neural network which can extract the features from the image autonomously for
the classification of the image into the classes as PD or control.
