import copy
with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()
lines = data.split("\n")

R = len(lines)
C = len(lines[0])

grid=[]
for l in lines:
    row=[]
    for c in l:
        row.append(c)
    grid.append(row)

def countRolls(r,c,grid):
    count=0
    h=len(grid)-1
    l=len(grid[0])-1
    
    if r>0 and c>0 and grid[r-1][c-1] == '@':
        count+=1
    if r>0 and grid[r-1][c] == '@':
        count+=1
    if r>0 and c<l and grid[r-1][c+1] == '@':
        count+=1    
    if c>0 and grid[r][c-1] == '@':
        count+=1   
    if c<l and grid[r][c+1] == '@':
        count+=1
    if r<h and c>0 and grid[r+1][c-1] == '@':
        count+=1
    if r<h and grid[r+1][c] == '@':
        count+=1
    if r<h and c<l and grid[r+1][c+1] == '@':
        count+=1
    return count

def removeRolls(r,c,grid2):
    grid2[r][c]='.'
    return grid2
    
ans1=0
grid2=copy.deepcopy(grid)
for r in range(R):
    for c in range(C):
        if grid[r][c] == '@' and countRolls(r,c,grid)<4:
            ans1+=1
        
prev=1      
while prev>0:
    prev=0
    for r in range(R):
        for c in range(C):
            if grid2[r][c] == '@' and countRolls(r,c,grid2)<4:
                grid2=removeRolls(r,c,grid2)
                prev+=1

print(ans1)
print(sum(grid[r].count('@')-grid2[r].count('@') for r in range(R)))