### Stuart Hopkins --- A02080107 --- Cs 5050
# Assignment 6
## Problem 1a
### Definition

Given a directed graph `G` of `n` vertices and `m` edges, let `s` be a vertex of `G`. Design a`O(m+n)` time algorithm to determine whether the following is true: there exists a path from `s` to `v` in `G` for every vertex `v` of `G`.

### Solution
To begin, we will start with the adjacencies of `s`.
We will add it to an array of visited verticies.
We will then use recursion to go through every possible adjacency using a depth first traversal.
Before we go to the vertex we will check if it is in the visited list.
This will keep us from repeatedly going to vertices.
This will allow us to visit each vertex that `s` is connected to exactly once.
That means it will give us the correct solution within set the time constraints.

```

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

## Problem 1b
### Definition

Given a directed graph `G` of `n` vertices and `m` edges, let `s` be a vertex of `G`. Design a`O(m+n)` time algorithm to determine whether the following is true:
there exists a path from `v` to `s` in `G` for every vertex `v` of `G`.

### Solution
The solution for <i>1b</i> is nearly the exact solution to problem <i>1a</i>.
The only thing we will do differently is that we will reverse the graph's adjacency list.
To do this we will go through every vertex and add its dependancies to a new adjacency list.
Once the adjacency list is reversed, we will perform the solution to <i>1a</i>.
If we can reach any `v` from `s` on a reversed graph, then on the regular graph every `v` can reach `s`.
This solution is correct because we have already proven the solution from <i>1a</i> is correct.

To perform the reversal, we will only do `O(m+n)` operations because we will only touch each node and edge a single time.
After performing the reversal we will perform the solution to <i>1a</i> which we have proven to be `O(m+n)`.
`O(m+n) + O(m+n) = 2*O(m+n) = O(m+n)`
Therefore we have a time of `O(m+n)`. 


## Problem 2
### Definition

Given an undirected graph G of n vertices and m edges, suppose s and t are two vertices in G.
We have already known that a shortest path from s to t can be found using the breadth-first-search (BFS) algorithm.
However, there might be multiple different shortest paths from s to t (e.g., see Fig. 1 as an example).
Design a O(m+n) time algorithm to compute the number of different shortest paths from s to t 
(your algorithm does not need to list all shortest paths, but only report the number).
(Hint: Modify the BFS algorithm.)

### Solution
To solve this problem we will rely heavily on the BFS algorithm as discussed in class.
All we will add is a new list that keeps track of how many paths are going through that vertex.
Because the BFS algorithm already does most of the heavy lifting we will only add three lines of code.

```

# Majority of code copied from lecture notes
# All original code has a '# new' tag on it

def modBFS(G, s):
  for vertex in G:
    color[vertex] = white
    d[vertex] = infinity
    prev[vertex] = Null

    pathCount[vertex] = 0  # new

  Q = queue()
  d[s] = 0
  color[s] = blue
  enqueue(Q, s)

  while Q is not empty:
    u = dequeue(Q)
    for each vertex in Adj[u]
      if color[vertex] == white:
        color[vertex] = blue
        d[vertex] = 1 + d[u]
        prev[vertex] = u
        enqueue(Q, vertex)
        pathCount[vertex] = pathCount[u]  # new
        
      else if color[vertex] == blue and pathCount[u] + 1 == pathCount[vertex]:  # new
        pathCount[vertex] += 1  # new

    color[u] = red

  return pathCount[t]  # new

