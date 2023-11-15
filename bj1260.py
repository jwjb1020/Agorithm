import sys

# dfs 함수
def dfs(idx):
    global visted
    visted[idx] = True
    print(idx, end= " ")
    for next in range(1, n +1):
        if not visted[next] and graph[idx][next]:
            dfs(next)

# bfs 함수
def bfs():
    global q, visted
    while q:
        cur = q.pop(0)
        print(cur, end= " ")
        for next in range(1, n + 1):
            if not visted[next] and graph[cur][next]:
                visted[next] = True
                q.append(next)

# 0 입력 및 초기화
input = sys.stdin.readline
n,m,v = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n+1)]
visted = [False] * (n + 1)
# 1. graph 정보 입력
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(v)
print()
# 3. bfs
visted = [False] * (n + 1)
q = [v]
visted[v] = True
bfs()

