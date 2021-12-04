f=open("inputs.txt")

numbers=[72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5
]
boards=[[list(map(int,i.split())) for i in r.split('\n')] for r in f.read().split('\n\n')]

def get_sum(board):
    sum=0
    for i in board:
        for j in i:
            if j!='X':
                sum+=j
    return sum


for n in numbers:
    for board in boards:
        for i in board:
            if n in i:
                i[i.index(n)]='X'
    
    for board in boards:
        s=[]
        for i in board:
            if all(x == 'X' for x in i):
                s.append(get_sum(board)*n)
        for i in range(len(board[0])):
                if all(l[i] is None for l in board):
                    s.append(get_sum(board)*n)
        
        if len(s):
            print(s[-1])
            break
    else:
        continue
    break



print(boards)