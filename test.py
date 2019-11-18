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

