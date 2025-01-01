f1=open('SELF.txt','r')
f2=open('empt2.txt','w')
cont=f1.readlines()
for i in range(0,len(cont)):
    if(i%2==0):
        f2.write(cont[i])
    else:
        pass
f2.close()
