from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

(n, m) = (int(x) for x in raw_input().split())

graph = Graph()
try: 
    for _ in range(m):
        (n1, n2, w) = raw_input().split()
        graph.add_node(n1)
        graph.add_node(n2)
        graph.add_edge(n1, n2, int(w))
        graph.add_edge(n2, n1, int(w))
except EOFError:
    pass
    

def dijsktra(graph, initial):
  visited = {initial: 0}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight

  return visited

v = dijsktra(graph, '1')
print ' '.join([str(v[str(x)]) for x in range(2,n+1)])