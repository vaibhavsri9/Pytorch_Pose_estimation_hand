#!/usr/bin/env python

import torch
import torchvision
from torchvision.transforms import transforms
import torch.optim as optim
from create_dataset_pytorch import HandPoseDataset
from neural_network_training_classifier import Net
import matplotlib.pyplot as plt
import torch.nn as nn
import numpy as np



transform = transforms.Compose(
    [transforms.ToPILImage(),transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
trainset = HandPoseDataset(root_dir = 'test/',csv_file='test/All_poses.csv',transform=transform)
trainloader = torch.utils.data.DataLoader(trainset,batch_size=4,shuffle=False,num_workers=1)
net = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.1, momentum =0.9)


for epoch in range(10):
    for i,data in enumerate(trainloader):
        inputs = data['image']
        labels = data['Pose']
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        #print statistics
        running_loss += loss.item()
        print(epoch+1,i + 1,running_loss)


print('Finished Training')
