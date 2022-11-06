from pygeocoder import Geocoder
from keys import google_api
import pandas as pd
import sys

def is_valid_address(address):
    print(address)
    is_valid = False
    try:
        is_valid = Geocoder(google_api).geocode(address).valid_address()
        print(address, "worked")
    except:
        pass
    return is_valid

def main():
    filename = sys.argv[1]
    df = pd.DataFrame()
    filename = filename.split('.')[0]
    print(filename + '.csv')
    with open(filename + '.csv', 'r') as f:
        df = pd.read_csv(filename + '.csv')

    is_valid = df['address'].apply(is_valid_address)

    valid_df = df[is_valid]
    valid_df.to_csv(filename + '_cleaned.csv')

    invalid_df = df[~is_valid]
    invalid_df.to_csv(filename + '_removed.csv')

if __name__ == "__main__":
    main()
