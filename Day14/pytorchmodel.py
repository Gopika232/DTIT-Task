import torch    #type:ignore
import torch.nn as nn    #type:ignore
import torch.optim as optim   #type:ignore
from torchvision import datasets, transforms   #type:ignore
import time


# Dataset
transform = transforms.ToTensor()
train_data = datasets.MNIST(root="data",train=True,download=True,transform=transform)
test_data = datasets.MNIST(root="data",train=False,download=True,transform=transform)

train_loader = torch.utils.data.DataLoader(train_data,batch_size=64,shuffle=True)
test_loader = torch.utils.data.DataLoader(test_data,batch_size=64,shuffle=False)

# Neural Network
class NeuralNet(nn.Module):

    def __init__(self):
        super().__init__()

        self.model = nn.Sequential(nn.Flatten(),nn.Linear(784,128),nn.ReLU(),nn.Linear(128,64),nn.ReLU(),nn.Linear(64,10))

    def forward(self,x):
        return self.model(x)

model = NeuralNet()

loss_function = nn.CrossEntropyLoss()

optimizer = optim.Adam(model.parameters(),lr=0.001)

start=time.time()
# Training
for epoch in range(5):
    for images,labels in train_loader:
        output=model(images)
        loss=loss_function(output,labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print("Epoch:",epoch+1,"Loss:",loss.item())

end=time.time()

# Testing
correct=0
total=0

with torch.no_grad():
    for images,labels in test_loader:
        output=model(images)
        _,pred=torch.max(output,1)
        total += labels.size(0)
        correct += (pred==labels).sum().item()

accuracy = correct/total*100

print("\nPyTorch Results")
print("Accuracy:",accuracy)
print("Time:",end-start,"seconds")



####     OUTPUT     ####

# 100.0%
# 100.0%
# 100.0%
# 100.0%
# Epoch: 1 Loss: 0.06328825652599335
# Epoch: 2 Loss: 0.007448408752679825
# Epoch: 3 Loss: 0.3358929455280304
# Epoch: 4 Loss: 0.04983864352107048
# Epoch: 5 Loss: 0.11842896789312363

# PyTorch Results
# Accuracy: 97.05
# Time: 76.09703278541565 seconds
