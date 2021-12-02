f=open("day2_inputs.txt")
r=f.read()
r=r.split("\n")
pos=[0,0]
aim=0
for i in r:
    l=i.split()
    if l[0]=='forward':
        pos[0]+=int(l[1])
        pos[1]+=int(l[1])*aim
    if l[0]=='down':
        aim+=int(l[1])
    if l[0]=='up':
        aim-=int(l[1])

print(pos[0]*pos[1])

f.close()