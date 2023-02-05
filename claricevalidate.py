import requests
import json
import os
from pycountry import countries
import re

key = os.environ["GOOGLE_API"]

ERROR_STRING = "ERROR: invalid address"

"""
def get_line_2(addr):
    line2 = ''
    for k in ['CITY', 'ST', 'ZIP','COUNTRY']:
        val = addr[k]
        if isinstance(val, float):
            val = int(val)
        val = str(val)
        if val:
            line2 += val.strip() + ', '
    return line2[:-2]
"""

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
    ret_str = ERROR_STRING
    
    #org = addr['COMPANY']

    #try: 
        #line2 = get_line_2(addr)

    address = {
        "regionCode": "US",
        "locality": "Mountain View",
        "administrativeArea": "CA",
        "postalCode": "94043",
        "addressLines": ["1600 Amphitheatre Pkwy"]
        }

    url = 'https://addressvalidation.googleapis.com/v1:validateAddress?'

    data = {"key": key, "address": address, "enableUspsCass": True} 

    r = requests.get(url, params=data)
    print('success')

    #res = json.loads(r.text)#['results'][0]['formatted_address']

    print(r)
    print(r.text)
    #ret_str = res

    # except:
    #     print('failed', addr)
    #     pass

    return ret_str

validate_addr("test")