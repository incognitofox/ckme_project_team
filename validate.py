import requests
import json
import os
from pycountry import countries
import re
from geocode import geocode_addr
from googleAddressValidation import googleValidateAddressAPI
import time

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

key = os.getenv('GOOGLE_API_KEY')

ERROR_STRING = "ERROR: invalid address"

def address_simulator():
    adr = {
            'COMPANY': "CAPITAL CITY SYMPHONY",
            'ADDRESS2': "",
            'ADDRESS': "C/O ATLAS PERFORMING ARTS CENTER 1333 H STREET NE",
            'CITY': "WASHINGTON",
            'ZIP': "20002", 
            'ST': "DC",
            'COUNTRY': "United States"
        }
    return adr
    
def get_line_2(addr):
    line2 = ''
    for k in ['CITY', 'ST', 'ZIP','COUNTRY']:
        print(addr[k])
        if str(addr[k]).lower() == "nan" or str(addr[k]) == "":
            continue
        val = addr[k]
        if isinstance(val, float):
            val = int(val)
        val = str(val)
        if val:
            line2 += val.strip() + ', '
    return line2[:-2]

def validateWithTextsearch(addr):
    '''
    Returns a valid address given organization name and known address.
    If the address cannot be found, return an ERROR indicator

    Inputs: 
        org (string) - the organization name
        addr (string) - string representation of address to validate
    Outputs:
        result (string) - a valid address or ERROR_STRING
    '''
    ret_str = ERROR_STRING
    
    org = addr['COMPANY']
    line2 = get_line_2(addr)
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
    coords = geocode_addr(f'{org} {line2}')
    data = {"key": key, "query": f'{org} {line2}', "location": coords} 

    r = requests.get(url, params=data)
    print('success')
    print(r.text)

    try:
        ret_str = json.loads(r.text)['results'][0]['formatted_address']
    except:
        pass

    print(ret_str)
    return ret_str


def validate_addr(addr):
    '''
    Returns a valid address given organization name and known address.
    If the address cannot be found, return an ERROR indicator

    Inputs: 
        org (string) - the organization name
        addr (string) - string representation of address to validate
    Outputs:
        result (string) - a valid address or ERROR_STRING
    '''

    modified = False
    res = googleValidateAddressAPI(addr)
    time.sleep(0.01)    
    if res == ERROR_STRING:
        res = validateWithTextsearch(addr)
    time.sleep(0.01)
    return [res, modified]

