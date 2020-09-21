from bs4 import BeautifulSoup
import requests
import sys
import re

"""
# A test to cofirm the command line argument was correctly passed in
print("URI requested: ", sys.argv[1])
"""

response = requests.get(sys.argv[1])

soup = BeautifulSoup(response.text)
for links in soup.find_all('a'):
    resp = requests.get((links.get('href')))
    if resp.headers['Content-Type'] != "application/pdf":
        continue
    else:
        print('\n')
        print('URI: ', links.get('href'))
        print('Final URI: ', resp.url)
        print('Content Length: ', resp.headers['Content-Length'], 'bytes')
        print('\n')
