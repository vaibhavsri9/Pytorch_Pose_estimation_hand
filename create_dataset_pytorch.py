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
from PIL import Image

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
        #print(self.pose_df)
        self.root_dir = root_dir
        #print(self.root_dir)
        self.transform = transform

    def __len__(self):
        return len(self.pose_df)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        img_name = os.path.join(self.root_dir,
                                self.pose_df.iloc[idx, 0])
        image = Image.open(img_name)
        pose_info = self.pose_df.iloc[idx, 1:]
        pose_info = np.asarray([pose_info])
        pose_info = pose_info.astype('float').reshape(1, 7)
        pose_info = np.squeeze(pose_info)

        if self.transform:
            image= self.transform(image)
            pose_info = torch.from_numpy(pose_info).float()
        sample = image, pose_info

        return sample


"""

pose_dataset = HandPoseDataset(csv_file='test/All_poses.csv',
                                    root_dir='test/')
sample = pose_dataset[3]
print(sample)
"""

"""
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

# Writing dataloader
#dataloader =  DataLoader(pose_dataset,batch_size = 4,shuffle = True, num_workers =4)
"""

"""
dataloader =  DataLoader(pose_dataset,batch_size = 4,shuffle = True, num_workers =1)
for i_batch,sample_batched in enumerate(dataloader):
    print(i_batch, sample_batched['image'])
    if i_batch == 3:
        break
"""
