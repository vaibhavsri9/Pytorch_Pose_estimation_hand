# Pytorch_Pose_estimation_hand
Pose estimation of hand using Pytorch with creation of custom dataset 

# Installation
Make sure your ros environment is setup. 

Install the openvr_ros package using this link :(https://github.com/vaibhavsri9/openvr_ros)

# Usage 
Use these scripts to create a .csv file for all data with image labels and their respective hand pose data.
```
image_extractor.py --bag_file <your bag file>
pose_extractor.py --bag_file <your bag file>
```

