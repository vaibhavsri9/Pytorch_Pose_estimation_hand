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

#device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = 'cpu'

transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
trainset = HandPoseDataset(root_dir = 'test/',csv_file='test/All_poses.csv',transform=transform)
train_loader = torch.utils.data.DataLoader(trainset,batch_size=1,shuffle=False,num_workers=4)
net = Net().to(device)
criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.1)
num_epochs = 2
n_total_steps = len(train_loader)

for epoch in range(2):
    for i, (images, y) in enumerate(train_loader):
        images = images.to(device)
        y = y.to(device)
        y_predicted = net(images)
        #print('y_pred size: ', y_predicted.size(), 'y size: ', y.size())
        loss = criterion(y_predicted, y)

        # Backward pass and update
        loss.backward()
        optimizer.step()

        # zero grad before new step
        optimizer.zero_grad()

        if (i + 1) % 10 == 0:
            print('Epoch ', (epoch + 1), '/', num_epochs, ' Step ', (i + 1), '/', n_total_steps, ' Loss: ', loss.item())



print('-------------------Model Performance Sample ----------------')
inputs, ys = next(iter(train_loader))
inputs = inputs.to(device)
print('True:', ys)
print('From model: ', net(inputs))
print('------------------- ---------------------------------------')

print('Evaluating on same training data ------------------')
with torch.no_grad():
    loss_array = []
    for i, (images, y) in enumerate(train_loader):
        images = images.to(device)
        y = y.to(device)
        y_predicted = net(images)
        loss = criterion(y_predicted, y)
        loss_array.append(float(loss))
    avg_loss = sum(loss_array)/len(loss_array)
print('MSE: ', avg_loss)


print('Finished Training')
