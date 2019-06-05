import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


url = 'https://10.0.0.5/restconf'
username = 'ignw'
password = 'ignw'
headers = {'content-type': 'application/yang-data+json', 'accept': 'application/yang-data+json'}
endpoint='/data/Cisco-IOS-XE-native:native/interface/'
data={
'Cisco-IOS-XE-native:Loopback':{
'name':2,
'description':'Using restConf',
'ip':{
   'address':{'primary':{'address':'172.16.1.2','mask':'255.255.255.255'}}
}
}
}

resp = requests.post(f'{url}/{endpoint}', auth=(username,password), headers = headers,data=json.dumps(data),verify= False)
print(resp.status_code)
print(resp.text)
