import requests
import json
import os
from pycountry import countries
import re


#takes in an address string and returns a dict of longitude and latitude
def geocode_addr(addr):
    
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

    key = os.getenv('GOOGLE_API_KEY')

    ret_dict = {}

    try: 

        url = 'https://maps.googleapis.com/maps/api/geocode/json?'

        data = {"key": key, "address": addr} 

        r = requests.get(url, params=data)
        print('success')

        res = json.loads(r.text)

        coordDict = res["results"][0]["geometry"]["location"]

        #print(res)

        ret_dict = coordDict

    except:
        print('failed')
        pass

    return ret_dict

#print(geocode_addr("1156 E 61st street 60637"))
