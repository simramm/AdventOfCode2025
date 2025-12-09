from shapely import Polygon,box

with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

lines = data.split("\n")
lines = [tuple(map(int, row.split(','))) for row in lines]

ans1,ans2 = 0,0
polygon = Polygon(lines)

for a,b in lines:
    for c,d in lines:
        ans1 = max(ans1,(abs(a-c)+1) * (abs(b-d)+1))
        if (a,b) == (c,d) or a == c or b == d:
            continue  
        rect = box(a,b,c,d)        
        if polygon.contains(rect):
            ans2 = max(ans2, (abs(a-c)+1) * (abs(b-d)+1))

print(ans1)
print(ans2)