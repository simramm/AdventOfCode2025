import math
with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()
lines = data.split("\n")
                       
p1=2
p2=12

def calcJoltage(num):
    ans=0
    for l in lines:
        s=0
        jolt=""
        for i in range(num):            
            m = max(l[s:len(l)-num+i+1])
            jolt+=str(m)
            s=l.index(m,s) +1
        ans+=int(jolt)
    return ans

print(calcJoltage(p1))
print(calcJoltage(p2))
    