import torch
import mlflow
import mlflow.pytorch

from model import LottoMLP
from preprocess import load_dataset

def train_model():

    X,y=load_dataset()

    X=torch.tensor(X).float()
    y=torch.tensor(y).float()

    model=LottoMLP()

    optimizer=torch.optim.Adam(model.parameters(),lr=0.001)

    loss_fn=torch.nn.BCELoss()

    mlflow.set_experiment("lotto_mlp")

    with mlflow.start_run():

        for epoch in range(200):

            pred=model(X)

            loss=loss_fn(pred,y)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        mlflow.log_param("epochs",200)
        mlflow.log_metric("loss",loss.item())

        mlflow.pytorch.log_model(model,"model")
