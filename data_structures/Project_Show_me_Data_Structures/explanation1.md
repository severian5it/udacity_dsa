# Explanation or Project 1

## LRU Cache

The problem is solved with the usage of 2 Data structure

* List
* Double Linked List

## File Recursion

a Recursive function has been implemented using `os` module. Being the recursive nature, the complexity
is:
```
O(N)
```

Being N the number of directory in the hierarchy.

## Huffman Coding

The problem is solved with the usage of 3 Data structure

* Hashmap containing the frequency of letters
* Priority Queue
* Binary Tree

## Active Directory

The look up has been implemented via recursion, first is checked whether user is in current group,
then the function is called recursively on groups belonging to the parent group.
The complexity is therefore at worst case:
```
O(N)
```

Being N the number of groups in the hierarchy.


## Blockchain

Block-chain has been implemented by usage of a Linked List, where the *tail* is stored as an attribute, 
and not the head, as it happens in a traditional Linked List.

A new attribute has been added to the block to keep track of the previous block, since is not 
possible to do the same with the hash. The Block-chain has same performance of a linked list, therefore:

**Insert:** O(1) since is appended directly to the tail.

**Delete:** O(N) traversing all the list.

**Search:** O(N) traversing all the list.

**Size:** O(N) traversing all the list.



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
O(N) + O(N)*O(1) --> O(2N)--> O(N)
```



