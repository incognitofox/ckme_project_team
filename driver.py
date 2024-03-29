import pandas as pd
import json
from validate import validate_addr, ERROR_STRING
from scraper import scrape_addr

def get_valid_addr(addr):
    '''
    Returns a valid address given an organization name 
    and a k nown address.

    Inputs: 
        org (string): organization name
        addr (string): known address
    Returns (string): valid address
    '''

    result = validate_addr(addr)
    if result[0] == ERROR_STRING:
        result = [scrape_addr(addr['COMPANY']), True]
    print(result)
    return result

def get_addr_str(row):
    '''
    Helper to get full address

    Inputs:
        row (DataFrame row)
    Returns (string): concatenated address
    '''

    headers = ['ADDRESS2', 'ADDRESS', 'CITY', 'ZIP', 'ST', 'COUNTRY']
    return ','.join([str(row[header]) for header in headers])

def go(fname):
    '''
    Generates valid address and writes them to new csv file

    Inputs:
        fname (string): filename with data
    '''

    fname = fname.split(".")[0]
    df = pd.read_csv(f'./uploads/{fname}.csv')
    df = df.dropna(how="all")
    print(df)
    print(df.columns)
    df['COUNTRY'] = df['COUNTRY'].fillna("United States")
    df[['address', 'corrected']] = df.apply(lambda x: pd.Series(get_valid_addr(x)), axis=1) 
    df.to_csv(f"{fname}-cleaned.csv", index=False)


