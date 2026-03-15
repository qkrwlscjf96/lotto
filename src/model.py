import torch
import torch.nn as nn

class LottoMLP(nn.Module):

    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(45,128),
            nn.ReLU(),
            nn.Linear(128,128),
            nn.ReLU(),
            nn.Linear(128,45),
            nn.Sigmoid()
        )

    def forward(self,x):
        return self.net(x)
