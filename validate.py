import pandas as pd

def validate(df):
    pass

def go(fname):
    fname = fname.split(".")[0]
    df = pd.read_csv(f'./uploads/{fname}.csv')
    validate(df)
    df.to_csv(f"{fname}-cleaned.csv")

