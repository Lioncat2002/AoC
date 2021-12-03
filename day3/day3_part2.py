f=open("day3_inputs.txt")
r=f.read()
r=r.split('\n')
gamma=''
epsilon=''
l=len(r[0])
chosenbit1=[]
k=r
for i in range(0,l):
    ocount=0
    zcount=0
    for j in r:
        if j[i]=='1':
            ocount+=1
        else:
            zcount+=1
    if ocount>=zcount:
        for j in r:
            if j[i]=='1':
                chosenbit1.append(j)
    else:
        for j in r:
            if j[i]=='0':
                chosenbit1.append(j)
    r=chosenbit1
    chosenbit1=[]
    if len(r)==1:
        break
oxygen=r[0]
r=k
chosenbit0=[]
for i in range(0,l):
    ocount=0
    zcount=0
    for j in r:
        if j[i]=='1':
            ocount+=1
        else:
            zcount+=1
    if ocount<zcount:
        for j in r:
            if j[i]=='1':
                chosenbit0.append(j)
    else:
        for j in r:
            if j[i]=='0':
                chosenbit0.append(j)
    r=chosenbit0
    chosenbit0=[]

    if len(r)==1:
        break
co2=r[0]
print(int(oxygen,2)*int(co2,2))
f.close()
