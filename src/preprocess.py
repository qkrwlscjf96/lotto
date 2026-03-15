import numpy as np
import pandas as pd

def encode(nums):

    v=np.zeros(45)

    for n in nums:
        v[n-1]=1

    return v


def load_dataset():

    df=pd.read_csv("data/lotto.csv")

    X=[]
    y=[]

    for i in range(len(df)-1):

        cur=df.iloc[i][1:7].values
        nxt=df.iloc[i+1][1:7].values

        X.append(encode(cur))
        y.append(encode(nxt))

    return np.array(X),np.array(y)
