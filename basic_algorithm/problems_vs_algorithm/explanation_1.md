# Project1: Problems vs Algorithm
## 1. Square Root
First implementation I did was traversing all the number, and find which one was closest to the number to square.
This proved less efficient, so I implement a `Binary Search` on the list of numbers to verify.

It's important to notice that for a matemathic property, we can limit the list of number to search to 
**n/2**.

*Time complexity*, as we said is `O(log(N/2))`; *Space complexity* is equals to `O(N/2)` because the array to traverse is generated

## 2. Search Rotated Array
The Search in the Rotate Array is implemented as a `Recursive Binary Search`, with specific set of conditions
that allow us to leverage the end and the start of the array, to know if the rotation is before or after the mid index.

*Time complexity*, is the same of  binary search, then `O(log(N/2))`, while *Space complexity* is `O(1)` since we just use
variable to store the member of array, but we don't use other structure.

## 3. Re-arrange Array

Originally I use a permutation to get all possible list, and get the number out of the list, using the condition
that the number cannot have more than 1 digit of difference. This solution didn't scale up and was not efficient
being `O(n^2)`.

The most efficient approach is a `Divide and Conquer` one:
* Order the array
* Compose the numbers taking digits alternatively from the array.

The second point is working for a mathematical property and expecting all distinct number into array.
*Time complexity*, is the sum of a `Merge Sort` and of a single traversal, then:
```
O(Nlog(N)) + O(N) --> O(Nlog(N)
```
*Space complexity* is less, since `Merge Sort` is executed in place, therefore it is `O(N)`, because of the array
used to keep the sorted results.

## 4. Dutch Flag

this exercise is totally similar to `sort012` problem executed in the sorting section, in which sorting
is executed in place using 2 indices.

*Time complexity* is equal to `O(N)`, since the array is traversed once. *Space complexity* is less, and it's 
only O(1), considering the variables that are holding intermediates values.

## 5. Tries Autocomplete

The problems is solved leveraging a Trie, as explained in the course, having its insert operation performed
at `O(N)` complexity, where is N is the number of letters composing a word.

The find suffices operation was implemented via recursion, traversing all the nodes at  `O(N)` time complexity,
while the space complexity is equals to `O(1)`, since no additional objects are created.

## 6. Max Min Unsorted Array

I approached this problem with the most *naive* way possible, traversing the unsorted array and keeping track of the elements.
*Time complexity* is equal to `O(N)`, since the array is traversed once. *Space complexity* is less, and it's 
only O(1), considering the variables that are holding intermediates values.

## 7. Http Router with Trie

Also router problem used tre Trie, as explained in the course, and all the insert operation performed
at `O(N)` complexity, where N is the number of element composing a path.

The Look-up operation was implemented via recursion, traversing all the nodes at  `O(N)` *Time complexity*,
while the space complexity is equals to `O(1)`, since no additional objects are created.

