with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

*shapes, p = data.split('\n\n')
shapes = [s.count('#') for s in shapes]
areas = p.split("\n")

ans1 = 0
for l in areas:       
    area,blocks = l.split(": ")    
    x,y = list(map(int,area.split("x")))    
    nums = list(map(int,blocks.split()))    
    if x*y > sum(a*b for a,b in zip(nums,shapes)):
        ans1+=1    
print(ans1)

# Eric you devil