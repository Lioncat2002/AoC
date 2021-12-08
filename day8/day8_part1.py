f=open("inputs.txt")

r=f.read().split('\n')
s=0
for i in r:
    l=i.split('|')[1]
    print(l)
    for j in l.split():
        print(j)
        if len(j) in [2,3,4,7]:
            s+=1
print(s)
f.close()