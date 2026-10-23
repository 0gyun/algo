import sys
from collections import deque
input = sys.stdin.readline

def dfs(node, visited):
    if visited[node]:
        return ''
    string = str(node) + ' '
    visited[node] = True
    next_nodes = edges[node]
    next_nodes.sort()
    for next_node in next_nodes:
        string = string + dfs(next_node, visited)
    return string

def bfs(node, visited, string):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        string = string + str(node) + ' '
        next_nodes = edges[node]
        next_nodes.sort()
        queue.extend(next_nodes)
    return string


num_nodes, num_edges, start_node = map(int, input().split())
edges = [[] for _ in range(num_nodes+1)]

for _ in range(num_edges):
    a, b = map(int, input().split())
    if b not in edges[a]:
        edges[a].append(b)
        edges[b].append(a)

visited = [False] * (num_nodes+1)
print(dfs(start_node, visited))
visited = [False] * (num_nodes+1)
print(bfs(start_node, visited, ''))