import requests
import argparse
import json
# from dynapork import config

with open('dynapork.conf') as json_file:
  config = json.load(json_file)

# Get external ip.. The site below is pretty fast and simple. Of course there are 
# other alternatives. You're free to try something else.
external_ip = requests.get("https://api64.ipify.org?format=json").json()['ip']

# print(external_ip)
print("ⓓ ⓨ ⓝ ⓐ ⓟ 🐷ⓡ ⓚ")
parser = argparse.ArgumentParser()
parser.add_argument('-d','--daemon',action='store_true',help='run as a daemon')
parser.add_argument('-f','--force',default=external_ip,metavar='IP_ADDRESS',help='force ip address')
parser.add_argument('-n','--name',metavar='DOMAIN',help='run only for the DOMAIN')
parser.add_argument('-s','--sub',metavar='SUBDOMAIN',help='run only for the SUBDOMAIN')
parser.add_argument('-V','--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

sites = requests.post("https://porkbun.com/api/json/v3/dns/retrieve/example.site",
  json={
        "secretapikey": config['secretapikey'],
        "apikey": config['apikey'],
  })

def site_id(name):
    for key in sites.json()['records']:
        if name.lower() == key['name'].lower():
            return key['id']

print(site_id('www.example.site'))