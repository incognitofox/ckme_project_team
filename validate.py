ERROR_STRING = "ERROR: Invalid Address"

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
    result = ERROR_STRING
    return result
