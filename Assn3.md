###Stuart Hopkins --- A02080107 --- Cs 5050
#Assignment 3
##Problem 1
The basic algorithm for this problem is to do a binary search on the array.
Once the array is split in half we will check to see if the item is greater than the index to the left and/or greater than the index to it's 
right.
If it is less than the index to it's left we know that it is descending so we will chose search the left array.
If it is greater than the index to it's left and less than the index to it's right do a binary search on the right side.
Finally, if it is greater than the index to it's left and greater than the index to it's right than it is the "peak entry".

```
def binarySearch (array, index, minBound, maxBound):
    if(array[index] < array[index-1]) {
      return binarySearch(array, <middle of minBound and index-1>, minBound, index-1);
    }
    else if(array[index] < array[index + 1]) {
      return binarySearch(array, <middle of index+1 and maxBound>, index+1, maxBound);
    }    
    else {
      return index;
    }
```

This algorithm is correct because the "peak entry" will never be on an end.
This means that the only possible scenario is for the "peak entry" to be surrounded by a two numbers less than itself. 

Because we are dividing the problem size in half and doing constant time each call, the problem is `O(n)`.

##Problem 2
'In the SELECTION algorithm we studied in class, the input numbers are divided into groups of five. 
Will the algorithm still work in linear time if they are divided into groups of seven? 
Please justify your answer.'

As stated in the problem, we studied the SELECTION algorithm in class.
While studying the algorithm in class we derived the formula: 

<sup>n</sup>&frasl;<sub>5</sub> &times; <sup>1</sup>&frasl;<sub>2</sub> &times; 3 = <sup>3</sup>&frasl;<sub>10</sub> &times; n

Using this formula we proved that selection using groups of five was possible.
To prove that selection is possible useing seven groups is also possible by modifying the formula to be:

<sup>n</sup>&frasl;<sub>7</sub> &times; <sup>1</sup>&frasl;<sub>2</sub> &times; 3 = <sup>3</sup>&frasl;<sub>14</sub> &times; n

This means that we must have at least <sup>3</sup>&frasl;<sub>14</sub> &times; n elements of A<sub>n</sub> >= y.
At most, we can have 

n - <sup>3</sup>&frasl;<sub>14</sub> &times; n = <sup>11</sup>&frasl;<sub>14</sub> &times; n 

elements in A<sub>n</sub> <= y. 
If this is the case then the selection algorithm will work with groups of 7.
This means the time function is 

T(n) = T(<sup>11</sup>&frasl;<sub>14</sub> &times; n) + T(<sup>n</sup>&frasl;<sub>7</sub>) + n

We will guess that T(n) = O(n).
We will then assume that 

T(n) <= c &times; n

T(<sup>11</sup>&frasl;<sub>14</sub> &times; n) <= c &times; <sup>11</sup>&frasl;<sub>14</sub> &times; n

T(<sup>n</sup>&frasl;<sub>5</sub>) <= c &times; <sup>n</sup>&frasl;<sub>7</sub>

This means that if T(n) = O(n) then T(n) <= c &times; n. 
That looks like this:

c &times; n >= T(<sup>11</sup>&frasl;<sub>14</sub> &times; n) + T(<sup>n</sup>&frasl;<sub>7</sub>) + n 

c &times; n >= c &times; <sup>11</sup>&frasl;<sub>14</sub> &times; n + c &times; <sup>n</sup>&frasl;<sub>7</sub> + n

c &times; n >= c &times; <sup>13</sup>&frasl;<sub>14</sub> &times; n + n

c >= c &times; <sup>13</sup>&frasl;<sub>14</sub> + 1

If we substitute 20 in for c then we get 20 >= 19.57 which is true!
Therefore, we can say that groups of seven do work for the selection algorithm.
We can also say that the selection algorithm using groups of seven is `O(n)` time.

