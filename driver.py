import pandas as pd
from validate import validate_addr, ERROR_STRING
from scraper import scrape_addr

def get_valid_addr(org, addr):
    '''
    Returns a valid address given an organization name 
    and a k nown address.

    Inputs: 
        org (string): organization name
        addr (string): known address
    Returns (string): valid address
    '''

    result = validate_addr(org, addr)
    if result == ERROR_STRING:
        result = scrape_addr(org)
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
    print(df.columns)
    df['address'] = df.apply(get_addr_str, axis=1)
    df['address'] = df.apply(lambda x: get_valid_addr(x['COMPANY'], x['address']), axis=1) 
    df.to_csv(f"{fname}-cleaned.csv")


