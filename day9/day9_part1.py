f=open("inputs.txt")

r=f.read().split('\n')
f.close()

a=[[10]*(len(r[0])+2)]

for i in r:
    a.append([10]+list(i)+[10])
a.append([10]*(len(r[0])+2))    
s=0
for i in range(len(a)):
    a[i]=[int(j) for j in a[i]]
    print(a[i])

for i in range(1,len(a)-1):
    for j in range(1,len(a[0])-1):
        if a[i][j]<a[i-1][j] and a[i][j]<a[i][j+1] and a[i][j]<a[i+1][j] and a[i][j]<a[i][j-1]:
                s+=a[i][j]+1         
print(s)

        