##Problem 3
###Problem 3 part a
For this problem we must find a `O(nlogn)` algorithm.
To do this we will first sort the array.
Secondly, we will do a binary search of the array checking each pivot in the blackbox.
If the item is a feasible value we will store it as the max feasible value.
We do not need to compare the feasible values each time because if a new feasible value is found it will always be larger than the previous 
based on a binary search algorithm.
Once the algorithm hits the base case `sub-array.length = 1` then the program will return the stored feasible value (which is the largest one.

The algorithm is correct because with the array sorted we know that if we choose the right array in the binary search we are always testing 
larger numbers than the already stored maxFeasible. 
This way we always get the max feasible value possible.

The algorithm runs in `O(nlogn)` time because it takes `nlogn` time to sort the array and `logn` time to find the value.
The `nlogn` will dominate so the time complexity is `O(nlogn)`.

###Problem 3 part b
For this problem we must find a `O(n)` time algorithm.
To do this we will use the selection algorithm and modify it a bit.
Each recursive call, we will find the median using the selection algorithm.
We will test the median in the blackbox.
Depending on if it is feasible we will test the left or the right side of the median (selection gives us the two halves that it divides).
We will then call the function recursively on whichever half is determined the correct way to go based off of whether the pivot is feasible or
not.

```
foo (arr) {
    if (arr.length == 1) 
        return arr[0];
    
    {leftArray, pivot, rightArray} = selection(k=n/2, array=arr);
    feasible = blackbox(pivot);
    
    if(feasible == true) 
        return max(pivot, foo(rightArray)); 
    else
        return foo(leftArray);
}
```

This is a correct algorithm because we are still "sorting" in a way. 
We get a median using selection and use that to narrow our field of vision to only the numbers higher or lower than it.
This way we still test the possibilities but in a smart way.

The algorithm is `O(n)`. This is because the algorithm runs in `T(n) = T(n/2) + n`. 
This recursive time equation is equal to `O(n)`.

##Problem 4
###Problem 4 part a
For this part a `O(nlogn)` time algorithm is required.
This algorithm is very simple. 
To achieve a `O(nlogn)` time algorithm we will first sort the data using merge sort.
From this merge sort we will then find each k<sub>value</sub> by using the index because the array is in order.
So the k<sub>2</sub> value will be found using array[k<sub>2</sub> - 1] (assuming the index starts at zero).

```
getKValues(array, kArray) {
    mergeSort(array);

    for(k in kArray) {
        kValues.add(array[k - 1]);
    }

    return kValues;
}
```
This solution is correct because the k<sup>th</sup> value is the k<sup>th</sup> smallest value.
This means if you sort the array you can find the k<sup>th</sup> smallest value in constant time (once the array is sorted).

This solution takes `O(nlogn)` time because once the array is sorted it takes `m` time to get all the k<sub>values</sub>.
To sort the array is `nlogn` time so `O(nlogn)`.

###Problem 4 part b
For this part `O(nm)` time is required.
To do this we will do the selection algorithm `m` times.

```
getKValues(array, kArray) {
    for(k in kArray) {
        kValues.add(selection(k, array));
    }
}
```

This solution is correct because the selection algorithm finds the k<sub>th</sub> value in an array and returns it.
If we do this for each k<sub>value</sub> then we will get the correct answer.

This algorithm runs in `O(nm)` time because the `selection` algorithm runs in `O(n)` time. 
We perform the `selection` algorithm `m` times and therefore we have `O(nm)`.

###Problem 4 part c
For this part `O(nlogm)` time is required.
To do this we will use the selection algorithm but modify it slightly.
In the selection algorithm, the pivot is found with around equal parts on either side of it.
Then the k<sup>th</sup> value is found. 
Instead of throwing away those two sections we have found, we will keep them. 
This will hep us average out to `O(nlogm)` time.

To start out we will use the middle array element of kArray (the array of k values).
We will find that k value and then have the selection algorithm return that k value as well as the two arrays it split.
We will then recursively call the values in the k array less than the middle one on the lower array, and the greater k values on the upper one.
This will allow us to not search through the entire array each time.

```
binaryK (array, kArray) {
    if kArray.length < 1 return {}
    
    midKIndex = kArray.length / 2
    currK = kArray[midKIndex]
    
    // This selection algorithm returns the k value, and the two 
    // sets of numbers higher and lower than the k value.
    {currKValue, lowArray, highArray} = selection(currK, array)
    
    // Subtract the midKIndex from all of the K in the upper part 
    // of the K array so that it is still finding the correct K.
    for index in kArray[midKindex+1 :] {
        kArray[index] -= kArray[midKIndex]
    }
    
    // Call the high and low sides recursively
    solvedK += binaryK(lowArray, kArray[0: midKIndex - 1])
    solvedK += binaryK(highArray, kArray[midKIndex + 1 :])
    
    // Return the array of solved k values
    return solvedK
}
```
This algorithm is correct because it checks every possible scenario for each k value.
The way that it is correct but improves upon previous designs is that it only checks possibilities and not all of the array.
If a k value is greater than the middle k value then it only needs to look at values greater than the value of the middle k.

This algorithm is `O(nlogm)` time because we have to do `n` operations `logm` times. 
This happens because each level of recursion we split the time in half but do two of it.
Each level does `n` work. 
This means that we do `n` work `logm` levels deep.
This means that `O(nlogm)` is the time of the equation.  
