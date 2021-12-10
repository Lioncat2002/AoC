open_brackets=['(','{','[','<']
closed_brackets=[')','}',']','>']
points={
    '(':1,
    '[':2,
    '{':3,
    '<':4
}
f=open('inputs.txt')
r=f.read().split('\n')
f.close()

scores=[]
for i in r:
    s=''
    stack=[]
    point=0
    for j in i:
       
        s+=j
        if j in open_brackets:
            stack.append(j)
        elif j in closed_brackets:
            pos = closed_brackets.index(j)
            if stack and (open_brackets[pos] == stack[-1]):
                stack.pop()
                print(s)
    for k in range(len(stack)-1,-1,-1):
        point=point*5+points[stack[k]]
        print(point)
    scores.append(point)
    print(stack,scores)
scores.sort()
from statistics import median
print(scores)
print(scores[int(median(range(0,len(scores))))])
