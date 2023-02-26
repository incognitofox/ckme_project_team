#https://addressvalidation.googleapis.com/v1:validateAddress?
import requests
import json
import os
from pycountry import countries
import re
from geocode import geocode_addr
from dotenv import load_dotenv
import country_converter as coco

load_dotenv()

key = os.getenv('GOOGLE_API_KEY')

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
        val = addr[k]
        if isinstance(val, float):
            val = int(val)
        val = str(val)
        if val:
            line2 += val.strip() + ', '
    return line2[:-2]

def googleValidateAddressAPI(addr):
    print(addr)
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

    try: 
        #line2 = get_line_2(addr)

        url = f'https://addressvalidation.googleapis.com/v1:validateAddress?key={key}'

        #streetAdr = f'{org} {line2}'

        adrData = {"address": {}}

        supportedCodes = ["AU","AT","BE","BR","CA","CL","CO","DK","FI","FR","DE","HU","IE","IT","MY","MX","NL","NZ","PL","PR","SG","SI","ES","SE","CH","GB","US"]

        if ("COUNTRY" in addr and addr["COUNTRY"] != "" and addr["COUNTRY"].lower() != "nan"):
            country = [addr["COUNTRY"]]
            iso2_country_code = coco.convert(names=country, to='ISO2')
            print(iso2_country_code)
            if iso2_country_code in supportedCodes:
                adrData["address"]["regionCode"] = iso2_country_code
                print(adrData)


        if ("CITY" in addr and  addr["CITY"] != "" and addr["CITY"].lower() != "nan"):
            adrData["address"]["locality"] = addr["CITY"]
            print(adrData)


        if ("ST" in addr and not addr["ST"] != "" and addr["ST"].lower() != "nan"):
            
                adrData["address"]["administrativeArea"] = addr["ST"]
                print(adrData)
        
        if ("ZIP" in addr and addr["ZIP"] != "" and addr["ZIP"].lower() != "nan"):
            adrData["address"]["postalCode"] = addr["ZIP"]
            print(adrData)

        if ("ADDRESS" in addr and addr["ADDRESS"] != "" and addr["ADDRESS"].lower() != "nan"):
            adrData["address"]["addressLines"] = addr["ADDRESS"]
            print(adrData)

        if ("ZIP" in addr and addr["ZIP"] != "" and addr["ZIP"].lower() != "nan"):
            adrData["address"]["postalCode"] = addr["ZIP"]
            print(adrData)

        
        print(adrData)
        r = requests.post(url, json = adrData, headers={'Content-Type': 'application/json'})
        print('success')

        res = json.loads(r.text)

        print(res)

        if "addressComplete" in res["result"]["verdict"]:
            formattedAddress = res["result"]["address"]["formattedAddress"]
            ret_str = formattedAddress

        #addressComplete = res["result"]["verdict"]["addressComplete"]

        #formattedAddress = res["result"]["address"]["formattedAddress"]

        # with open("test1.json", "w") as outfile:
        #     json.dump(res, outfile, indent=4)
        
        # print(formattedAddress)

        # if addressComplete:
        #     ret_str = formattedAddress

    except:
        print('failed', addr["COMPANY"])
        pass

    return ret_str

#googleValidateAddressAPI(address_simulator())