```

This algorithm is correct because the BFS algorithm is correct.
All we add is three lines of logic to keep track of how many shortest paths go through each vertex.
Once we get to the end we return the path count at `t`.
This gives us the total number of shortest paths that get to `t`.
Keep in mind the BFS algorithm only gives us shortest paths because it quits the cycle it hits t.

The time complexity of this algorithm is `O(m + n)` because we add constant time elements to the BFS algorithm.
This does not change the time complexity so it retains BFS's `O(m + n)` time complexity.


## Problem 3
### Definition

Given a directed-acyclic-graph (DAG) G of n vertices and m edges, let s and t be two vertices of G.
There might be multiple different paths (not necessarily shortest paths) from s to t (e.g., see Fig. 2 for an example).
Design an O(m + n) time algorithm to compute the number of different paths in G from s to t.

### Solution

To do this problem we will use a Depth First Search (DFS).
We will go until we dead end, reach `t`, or hit a node that we know can reach `t`.
In the first case, we will return `0` since we did not reach `t`.
In the second case, we will return `1` because that is one path that reached `t`.
In the third case, we will return `1` plus the 'weight' of the child vertex (the number of ways you can get to `t` from the node) plus the current weight of the calling vertex.
This third case can be written as: `currWeight += recursionWeight + 1`.
In all the cases, we will set the weight of that vertex to the number we are returning (therefore returning the weight of the node).
It should be noted that we will never run into a node that has been used in our recursion tree because the graph is acyclic.

This method is correct because we will try every possible path from `s` to `t`.
Instead of trying them by brute force, we will dynamically store the weights of nodes and propigate those weights up to `s`.
It should be noted that this method would not work if the graph was cyclic but by definition the graphs we are useing are acyclic.

The time analysis for this method is `O(m+n)`.
This is because we are storing the weight of each node we have previously touched.
This means that if we visit a node that already has a calculated weight we can use that weight to determine the calling nodes weight.
That means we will never visit any node or edge more than once giving us a `O(m+n)` time.


## Problem 4
### Definition

In class we studied an algorithm for computing shortest paths in directed-acyclicgraphs (DAG) with weights on edges.
Particularly, the length of a path is defined to be the total sum of the weights of all edges in the path.
Sometimes we are not only interested in a shortest path but also care about the number of edges of the path.
For example, consider a flight graph in which each vertex is an airport and each edge represents a flight segment from one airport to another,
  and the weight of every edge represents the price of that flight segment.
If you want to fly from airport s to another one t, you are certainly interested in a shortest path from s to t to minimize the total price you have to pay.
But you probably do not want a path with too many connections (i.e., too many edges) even if it is relatively cheap.
For example, suppose you can only accept a 2 path with at most two connections (i.e., three edges).
Then, your goal is essentially to find a shortest path from s to t with the restriction that the path must have at most three edges
  (or, among all paths from s to t with at most three edges, you are looking for a shortest such path).
This is the problem we are considering in this exercise.
Let G be a DAG (directed-acyclic-graph) of n vertices and m edges.
Each edge (u, v) has a weight w(u, v) (which can be positive, zero, or negative).
Let k be a positive integer, which is given in the input.
A path in G is called a k-link path if the path has no more than k edges.
Let s and t be two vertices of G.
A k-link shortest path from s to t is defined as a k-link path from s to t that has the minimum total sum of edge weights among all k-link s-to-t paths in G.
Refer to Fig. 3 for an example.
Design an O(k(m + n)) time algorithm to compute a k-link shortest path from s to t.
For simplicity, you only need to return the length of the path and do not need to report the actual path.
(Hint: use dynamic programming)

### Solution

To perform this problem we will need to first do a topological sort.
We will use the algorithm from class to do this topological sort.
We will then cut off all values that appear before `s` because that means `s` cannot reach them.
From there we will initialize the array as all infinities.
Each row of the table will be a k value.
Each column of the table will be vertex (sorted in topological order).
If a vertex in the previous row is not infinity then we will go through its adjacency list and update the current row.
To do this we will always take the lesser value of the current weight and new weight.
Finally, once the array is completely filled out we will take the minimum value in column `t`.

```

def kShortest(G, s, t, k):
  topo = topologicalSort(G)
  # Cut off everything that appears before 's' in the sort
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
  
  # Find the shortest path calculated to t -- O(k)
  for weight in array[k][t]:
    minK = min(minK, weight)
  
  # returns Null if you cannot reach t in k moves
  return minK

```

This algorithm is correct because we check all possible paths to `t` from `s` (up to `k` away).
We compare the paths and only keep the shortest ones at that length.
We rely on the `min()` function prioritizing any number over `Null`.
The time analysis is `k * O(m + n)` because we do `O(m + n)` work for each `k`.
The reason we only do `O(m + n)` work is because in an acyclic graph we have at most `m` edges to `n` nodes.
This makes our time analysis `k * O(m + n)`.



