import requests
import json

def format_addr_USA(org_name, addr):

    # key in your API key below 
    geoapify_key = "89f9c261b35848d7905360fff7bcf15a"

    payload = {}
    payload["apiKey"] = geoapify_key
    payload["text"] = addr

    response = requests.get("https://api.geoapify.com/v1/geocode/search?", params=payload)
    response_j = response.json()
    properties = response_j["features"][0]["properties"]
    
    

    if properties["rank"]["confidence"]>0.8:
        #A try/except statement may be necessary here
        line_1 = org_name
        line_2 = properties["address_line2"]
        #line_3 = properties["city"] + ", " +  properties["county"] + ", " +  properties["state"] + ", " +  properties["postcode"]
        #line_4 = properties["country"]

        ret_str = line_1 + "\n" + line_2 #+ "\n" + line_3 + "\n" + line_4
        """
        format of ret_str:
        LINE 1: NAME OF ADDRESSEE
        LINE 2: STREET ADDRESS OR POST OFFICE BOX NUMBER
        LINE 3: CITY OR TOWN NAME, OTHER PRINCIPAL SUBDIVISION (i.e., PROVINCE, STATE, COUNTY, ETC.) AND POSTAL CODE (IF KNOWN)
        (Note:  in some countries, the postal code may precede the city or town name)
        LINE 4: COUNTRY NAME (UPPERCASE LETTERS IN ENGLISH)
        """
            
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

    else:
        print("Error - incorrect address")
        #the redefining of payload parameters below may be problematic
        payload = {}
        payload["name"] = org_name
        if properties["rank"]["confidence"]>0.8:

            #A try/except statement may be necessary here
            print('Searching by organization name.') 
            line_1 = org_name
            line_2 = properties["address_line1"]
            line_3 = properties["address_line2"]
            #line_4 = properties["city"] + ", " + ", " +  properties["state"] + ", " +  properties["postcode"]
            #line_5 = properties["country"]

            ret_str = line_1 + "\n" + line_2 + "\n" + line_3# + "\n" + line_4
            return ret_str
        else:
            print("No address found - start error sequence")
                    

print(format_addr_USA("Woodlawn Residential Commons", "603 South Ellis Avenue, Chicago, IL 60637"))

#Problems with this code: when address is wrong, the second if loop never runs