import requests
import json
import os

key = os.environ["geoapify_key"]

ERROR_STRING = "ERROR: invalid address"

def validate_addr(org, addr):
    '''
    Returns a valid address given organization name and known address.
    If the address cannot be found, return an ERROR indicator

    Inputs: 
        org (string) - the organization name
        addr (string) - string representation of address to validate
    Outputs:
        result (string) - a valid address or ERROR_STRING
    '''
    # key in your API key below 
    geoapify_key = key
    print(org, addr)

    payload = {}
    payload["apiKey"] = geoapify_key
    payload["name"] = addr
    ret_str = ERROR_STRING
    try:
        response = requests.get("https://api.geoapify.com/v1/geocode/search?", params=payload)
        response_j = response.json()
        if response_j == {}:
            print("No addresses found")
            return "error"
        properties = response_j["features"][0]["properties"]
        
        """
        format of ret_str:
        LINE 1: NAME OF ADDRESSEE
        LINE 2: STREET ADDRESS OR POST OFFICE BOX NUMBER
        LINE 3: CITY OR TOWN NAME, OTHER PRINCIPAL SUBDIVISION (i.e., PROVINCE, STATE, COUNTY, ETC.) AND POSTAL CODE (IF KNOWN)
        (Note:  in some countries, the postal code may precede the city or town name)
        LINE 4: COUNTRY NAME (UPPERCASE LETTERS IN ENGLISH)
        """
        
        line_1 = org
        line_2 = properties["address_line2"]
        line_3 = properties["city"] + ", " +  properties["county"] + ", " +  properties["state"] + ", " +  properties["postcode"]
        line_4 = properties["country"]

        ret_str = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
    
    except:
        pass 
    #Use this if you want to see what your resposne looks like:
    """
    json_object = json.dumps(response.json(), indent=4)

    with open("out3.json", "w") as outfile:
        outfile.write(json_object)
    """

    return ret_str
