import torch     #type:ignore
import torch.nn as nn     #type:ignore


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4,8)
        self.fc2 = nn.Linear(8,3)

    def forward(self,x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = NeuralNetwork()
input_data = torch.tensor([[1.0,2.0,3.0,4.0]])
output = model(input_data)


print(output)

####  OUTPUT  ####
# tensor([[0.1235, 0.9450, 0.0388]], grad_fn=<AddmmBackward0>)