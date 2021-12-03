f=open("day3_inputs.txt")
r=f.read()
r=r.split('\n')
gamma=''
epsilon=''
l=len(r[0])
for i in range(0,l):
    ocount=0
    zcount=0
    for j in r:
        if j[i]=='1':
            ocount+=1
        else:
            zcount+=1
    if ocount>zcount:
        gamma+='1'
        epsilon+='0'
    else:
        gamma+='0'
        epsilon+='1'

print(int(gamma,2)*int(epsilon,2))
print(gamma,epsilon)
f.close()
