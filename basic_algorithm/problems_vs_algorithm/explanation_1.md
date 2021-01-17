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

*Time complexity*, is the same of  binary search, then `O(log(N/2))`, while space complexity is `O(1)` since we just use
variable to store the member of array, but we don't use other structure.

## 3. Re-arrange Array
## 4. Dutch Flag
## 5. Tries Autocomplete
## 6. Max Min Unsorted Array
## 7. Http Router with Trie

