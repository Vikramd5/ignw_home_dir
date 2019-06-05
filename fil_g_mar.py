import random as rand
import string


spc=string.ascii_letters+string.digits

genRdm=lambda n: ''.join(rand.choice(spc) for i in range(n))


f=open('file.txt','a')
while True:
   print(f.write(genRdm(1024)))

