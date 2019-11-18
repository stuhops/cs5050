###Stuart Hopkins --- A02080107 --- Cs 5050
#Assignment 5
##Problem 1
###Definition
The knapsack problem we discussed in class is the following. Given an integer
M and n items of sizes {a1, a2, . . . , an}, determine whether there is a subset S of the items
such that the sum of the sizes of all items in S is exactly equal to M. We assume that M
and all item sizes are positive integers.

Here we consider the following unlimited version of the problem. The input is the same as
before, except that there is an unlimited supply of each item. Specifically, we are given n
item sizes a1, a2, . . . , an, which are positive integers. The knapsack size is a positive integer
M. The goal is to find a subset S of items (to pack in the knapsack) such that the sum of the
sizes of the items in S is exactly M and each item is allowed to appear in S multiple times
(as many as you want).

For example, consider the following sizes of four items: {2, 7, 9, 3} and M = 14. Here is a
solution for the problem, i.e., use the first item once and use the fourth item four times, so
the total sum of the sizes is 2 + 3 × 4 = 14 (alternatively, you may also use the first item 4
times and the fourth item 2 times, i.e., 2 × 4 + 3 × 2 = 14).

Design an O(nM) time dynamic programming algorithm for solving this unlimited knapsack
problem. For simplicity, you only need to determine whether there exists a solution (namely,
you answer is just “yes” or “no”; if there exists a solution, you do not need to report the
actual solution subset).

###Solution
To solve this problem we will use dynamic programming.
We will be using an algorithm similar to one we used in class to solve a knapsack problem.
We will use this solution but modify it a bit.
We will store all values of the subset S so that we do not have to recalculate that value we will just already have it.

#####Subproblems
1. If `a[n]` is not in `S`, then we will find a subset of `a[1, 2, ..., n-1]` that has a sum equal to `M`.
2. If `a[n]` is in `S`, we will find a subset of `a[1, 2, ..., n-1]` that has a sum equal to `M-a[n]*c` (where `c` is a constant).

#####Dependencies

- `if j >= A[i]: f[i, j] = max( f[i-1, j], f[i, j-A[i]] )`
- `else: f[i, j] = f[i-1, j]`

#####Code
```
def unlimitedKnap(A, M):
    
    for j in range(M):
        f[0, j] = 0
        
    for i in range(len(A)):
        f[i, 0] = 1
        
    for i in range(len(A)):
        for j in range(M):
            if j >= A[i]:
                f[i, j] = max( f[i-1, j], f[i, j-A[i]] )
            else:
                f[i, j] = f[i-1, j]
                
    // Returns a 1 or 0 as a boolean value
    return f[len(A), M]
```

This algorithm is extremely close to the one from class.
The algorithm is correct because it checks every possible value to reach M.
However, it checks every possible value in an efficient, dynamic way.
Because of this efficiency the time complexity is `O(nM)`


##Problem 2
This algorithm is extremely similar to that of <i>Problem 1</i>.
The main difference is that we now have to keep track of a weight as well.
This algorithm keeps track of the value and weight of an object while useing about the same process as <i>Problem 1</i>.
The change will be in the dependency relationship.

#####Subproblems

1. If `a[n]` is not in `S`, then we will find a subset of `a[1, 2, ..., n-1]` that has a sum as close/equal to `M` with weight maximized.
2. If `a[n]` is in `S`, we will find a subset of `a[1, 2, ..., n-1]` that has a sum less than/equal to `M-a[n]` with weight maximized.
   Then add the weight of `a[n]` to the weight.
   
#####Dependencies

- `if j >= a[i]: f[i, j] = max( f[i-1, j], f[i, j-a[i]] + a[i].weight )`
- `else: f[i, j] = f[i-1, j]`

#####Sudo-Code

```
def weightedKnap(A, M):

  for j in range(M):
    f[0, j] = 0
        
  for i in range(len(A)):
    f[i, 0] = 0
        
  for i in range(len(A)):
    for j in range(M):
      if j >= A[i] and f[i-1, j] > M-a[i]:
        f[i, j].weight = max( f[i-1, j].weight, 
                              f[i, j-a[i]].weight + a[i].weight )
                              
        f[i, j] = // The sum of values of whatever has the max weight 
                  // because either will be less than or equal to M
                  
        f[i, j].subset = // subset of max plus current if second 
                         // option was max
              
      else:
        f[i, j] = f[i-1, j]
        f[i, j].weight = f[i-1, j].weight
        f[i, j].subset = f[i-1, j].subset
                
    return { f[len(A), M].subset, f[len(A), M].weight }
```

