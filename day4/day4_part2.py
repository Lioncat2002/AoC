def match_columns(matrix,index):
    return [m[index] for m in matrix]
f=open("inputs.txt")

nums=[72,99,88,8,59,61,96,92,2,70,1,32,18,10,95,33,20,31,66,43,26,24,91,44,11,15,48,90,27,29,14,68,3,50,69,74,54,4,16,55,64,12,73,80,58,83,6,87,30,41,25,39,93,60,9,81,63,75,46,19,78,51,21,28,94,7,17,42,53,13,97,98,34,76,89,23,86,52,79,85,67,84,47,22,37,65,71,49,82,40,77,36,62,0,56,45,57,38,35,5]
r=f.read()
r=r.split('\n\n')
r=[i.split('\n') for i in r]



for i in range(len(r)):
    for j in range(len(r[i])):
        r[i][j]=r[i][j].split()

boards=r
def get_sum(matrix):
    sum=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]!='X':
                sum+=int(matrix[i][j])
    return sum

def boards_matching():
    score=[]
    for n in range(len(nums)):
        for i in range(len(boards)):
            for j in range(len(boards[i])):
          
                if str(nums[n]) in boards[i][j]:
                    boards[i][j][boards[i][j].index(str(nums[n]))]='X'
                for k in range(5):
                    col=match_columns(boards[i],k)
                    if boards[i][j]==['X', 'X', 'X', 'X', 'X'] or col==['X', 'X', 'X', 'X', 'X']:
                        #score.append(get_sum(boards[i])*n)
                
                        if len(boards)==1:
                            
                            print(get_sum(boards[0])*nums[n])
                            boards.pop()
                            return 

                        else:
                            boards.pop(i)
                            return

                        
                       
    
                    
while len(boards):
    boards_matching()
f.close()