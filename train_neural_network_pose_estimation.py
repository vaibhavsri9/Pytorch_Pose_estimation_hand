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
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])


trainset = HandPoseDataset(root_dir = 'test/',csv_file='test/All_poses.csv,transform = transform)
trainloader = torch.utils.data.DataLoader(trainset,batch_size=4,shuffle=True,num_workers=1)
net = Net()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.1, momentum =0.9)

for epoch in range(2):

    running_loss = 0.0
    for i,data in enumerate(trainloader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(ouputs, labels)
        loss.backward()
        optimizer.step()

        #print statistics
        runnin_loss += loss.item()


print('Finished Training')
