with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

ranges, ids = data.split("\n\n")
ranges = ranges.split("\n")
ids = [int(x) for x in ids.split("\n")]

idRanges = []
for r in ranges:
    idRanges.append([int(x) for x in r.split("-")])

ans1=0
for id in ids:
    for idr in idRanges:
        if idr[0]<=id<=idr[1]:
            ans1+=1
            break
print(ans1)

idRanges.sort()
newRanges=[idRanges[0]]

for a,b in idRanges:
    overlap = 0
    for idn,cc in enumerate(newRanges):
        na,nb=cc
        if na <= a <= nb and nb <= b:
            overlap = 1
            newRanges[idn][1] = b
            break
        if na <= a < nb and nb > b:
            overlap = 1
            break
    if overlap == 0:
        newRanges.append([a,b])

ans2=0
for nr in newRanges:
    if nr!=[0,0]:
        ans2+=nr[1]-nr[0]+1
print(ans2)
