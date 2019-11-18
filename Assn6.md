###Stuart Hopkins --- A02080107 --- Cs 5050
#Assignment 5
##Problem 1a
###Definition
1. Given a directed graph `G` of `n` vertices and `m` edges, let `s` be a vertex of `G`.

a. Design a`O(m+n)` time algorithm to determine whether the following is true: there exists a path from `s` to `v` in `G` for every vertex `v` of `G`.

###Solution
To begin, we will start with the adjacencies of `s`.
We will add it to an array of visited verticies.
We will then use recursion to go through every possible adjacency using a depth first traversal.
Before we go to the vertex we will check if it is in the visited list.
This will keep us from repeatedly going to vertices.
This will allow us to visit each vertex that `s` is connected to exactly once.
That means it will give us the correct solution within set the time constraints.

```python

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

```

This solution is correct as stated before.
We check all possible adjacencies while still keeping down on time.
The time analysis is `O(m + n)` because we are touching every vertex and every edge in the graph once in the worst case.
This means we must include `m` and `n`.






