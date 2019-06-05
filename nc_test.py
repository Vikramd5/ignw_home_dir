from ncclient import manager

m=manager.connect(host='10.0.0.5',port=830,username='ignw',password='ignw',device_params={'name':'csr'})

#for cap in m.server_capabilities:
#    print(cap)

c=m.get_config(source='running')

print(c)