#####Correctness and Time Analysis
This algorithm is correct because it will always maximize the weight while keeping the value beneath M.
It will also return the weight and subset of the max.
This algorithm runs in `O(nM)` because there is at most `M` work done for every `n` due to dynamic programming.
   
   
##Problem 3
###Definition
In class, we studied the longest common subsequence problem. Here we consider
a similar problem, called maximum-sum common subsequence problem, as follows. Let A be
an array of n elements and B another array of m elements (they may also be considered as
two sequences of numbers). A maximum-sum common subsequence of A and B is a common
subsequence of the two arrays that has the maximum sum among all common subsequences
of the two arrays (see an example below). As in the longest common subsequence problem
studied in class, a subsequence of elements of A (or B) is not necessarily consecutive but
follows the same order as in the array. Note that some numbers in the arrays may be negative.
Design an O(nm) time dynamic programming algorithm to find the maximum-sum common
subsequence of A and B. For simplicity, you only need to return the sum of the elements in
the maximum-sum common subsequence and do not need to report the actual subsequence.
Here is an example. Suppose A = {36, −12, 40, 2, −5, 7, 3} and B = {2, 7, 36, 5, 2, 4, 3, −5, 3}.
Then, the maximum-sum common subsequence is {36, 2, 3}. Again, your algorithm only needs
to return their sum, which is 36 + 2 + 3 = 41.

###Solution
This problem is so similar to the <i>LCS (Longest Common Subsequence)</i> that we will reference the work already done for it.
The two differences between the LCS problem and the <i>MSCS (Maximum-Sum Subsequence)</i> problem is that:

1. Instead of tracking the length of the sub-sequence we are tracking the sum.
2. There may be negative values in the array.

Because of these two extra considerations we will change the following things:

#####Dependency relation
- When `A[i] == B[j]` we will perform `f(i, j) = f(i-1, j-1) + A[i]`

#####The sudo-code
- We will change the code to reflect the change in the dependency relation
```
      .
      ...
    
6|    if A[i] == B[j]:
7|        f(i, j) = f(i-1, j-1) + A[i]

      ...
      .
        
```

The algorithm is correct because we already proved it in class.
The only thing we changed was counting the sum instead of the length changing neither the correctness nor time complexity.
Because we only added a constant time element to an already `O(nm)` algorithm, it maintains the `O(nm)` time complexity.


##Problem 4
###Definition
Given an array A[1 . . . n] of n distinct numbers (i.e., no two numbers of A are
equal), design an O(n<sup>2</sup>) time dynamic programming algorithm to find a longest monotonically
increasing subsequence of A (see the definition below). Your algorithm needs to report not
only the length but also the actual longest subsequence (i.e., report all elements in
the subsequence).

Here is a formal definition of a longest monotonically increasing subsequence of A (refer to the
example given below). First of all, a subsequence of A is a subset of elements of A following
their order in A, i.e., if a number a appears in front of another number b in the subsequence,
then a is also in front of b in A. Next, a subsequence of A is monotonically increasing if for
any two numbers a and b such that a appears in front of b in the subsequence, a is smaller
than b. Finally, a longest monotonically increasing subsequence of A refers to a monotonically
increasing subsequence of A that is the longest (i.e., has the maximum number of elements)
among all monotonically increasing subsequences of A.

For example, if A = {20, 5, 14, 8, 10, 3, 12, 7, 16}, then a longest monotonically increasing
subsequence is 5, 8, 10, 12, 16. Note that the solution may not be unique, in which case you
only need to report one such longest subsequence.

###Solution
For this problem, we will have the subproblem of: 
`f(i): length of the LMIS (longest monotonically increasing Subsequence) of A[1 ... i] for any 1 < i < n`
The Dependancy relation is `f(i) = max z.subsequence.length + 1` where `z` is the subset of all values in A[1 ... i] that are less than 
A<sub>i</sub>.
Using this subproblem and dependancy relation, we only need a one dimentional array `f`.
We will start at the first element and see that there is no `z` so we record a value.
After that if there is a `z` array we chose the `z` with the max subset. 
The sudo-code for this is as follows:

```
def findLMIS(A[]):

    max = 1

    for i in range(len(A)):
        lengthArr[i] = 1
        lmisArr[i] = [ A[i] ]
        
        for j in range(i):
            if A[j] < A[i] and lengthArr[j] >= lengthArr[i]:
                lengthArr[i] = lengthArr[j] + 1
                lmisArr = lmisArr[j].add( A[i] )
                
        if lengthArr[i] > lengthArr[max]:
            max = i
    
    return { lengthArr[max], lmisArr[max] }
```

This solution is correct because it checks every possible combination that would give max length.
What this solution does not do is extra work because it uses dynamic programming to store previously calculated values.
Because of this the time complexity is O(n<sup>2</sup>).
We know this because the maximum amount of work we do for each `n` is `n`.
This is because the worst case is that every value prior to it is less than it. 
Then we would have to check if `n` values had a longer length than it did.
Because of this, the solution's time is O(n<sup>2</sup>)

