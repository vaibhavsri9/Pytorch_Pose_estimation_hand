#!/usr/bin/env python

import sys
import os
import torch
from skimage import io,transform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

"""
Code to check retrieval
n = 65
pose_df = pd.read_csv('All_poses.csv',header=None)
pose_df =pose_df.T# image_names is a pandas series
img_name = pose_df.iloc[n, 0]
print('Image name: {}'.format(img_name))
pose_info = pose_df.iloc[n, 1:]
pose_info = np.asarray(pose_info)
pose_info = pose_info.astype('float').reshape(1,7)
print('Pose info shape: {}'.format(pose_info.shape))
"""
def image_show_with_pose(image):
    """
    Plot Image with Pose info
    """
    plt.imshow(image)
    # Logic for showing the Pose in the given image given parameters for arms
    plt.pause(0.01)
    return
"""
Code to check Plotting
plt.figure(img_name)
image_show_with_pose(io.imread(os.path.join('test/', img_name)))
plt.show()
"""
class HandPoseDataset(Dataset):
    """
    Hand Pose Dataset
    """
    def __init__(self, csv_file,root_dir, transform=None):
        """
        Args
        csv_file: path to csv file
        root_dir:path to where images are stored
        tranform(optional): includes various types of image transforms
        """
        self.pose_df = pd.read_csv(csv_file,header=None)
        self.pose_df = self.pose_df.T
        print(self.pose_df)
        self.root_dir = root_dir
        print(self.root_dir)
        self.transform = transform

    def __len__(self):
        return len(self.pose_df)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir,
                                self.pose_df.iloc[idx, 0])
        image = io.imread(img_name)
        pose_info = self.pose_df.iloc[idx, 1:]
        pose_info = np.asarray([pose_info])
        pose_info = pose_info.astype('float').reshape(1,7)
        sample = {'image': image, 'Pose': pose_info}
        return sample
            #if self.transform:
            #    sample = self.transform(sample)


pose_dataset = HandPoseDataset(csv_file='test/All_poses.csv',
                                    root_dir='test/')


for i in range(len(pose_dataset)):
    sample = pose_dataset[i]
    print(i, sample['image'].shape, sample['Pose'].shape)
    ax = plt.subplot(1, 4, i + 1)
    plt.tight_layout()
    ax.set_title('Sample #{}'.format(i))
    ax.axis('off')
    image_show_with_pose(sample['image'])
    if i == 3:
        plt.show()
        break
