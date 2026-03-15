import requests
import pandas as pd

def get_lotto(draw_no):

    url=f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"
    r=requests.get(url).json()

    return [
        r["drwtNo1"],
        r["drwtNo2"],
        r["drwtNo3"],
        r["drwtNo4"],
        r["drwtNo5"],
        r["drwtNo6"]
    ]


def update_lotto_data():

    df=pd.read_csv("data/lotto.csv")

    last_draw=df["draw"].max()

    new_nums=get_lotto(last_draw+1)

    new_row=[last_draw+1]+new_nums

    df.loc[len(df)]=new_row

    df.to_csv("data/lotto.csv",index=False)
