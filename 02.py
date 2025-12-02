with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

def isInvalid1(num,l):
    if l %2 !=0:
        return False    
    if num[l//2:] != num[:l//2]:
        return False        
    return True

def isInvalid2(num,l):
    for i in range(1, l//2+1):
        if l%i ==0 and num[i:] == num[:-i]:
            return True   
    return False

ranges = data.split(",")
ans1,ans2=0,0
for r in ranges:    
    a,b = map(int, r.split("-"))
    for x in range(a, b+1):        
        if isInvalid1(str(x),len(str(x))):
            ans1+=x
        if isInvalid2(str(x),len(str(x))):
            ans2+=x

print(ans1)
print(ans2)