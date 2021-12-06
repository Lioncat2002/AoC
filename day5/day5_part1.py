from collections import Counter
f=open("inputs.txt")
r=f.read()
r=r.split('\n')
coords=[]
for i in r:
    coords.append(i.split('->'))
pts=[]
for c in coords:
    x1=int(c[0].strip().split(',')[0])
    y1=int(c[0].strip().split(',')[1])

    x2=int(c[1].strip().split(',')[0])
    y2=int(c[1].strip().split(',')[1])
    if x1==x2 or y1==y2:
        for x in range(min(x1,x2),max(x1,x2)+1):
            for y in range(min(y1,y2),max(y1,y2)+1):
                pts.append((x,y))

print(len([x for (x,y) in Counter(pts).items() if y>1]))