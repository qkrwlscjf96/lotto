import os

import mlflow.pytorch
import pandas as pd
import requests
import torch

from utils.fetch_data import encode


def predict_numbers():
    model = mlflow.pytorch.load_model("models:/lotto_mlp/latest")

    df = pd.read_csv("data/lotto.csv")
    last = df.iloc[-1][1:7].values

    x = torch.tensor([encode(last)]).float()
    probs = model(x).detach().numpy()[0]

    nums = probs.argsort()[-6:]
    nums = sorted(nums + 1)

    return nums


def send_slack(msg, slack_url=None):
    webhook_url = slack_url or os.getenv("SLACK_URL", "YOUR_WEBHOOK")
    payload = {"text": msg}

    requests.post(webhook_url, json=payload, timeout=10)
