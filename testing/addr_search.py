import requests
import json

def format_addr_USA(name, addr):

    # key in your API key below 
    geoapify_key = ""

    payload = {}
    payload["apiKey"] = geoapify_key
    payload["name"] = addr

    response = requests.get("https://api.geoapify.com/v1/geocode/search?", params=payload)
    response_j = response.json()
    properties = response_j["features"][0]["properties"]
    
    """
    format of ret_str:
    LINE 1: NAME OF ADDRESSEE
    LINE 2: STREET ADDRESS OR POST OFFICE BOX NUMBER
    LINE 3: CITY OR TOWN NAME, OTHER PRINCIPAL SUBDIVISION (i.e., PROVINCE, STATE, COUNTY, ETC.) AND POSTAL CODE (IF KNOWN)
    (Note:  in some countries, the postal code may precede the city or town name)
    LINE 4: COUNTRY NAME (UPPERCASE LETTERS IN ENGLISH)
    """
    
    line_1 = name
    line_2 = properties["address_line2"]
    line_3 = properties["city"] + ", " +  properties["county"] + ", " +  properties["state"] + ", " +  properties["postcode"]
    line_4 = properties["country"]

    ret_str = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
    
    """
    #Use this if you want to see what your resposne looks like:
    json_object = json.dumps(response.json(), indent=4)

    with open("out3.json", "w") as outfile:
        outfile.write(json_object)
    """

    return ret_str

"""
If you did everything right you should be able to see this when running the line below:
Gerald Yeo
1156 East 61st Street, Chicago, IL 60637, United States of America
Chicago, Cook County, Illinois, 60637
United States
"""

print(format_addr_USA("Gerald Yeo", "Woodlawn Residential Commons"))

