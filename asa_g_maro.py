import requests
import random as rand
import string
from requests.packages.urllib3.exceptions import InsecureRequestWarning

spc=string.ascii_letters+string.digits
genRdm=lambda n: ''.join(rand.choice(spc) for i in range(n))

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username = 'ignw'
password = 'ignw'
payload = '''
{{
 "host": {{
  "kind": "IPv4Address",
  "value": "{}.{}.{}.{}"
 }},
 "kind": "object#NetworkObj",
 "name": "{}",
 "objectId": "{}"
}}
'''

headers = {'Content-type': 'application/json'}
while True:
     nm=genRdm(10)
     dt=payload.format(rand.randint(0,255),rand.randint(0,255),rand.randint(0,255),rand.randint(0,255),nm,nm)
     resp = requests.post(f'{url}objects/networkobjects/leGoogle', auth=(username,password), data=dt, headers=headers, verify=False)
     print(nm,resp.status_code)
     #print(resp.text)

