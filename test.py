def isPath(s, n, adjacencyList):
  visited = {s}

  for vertex in adjacencyList[s]:
    if vertex not in visited:
      visited.add(isPath(vertex, adjacencyList))

  if len(visited) == n:
    return True
  else:
    return False


def isPath(s, adjacencyList):
  visited = {s}

  for vertex in adjacencyList[s]:
    if vertex not in visited:
      visited.add(isPath(vertex, adjacencyList, visited))

  return visited


def kShortest(G, s, t, k):
  topo = topologicalSort(G)
  array = [k][topo]

  # Initialize the first row (zero indexed) -- O(n + m)
  for adjacency in G.adjacencyList[s]:
    # Assumes that the min function says any number is smaller than Null
    array[0][adjacency] = min(array[0][adjacency], adjacency.edgeWeight)

  # Calculate the array -- k*O(m + n)
  for index in k:
    for vertex in topo:
      if vertex is not Null:
        for adjacency in G.adjacencyList[vertex]:
          array[index + 1][adjacency] = min(array[index + 1][adjacency],
                                            G.adjacencyList[adjacency] + vertex)
  
  for weight in array[k][t]:
    minK = min(minK, weight)
  
  return minK



