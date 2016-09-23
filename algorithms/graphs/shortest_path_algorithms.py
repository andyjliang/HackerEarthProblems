from collections import defaultdict

(n, m) = (int(x) for x in raw_input().split())

graph = defaultdict(lambda: defaultdict(int))
try: 
    for _ in range(m):
        (n1, n2, w) = raw_input().split()
        graph[n1][n2] = int(w)
except EOFError:
    pass
    
    

def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it

    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]

    return d, p

(d, p) = bellman_ford(graph, '1')
print 'd', d 
print 'p', p
# print ' '.join([str(v[str(x)]) for x in range(2,n+1)])