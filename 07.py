with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()

lines_raw = [list(x) for x in data.replace("S","1").split("\n")]
lines = []

for l,line in enumerate(lines_raw): # remove empty lines
    if l>0 and line.count("^")==0:
        continue
    else:
        lines.append(line)

for l,line in enumerate(lines): # convert to numbers
    for i,c in enumerate(line):
        if c ==".":
            lines[l][i] = 0
        elif c =="1":
            lines[l][i] = 1
            
ans1,ans2 = 0,0
for l,line in enumerate(lines):
    for i,c in enumerate(line):
        if l==0:
            continue
        if c !="^" and lines[l-1][i] != "^" and lines[l-1][i]>0:
            lines[l][i] += lines[l-1][i]
        elif c =="^" and lines[l-1][i] >0:
            lines[l][i-1] += lines[l-1][i] 
            lines[l][i+1] += lines[l-1][i]
            ans1+=1
print(ans1)

for x in lines[-1]:
    if x !="^":
        ans2+=x
print(ans2)
                