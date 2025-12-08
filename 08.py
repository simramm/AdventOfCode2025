import math
with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()
test = False

boxes = [list(map(int, row.split(","))) for row in data.split("\n")]

def distance(box1, box2):
    dist = 0
    for i in range(3):
        dist += (box1[i]-box2[i])*(box1[i]-box2[i])    
    return math.sqrt(dist)

connections = []
for i in range(len(boxes)):
    for j in range(len(boxes)):
        connection = ()
        if j<=i:
            continue
        dist = distance(boxes[i], boxes[j])
        connection = (i,j,dist)
        connections.append(connection)
connections = sorted(connections, key=lambda x: x[2])

circuits = []
j=0
ans1,ans2 = 0,0
for b1,b2,dist in connections:
    j+=1
    if circuits == []:
        circuits.append([b1, b2])
    else:
        new = True
        for i,c in enumerate(circuits):
            if new:
                if b1 in c and b2 not in c:
                    for ci in circuits:
                        if b2 in ci:
                            circuits[i]=circuits[i]+(circuits.pop(circuits.index(ci)))
                            circuits[i] = list(set(circuits[i]))
                    if b2 not in circuits[i]:circuits[i].append(b2)
                    new = False
                elif b2 in c and b1 not in c:
                    for ci in circuits:
                        if b1 in ci:
                            circuits[i]=circuits[i]+(circuits.pop(circuits.index(ci)))
                            circuits[i] = list(set(circuits[i]))
                    if b1 not in circuits[i]:circuits[i].append(b1)
                    new = False
                elif b1 in c and b2 in c:
                    new = False
        if new:
            circuits.append([b1, b2])
        if (j == 10 and test) or (j == 1000 and not test):
            circuits.sort(key=lambda x:[len(x), x[0]], reverse=True)
            ans1 = len(circuits[0])*len(circuits[1])*len(circuits[2])
        if len(circuits) == 1 and len(circuits[0]) == len(boxes) and j>2:
            ans2 = boxes[b1][0]*boxes[b2][0]
            break

print(ans1)
print(ans2)



            
            