from ecommercetools import seo
import pandas
import bs4
import urllib3
import certifi
import re

def scrape_addr(org):
    '''
    Given an organization name, returns the address.

    Inputs:
        org (string): organization name
    Returns (string): an address
    '''
    results = seo.get_serps(org)
    
    myurl = results['link'][0]

    pm = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    html = pm.urlopen(url=myurl, method="GET").data
    soup = bs4.BeautifulSoup(html, features="html.parser")

    # Scrape main page of website
    # addr_1 = soup.find('div', text=)

    # About
    about = soup.find('a', {'href': re.compile(r'about/')})

    # Contact
    contact = soup.find('a', {'href': re.compile(r'contact/')})
    
    # Visit
    visit = soup.find('a', {'href': re.compile(r'visit/')})

    # Address found on main page
    # if addr_1:
        # Process address and return
        # return addr_1
    # else:



    



