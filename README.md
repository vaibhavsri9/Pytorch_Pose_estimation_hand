# Pytorch_Pose_estimation_hand
Pose estimation of hand using Pytorch with creation of custom dataset

# Installation
Make sure your ros environment is setup.

Install the openvr_ros package using this link :(https://github.com/sharif1093/openvr_ros)


# Usage
Use these scripts to create a .csv file for all data with image labels and their respective hand pose data.

```
image_extractor.py --bag_file <your bag file>
pose_extractor.py --bag_file <your bag file>
```
![alt text](https://github.com/vaibhavsri9/Pytorch_Pose_estimation_hand/blob/master/Image/GraspAction.png "Grasp Action Depiction")

Once you have a folder containing all the extracted images, we need to check the file which and change the location of the folder appropriately.
![alt text](https://github.com/vaibhavsri9/Pytorch_Pose_estimation_hand/blob/master/Image/All_poses.png "CSV file Format")
```
creat_dataset_pytorch.py
```

Once you have made changes to the root_dir and csv_file fields of the above file, go ahead and run the file to train the data :

```
train_neural_network_pose_estimation.py
```
Your results will appear with the MSE training loss.
![alt text](https://github.com/vaibhavsri9/Pytorch_Pose_estimation_hand/blob/master/Image/MSELoss.png "MSE Loss")
