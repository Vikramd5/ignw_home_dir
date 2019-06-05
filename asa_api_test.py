import requests

url='https://10.0.0.8/api/'
username=password='ignw'

rs=requests.get(f'{url}interfaces/physical', auth=(username, password),verify=False)
data=rs.json()
for i in data['items']:
    if 'ip' in i['ipAddress']:
        print(i['hardwareID'],i['ipAddress']['ip']['value'])
    else:
        print(i['hardwareID'])
