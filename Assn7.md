### Stuart Hopkins --- A02080107 --- Cs 5050
# Assignment 7
## Problem 1 TODO
### Definition
In class we studied algorithms for computing shortest paths.
Sometimes people are interesting in not only an arbitrary shortest path
  but also a shortest path with certain properties.
Let’s consider again the flight example given in Question 4 of Assignment 6.
Assume that saving money is very important to you
  (you need to pay tuition, to take care of your family, etc.),
  and so you want to find a shortest (i.e., cheapest) path regardless of how many edges it has.
Even in this case, there is still something you can do to “optimize” your life.
Indeed, it may be possible that there are multiple shortest paths from s to t
  (i.e., theses paths have different edges, but they have the same length).
In this case, instead of finding an arbitrary shortest path,
  it would certainly be better to find a shortest path with edges as few as possible.
This is the problem we are considering in this exercise.
But now we are considering a general graph, not necessarily a DAG.
The problem is formally defined as follows.
Given a graph G of n vertices and m edges.
Every edge (u, v) of G has a weight w(u, v) ≥ 0.
Let s and t be two vertices in G.
The length of a path in G is the sum of the weights of all edges in the path.
A shortest path from s to t is a path with the minimum length among all paths in G from s to t.
In class, we studied Dijkstra’s algorithm for computing such a shortest path.
It is possible that there are multiple different shortest paths from s to t in G
  (i.e., these paths may have different edges but their lengths are the same).
In some applications, you may want to find a shortest path
  from s to t that has edges as few as possible.
A path π in G from s to t is said to be optimal if (1) π is a shortest path from s to t,
  and (2) among all shortest paths from s to t, π has the minimum number of edges.
Refer to Figure 1 for an example.
Modify Dijkstra’s algorithm to compute an optimal path from s to t.
Your algorithm should be able to output the actual optimal path, but for simplicity,
  you only need to compute the correct predecessor information pre[v] for each vertex v of the graph.
Your algorithm should have the same time complexity as Dijkstra’s algorithm, i.e., O((m + n) log n).

### Solution
# TODO DELETE https://www.geeksforgeeks.org/dijkstras-shortest-path-with-minimum-edges/



## Problem 2 TODO
Let G be an undirected connected graph, and each edge (u, v) has a positive weight w(u, v) > 0.
Let s and t be two vertices of G. Let π(s, t) denote a shortest path from s to t in G.
Let T be a minimum spanning tree of G.
Please answer the following questions and briefly explain why you obtain your answers.

### Part a
#### Definition
Suppose we increase the weight of every edge of G by a positive value δ > 0.
Is the path π(s, t) still a shortest path from s to t?

#### Solution
Not necessarily, the path π(s, t) will not necessarily be a shortest path from s to t.
For example, if one path takes 3 edges and has a weight of 5
  and another path takes 3 edges with a weight of 6,
  if we increase all weights by δ=1 then we still take the first path the be the shortest
  with 3 edges and a weight of 8.
This is because 8 is less than 9.
However, if we take the same example with the first path having 4 edges instead of 3
  then increasing all weights by δ=2 will result in the second path being the shortest path.
This is because:

```
Before δ:
  1st: - - - - - - - - - - - - - - - current weight = 5
  2nd: - - - - - - - - - - - - - - - current weight = 6

After δ:
  1st: 4 edges * 2 = 8 extra edges + current weight = 13
  2nd: 3 edges * 2 = 6 extra edges + current weight = 12
```

We can therefore conclude that if the number of edges are the same in both paths then
  the path π(s, t) will still be a shortest path from s to t.
If the number of edges are different in both paths then
  the path π(s, t) will not necessarily be a shortest path from s to t.



### Part b TODO
#### Definition
Suppose we increase the weight of every edge of G by a positive value δ > 0.
Is the tree T still a minimum spanning tree of G? 

#### Solution
Yes


### Part c TODO
#### Definition
Let e be an edge of T.
Suppose we increase the weight of e by a positive value δ > 0
  (the weights of other edges of G do not change).
Is the tree T still a minimum spanning tree of G? 

#### Solution
Not necessarily


### Part d TODO
#### Definition
Let e be an edge of G, but e is not an edge of T.
Suppose we increase the weight of e by a positive value δ > 0
  (the weights of other edges of G do not change).
Is the tree T still a minimum spanning tree of G? 

#### Solution
No



## Problem 3 TODO
### Definition
Let G be an undirected connected graph of n vertices and m edges.
Suppose each edge of G has a color of either blue or red.
Design an algorithm to find a spanning tree T of G such that T has as few red edges as possible.
Your algorithm should run in O((n + m) log n) time.

### Solution
