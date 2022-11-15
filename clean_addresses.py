import pandas as pd

def main():
    addresses = pd.read_csv("addresses.csv")
    addresses = addresses.dropna(how="all")
    addresses.to_csv("addresses.csv")

if __name__ == "__main__":
    main()
