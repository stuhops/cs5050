###Stuart Hopkins --- A02080107 --- Cs 5050
#Assignment 4
##Problem 1
The `count` will start at zero.
We will start by comparing the value `x` to the root. 
If the count is greater than `k` we will return `True`.
If `x` is greater than or equal to the root we will add one to the count and check it's children recursively.
If `x` is less than the root we will return `False`.
If any of the nodes children returns `True` we will return `True` for everything.

This method will give us the correct outcome because if `count` elapses `k` then we know there are at least `k` values less than `x`.
If we run out of paths to check before `count` elapses `k` then that means there are only `count` values less than `x`.
This means if you got rid of the return statements the algorithm would run until `count` equaled the number of values less than `x`.
Note that this does not find the k<sub>th</sub> value. 

Because of the way this algorithm checks through values, the time will be `O(k)` time. 
If there is a value greater than `x` we will not check any of it's kids so this is how we keep the time complexity down.


##Problem 2
To perform this problem we will use the properties of the binary search tree.
We will perform a standard search for the element `x` while also keeping track of the last time we went left.
If we find the element then we will return `x` (the value we are searching for).
If we do not find the element we will return the value of the last node we went left at.
If we have not gone left yet and reach a `Null` element then `x` is larger than the max element in the tree.
In this case we will return `Null`.

```
def successor(x, node, lastLeft) {
    if node == null
        // NOTE: lastLeft.key is null if lastLeft has not been set yet.
        return lastLeft.key  
        
    else if node.key == x
        return x
    
    else if node.key < x
        return successor(x, node.left, node)
        
    else
        return successor(x, node.right, lastLeft)
        
}
```

This algorithm is correct because the successor of any element is the last time you went left in the tree.
This algorithm takes that into account and uses the basic principles of a BST to find the element's successor.
If we never go left in a tree and reach a `Null` node then we know there is no value larger than `x`.
This also leads to the correct answer of `Null`.

This algorithm takes `O(h)` time because we are only taking one path down the tree.
In the worst case scenario we will reach a bottom leaf which is `h` deep.
This means that in the worst case it is `O(h)` time.


##Problem 3
To solve this problem we will add an extra variable to each node `size` which holds the amount of children it has plus itself.
This extra variable will allow us to perform a search for `rank` in the correct time.
This means each node will have the values: `left`, `right`, `key`, and `size`.
Upon insertion the `size` will percolate up retaining the time (see below for more explanation).
The sudo code for the `rank` algorithm is as follows:


```
// NOTE: if `v.left` or `v.right` are equal to `NULL` 
// then their size will be equal to zero.

def rank(x, T) {
    v = T.root
    count = 0
    
    while v != null {
        if x == v.key 
            return count + v.left.size + 1
        else if x > v.key
            count += v.left.size + 1
        else
            v = v.left
    }
    
    return count + 1
}
```

This algorithm is correct because it takes into consideration all cases.
If the value `x` is not in the tree then the algorithm will still return the correct value.
If the value `x` is in the tree then the algorithm will use the predetermined `size` values to return it's rank.
This algorithm is correct as long as the `size` variables are correct.

This algorithm will perform in `O(h)` time for all functions <i>insert, delete, search, and rank</i>.
<i>Rank</i> because we are only following a single path down the tree and performing constant time each level.
For <i>search, insert, and delete</i> we get `O(h)` time because of the theorem discussed in class.
As stated in the theorem, the time does not change as long as the values for each node only depend on the value of `node.left` and `node.right`.
This is true for all cases for the new `size` variable and therefore time is preserved.


##Problem 4
To begin this problem, we will do a search operation for the `min`.
Once we find the `min` we will start an <i>in order traversal</i> of the tree.
Note that this means if the `min` is not in the tree then we only do an <i> in order traversal</i> of the elements greater than it.
We will perform the <i>in order traversal</i> only until we reach the max.
The sudo code is as follows:

```
def range(node, min, max) {
    if node == null
        return []
        
    else if node.key < min
        return []
        
    else {
        array = range( In order traversal to the left )
        
        if node.key > max 
            return arr
            
        // Add node.value to the array if within the range as part of the traversal
    
        array += range( In order traversal to the right )
        
        return array
    }
}
```

This is correct because it performs an in order traversal between the min and max values.
It does this by starting the in order traversal only once the min is hit.
An in order traversal returns a sorted list.
It always checks all the nodes to left before adding itself or returning because it is larger than the max.
It doesn't add any values that are larger than the max because it returns before it adds the value.

The time complexity is `O(h+k)` because depending on how wide the range is depends on the time.
The algorithm may search to the bottom of the tree giving it `h` time and then takes `k` time for the in order traversal.
If the range includes the entire tree then the time complexity will be `O(k)`.
If the range includes just one or two nodes the time complexity may be `O(h)`.
This means that the time complexity is `O(h+k)`.


##Problem 5
To change the time complexity from <i>Problem 4</i> to `O(h)` we will store the `size` of the node.
We will define the `size` of a node by it's value plus the value of it's children combined.
The `range-sum` algorithm finds the sum by first finding the first node where `min <= node.key <= max`.
Secondly, the algorithm finds the amount of `size` values in the left subtree that is not within the range.
Third, the amount of `size` values in the right subtree that are not within the range.
Lastly, return the split nodes size minus the second and third step results. 
The pseudo code for the `range-sum` is as follows:

```
def range-sum(xL, xR, T) {
    split = findSplit(xL, xR, T.root, T)
    minOff = findMin(xL, split)
    maxOff = findMax(xR, split)
    
    return split.size - minOff - maxOff
}
```

```
def findSplit(xL, xR, node, T) {
    if xL <= node.key <= xR or node == null
        return node
        
    else if xL > Node.size
        return findSplit(xL, xR, node.right, T)
        
     else 
        return findSplit(xL, xR, node.left, T)
        
}
```

```
// NOTE: the size of a null node is 0

def minOff(min, node, T) {
    if node.key == null
        return 0
        
    else if node.key == min
        return node.left.size

    else if min < node.key
        return minOff(min, node.left)
        
    else
        return minOff(min, node.right) + node.key + node.left.size
        
}
```

```
// NOTE: the size of a null node is 0

def maxOff(max, node, T) {
    if node.key == null
        return 0
        
    else if node.key == max
        return node.right.size

    else if max > node.key
        return maxOff(max, node.right)
        
    else
        return maxOff(max, node.left) + node.key + node.right.size
        
}
```

This algorithm is correct because if you take the `size` of the entire tree and subtract off the `size` of all the nodes not in the range you 
will end up with the correct answer.
By splitting the problem up into helper functions it is easy to see that this is what is happening.

The time complexity for the algorithm is `O(h)` time for <i>insert, delete, search, and range-sum</i> functions. 
For the <i>insert, delete, and search</i> functions the time complexity stays the same because of the theorem from class.
The `size` variable only depends on the child nodes which meets the requirements of the theorem. 
For the <i>range-sum</i> algorithm it is `O(h)` because the time equals `2h` in the worst case. 
Take the polynomial out and you have `O(h)`.
