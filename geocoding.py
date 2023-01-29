import requests
import json
import os
from pycountry import countries
import re

#https://maps.googleapis.com/maps/api/geocode/

#Address should be a string

def geocode_addr(addr):
    
    ret_str = "ERROR_STRING"

    try: 
        line2 = get_line_2(addr)

        url = 'https://maps.googleapis.com/maps/api/geocode/json?'

        data = {"key": key, "address": addr} 

        r = requests.get(url, params=data)
        print('success')

        res = json.loads(r.text)

        print(res)

        ret_str = res

    except:
        print('failed', org)
        pass

    return ret_str
