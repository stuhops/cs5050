### Stuart Hopkins --- A02080107 --- Cs 5050
# Assignment 7
## Problem 1
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
For this problem we will utilize Dijkstra's algorithm.
We will change the algorithm to check the distance from the parent node.
This way when Dijkstra's completes, instead of returning the value, it runs again on unused nodes.
It will continue to run until all nodes have been used.

The main thing changing is distance from the parent node.
When a path is used, before it is marked black it will set its children with its distance from the parent,
  as well as all other things Dijkstra's algorithm marks it with.

This algorithm is correct because we are adding onto Dijkstra's algorithm.
All that is being done is requiring Dijkstra's algorithm to try all shortest paths
  and not just return the first one it finds.
This way it still only checks each node once but will find all shortest paths
  and return the most optimized one.

The algorithm maintains Dijkstra's time complexity of `O((m + n) log n)`.
This is because we only add a constant time element to it.
Forcing Dijkstra's algorithm to try all shortest paths does not increase the time complexity
  because the data stored on a used vertex is enough to determine shortest path.
This means that we have a higher chance of touching all nodes in the graph but does not change the worst case.
Therefore, the algorithm has a time complexity of `O((m + n) log n)`.



## Problem 2
Let G be an undirected connected graph, and each edge (u, v) has a positive weight w(u, v) > 0.
Let s and t be two vertices of G. Let π(s, t) denote a shortest path from s to t in G.
Let T be a minimum spanning tree of G.
Please answer the following questions and briefly explain why you obtain your answers.

## Part a
### Definition
Suppose we increase the weight of every edge of G by a positive value δ > 0.
Is the path π(s, t) still a shortest path from s to t?

### Solution
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



## Part b
### Definition
Suppose we increase the weight of every edge of G by a positive value δ > 0.
Is the tree T still a minimum spanning tree of G? 

### Solution
Yes, the tree T will still be a minimum spanning tree of G.
This is because Prim's algorithm uses a min-heap.
If all values in a heap are increased by the same constant,
  the relations between the values will not change.
This can be seen where `(a + δ) > (b + δ) -----> a > b`.

This is different than <i><b>a</b></i>
  because the minimum spanning tree will always have `n = m` edges.
Therefore we are comparing paths with exactly the same amount of edges.
This eliminates the case that causes <i><b>a</b></i> to fail.



## Part c
### Definition
Let e be an edge of T.
Suppose we increase the weight of e by a positive value δ > 0
  (the weights of other edges of G do not change).
Is the tree T still a minimum spanning tree of G? 

### Solution
Not necessarily.
Because Prim's algorithm uses a min-heap to determine a minimum spanning tree,
  adding to the weight of <i>e</i> may make it move places in the min-heap.
It is possible that the weight of <i>e</i> does not change enough to move in the min-heap
  but it is possible.
Because of this movement, it is possible <i>e</i> moves so far in the min-heap
  that it is no longer used in the minimum spanning tree.
This means that the tree T will not necessarily still be a minimum spanning tree of G.



## Part d
### Definition
Let e be an edge of G, but e is not an edge of T.
Suppose we increase the weight of e by a positive value δ > 0
  (the weights of other edges of G do not change).
Is the tree T still a minimum spanning tree of G? 

### Solution
Yes, prim's algorithm

Yes, the tree T will still be a minimum spanning tree of G.
This is because <i>e</i> is already great enough to not be used.
Prim's algorithm uses a min-heap.
<i>e</i> is already far enough along in the queue to not be used
  so adding δ to it will only take it further away from being used.
Because <i>e</i> will not be used either way it does not change the end result of Prim's algorithm.
Therefore, the tree T will still be a minimum spanning tree of G.




## Problem 3
### Definition
Let G be an undirected connected graph of n vertices and m edges.
Suppose each edge of G has a color of either blue or red.
Design an algorithm to find a spanning tree T of G such that T has as few red edges as possible.
Your algorithm should run in O((n + m) log n) time.

### Solution
To solve this problem we will use Prim's algorithm.
There are not currently weights on the edges so we will use the blue and red properties as weights.
To begin we will loop through all edges and assign each a weight with respect to its color.
If the edge is blue we will give it a weight of 1 and if it is red a weight of 2.
This way, Prim's algorithm will try all blue edges before it tries the red edges.

This algorithm will be correct because Prim's algorithm has been proven to be correct.
We are using Prim's algorithm to do all the computation
  and only forcing it to use the blue edges before the red edges.

The time complexity will stay the same as Prim's time complexity.
This is because adding a weight to all edges will take `O(m)` time.
Prim's time complexity is `O((n + m) log n)` so `O((n + m) log n) + O(m) = O((n + m) log n)`.
