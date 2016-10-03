from math import sqrt

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


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

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
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


happiness = 0
graph = Graph()
n = int(raw_input())
for _ in range(n):
	(x,y,f) = map(int, raw_input().split())
	happiness += f
	graph.add_node((x,y))
for node in graph.nodes:
	for node

# best_travel_happiness = float('-inf')

# for perm in permutations(coords):
# travel_happiness = 0
perm = sorted(coords, key=lambda c: sqrt(c[0]**2+c[1]**2))
for i in range(len(perm)-1):
	happiness -= sqrt((perm[i][0]-perm[i+1][0])**2+(perm[i][1]-perm[i+1][1])**2)
# best_travel_happiness = max(best_travel_happiness, travel_happiness)
	
# print reduce(lambda c1,c2: sqrt((c2[0]-c1[0])**2+(c2[1]-c1[1])**2), coords)

print round(happiness, 6)




