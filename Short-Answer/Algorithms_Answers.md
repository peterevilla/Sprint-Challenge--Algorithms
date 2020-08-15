#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

    No matter the range of the loop, the operation result is proportional compare of size of n.


b) O(nlog n)

    the outer loop in O(n) but inner loop increments by 2, log n


c) O(n)

Uses recursion but each call only has one recursive call. Like a single for loop.

## Exercise II

In order to minimize the number of dropped + eggs broken, i would find a way to compare f with the height of the floor, so i need to compare (drop a egg) to test the height that the egg would not broke. I would to a Binary search, starting from the middle of the bulding, if the egg brokes, i will search the lower half of the building starting from the middle of the lower half, if not, the same for the higher half, starting from its middle...if we avoid a broken egg check its higher middle, if it break, the one breaks is f.


