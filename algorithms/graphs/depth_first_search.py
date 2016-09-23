from collections import defaultdict
from pdb import set_trace

adj = defaultdict(set)

for line in open('hackerearth_input.txt', 'r'):
	(n1, n2) = line.strip().split()
	adj[n1].add(n2)
	adj[n2].add(n1)
	

def dfs(graph, start):
    visited, stack = set(), [start]

    while stack:
    	
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print list(dfs_paths(adj, '1', '23'))