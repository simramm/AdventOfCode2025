with open(__file__[-5:-3]+'.in') as f: data = f.read()
#with open(__file__[-5:-3]+'-test.in') as f: data = f.read()
lines = data.split("\n")

graph ={}
for l in lines:
    k,v = l.split(": ")
    graph[k] = v.split(" ")
print(graph)

def findPaths(g, start, end):
    memo = {}
    def dfs(node):
        if node == end:
            return 1
        if node in memo:
            return memo[node]
        count = 0
        if node != "out":
            for neighbor in g[node]:
                count += dfs(neighbor)
        memo[node] = count
        return count
    return dfs(start)

print(findPaths(graph,"you","out"))
print(findPaths(graph,"svr","fft")*findPaths(graph,"fft","dac")*findPaths(graph,"dac","out"))