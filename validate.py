import requests
import json
import os
from pycountry import countries
import re
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('GOOGLE_API')

ERROR_STRING = "ERROR: invalid address"

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
    
    org = addr['COMPANY']

    try: 
        line2 = get_line_2(addr)

        url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'

        data = {"key": key, "query": f'{org} {line2}'} 

        r = requests.get(url, params=data)
        print('success')

        res = json.loads(r.text)['results'][0]['formatted_address']

        print(res)

        ret_str = res

    except:
        print('failed', org)
        pass

    return ret_str
