# Explanation or Project 1

## LRU Cache

The problem is solved with the usage of 2 Data structure

* List
* Double Linked List

## File Recursion

## Huffman Coding

The problem is solved with the usage of 3 Data structure

* Hashmap containing the frequency of letters
* Priority Queue
* Binary Tree

## Active Directory

## Blockchain

## Union and Intersection

The implementation of the two functions is based on a *linked list* and takes advantage of a *set* 
in the case of intersection. 
**union:** the first Linked List is traversed till the end, and each element is inserted in the new 
 output, then the second is traversed and the new elements gets inserted, therefore it has complexity: 
```
O(2N) --> O(N)
```
**intersection:** the first linked list is traversed, and each element is inserted into 
a set. the second is then traversed, and if the element is present in the set, gets also inserted 
in the output linked list.
Considering lookup into the set as O(1), for the low number of element, complexity is:
```
O(N) + O(N)*O(1) --> O(2N)--> O(1)
```



