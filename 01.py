import math
with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()
lines = data.split("\n")

p = 50
ans1,ans2 = 0,0

for l in lines:
    num = int(l[1:])    
    if l[0] == 'L':        
        if p ==0:
            ans2-=1      
        p -= num        
        while p < 0:
            ans2 +=1
            p += 100
    if l[0] == 'R':        
        p += num
        while p > 99:
            ans2 +=1
            if p ==100:
                ans2-=1
            p -= 100
    if p == 0:
        ans1+=1
        ans2+=1
print(ans1)
print(ans2)