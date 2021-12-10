open_brackets=['(','{','[','<']
closed_brackets=[')','}',']','>']
points={
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}
f=open('test_inputs.txt')
r=f.read().split('\n')
f.close()
point=0
stack=[]
for i in r:
    s=''
    for j in i:
       
        s+=j
        if j in open_brackets:
            stack.append(j)
        elif j in closed_brackets:
            pos = closed_brackets.index(j)
            if stack and (open_brackets[pos] == stack[-1]):
                stack.pop()
            else:
                print(s,"Error: ",j)
                point+=points[j]
                break
print(point)