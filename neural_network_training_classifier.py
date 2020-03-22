import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 11)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 11)
        self.conv3 = nn.Conv2d(16, 32, 5)
        self.conv4 = nn.Conv2d(32, 32, 3)
        self.pool2 = nn.MaxPool2d(5, 5)
        self.fc1 = nn.Linear(32 * 7 * 11, 500)
        self.fc2 = nn.Linear(500, 250)
        self.fc3 = nn.Linear(250, 100)
        self.fc4 = nn.Linear(100, 50)
        self.fc5 = nn.Linear(50, 20)
        self.fc6 = nn.Linear(20, 7)

    def forward(self, x):
        # -> n, 3, 480, 640
        #print('Initial: ', x.size())
        x = self.conv1(x)           # conv1-> 6, 470, 630
        #print('conv1: ', x.size())
        x = F.elu(x)
        #print('elu: ', x.size())
        x = self.pool(x)            # pool - > 6,235,315
        #print('pool: ', x.size())
        x = self.conv2(x)           # conv -> 16, 225, 305
        #print('conv2: ', x.size())
        x = F.elu(x)
        #print('elu: ', x.size())
        x = self.pool2(x)           # pool -> 16, 45, 61
        #print('pool2: ', x.size())
        x = self.conv3(x)           # 32, 41, 57
        #print('conv3: ', x.size())
        x = self.conv4(x)           # 32, 39, 55
        #print('conv4: ', x.size())
        x = self.pool2(x)            # 32, 7, 11
        #print('pool2: ', x.size())
        x = x.view(-1, 32 * 7 * 11)  # 2464
        #print('view(-1, 32 * 4 * 11): ', x.size())
        x = self.fc1(x)
        #print('fc1: ', x.size())
        x = torch.sigmoid(x)  # -> n, 500
        #print('sigmoid: ', x.size())
        x = self.fc2(x)
        #print('fc2: ', x.size())
        x = self.fc3(x)
        #print('fc3: ', x.size())
        x = self.fc4(x)
        #print('fc4: ', x.size())
        x = self.fc5(x)
        #print('fc5: ', x.size())
        x = self.fc6(x)
        #print('fc6: ', x.size())
        return x
