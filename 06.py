import copy
with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

lines = [x.split() for x in data.split("\n")]
operators = lines.pop()
lines = [list(map(int, row)) for row in lines]

ans1=0
for i in range(len(lines[0])):    
    if operators[i] == '+':
        ans1+= sum(list(zip(*lines))[i])
    if operators[i] == '*':
        prod = 1
        for n in list(zip(*lines))[i]:
            prod *= n
        ans1+= prod
print(ans1)

ans2=0
l2 = data.split("\n")

nums = []
operator = ''
for i in range(len(l2[0])):
    column =""    
    for c in l2:    
        if c[i] == '+' or c[i] == '*':
            operator = c[i]
        else:
            column+=c[i]
    if column.strip() != "":
        nums.append(int(column))
    if column.strip() == "" or i == len(l2[0])-1:
        if operator == '+':
            ans2 += sum(int(x) for x in nums)
        if operator == '*':
            prod = 1
            for x in nums:
                prod *= int(x)
            ans2 += prod
        nums = []

print(ans2)
                
            
            
