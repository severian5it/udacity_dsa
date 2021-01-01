# Explanation or Project 1

## LRU Cache

The problem is solved with the usage of 2 Data structure.

* Python Dictionary.
* Double Linked List.

It could have been possible use *a hash function* and a *bucketed list* in place of the dictionary, 
however I used the last one for the sake of simplicity.

The *Double Linked List* allows to keep track of the least recent used element, and to evict it, when 
capacity is exhausted. Least used element is always at the head, while the most recent 
used is always moved at the tail.

The Double Linked List is created with a tail and a head node already in place, this way it was possible
to implement the algorithm without taking care of situation in which head and tail were the same or were None.

The complexity of this implementation is the following:

**Get:** O(1) to retrieve from dictionary and O(1) to move it to the end of the DLL, therefore `O(1)`.

**Set:** O(1) to put it in the dictionary, O(1) to move it to the end of the DLL and, in case capacity
is a above the limit, an additional O(1)  to evict the least recently used element. In total is `O(1)`.

Space Complexity will be  more severe `O(k) + O(k) -> O(2k)`, where k is the max size, this because 
of Linked List and Hashmap usage.




## File Recursion

a Recursive function has been implemented using `os` module. Given the recursive nature, the Time complexity
is:
```
O(N)
```

Being N the number of directory in the hierarchy. Space complexity will be `O(N)`, related to the output string.

## Huffman Coding

The problem is solved with the usage of 3 Data structure

* Hashmap containing the frequency of letters.
* Priority Queue.
* Binary Tree.

the *Priority Queue* is re-implementation of the queue, adapted to the Node that are composing the binary
Tree.
When popping from the *Priority Queue*, all the queue is traversed to find the top priority element.

The *Hashmap* with the frequency is created traversing the original sentence; The *Binary Tree* contains in 
each node the Letter and the Priority.

Let's analyse the complexity, breaking what happens in encoding/decoding phase.

**Encoding:** following events are happening:
1. The sentence is traversed with O(N) complexity to form the Frequency Hashmap, Where n is the original lenght of the string. 
1. Frequency Hashmap is traversed with with O(k) complexity to generate Nodes that are inserted in Priority Queue; where k the 
number of the letters
1. Nodes are popped out from the Priority Queues 2 by 2, to form new nodes. The complexity of this 
phase is roughly O(2k*k) being k the number of nodes.
1. the Binary Tree formed is searched N times, for each character of the string. Each Search has O(logk)
complexity, being the tree binary, therefore the total complexity is O(Nlogk)

The Time complexity of the function is:
```
O(N) + O(k) + O(2k^2) + O(Nlogk) --> O(N) + O(k^2) + O(Nlogk)
```

Space Complexity will be limited to the Data structures used, which are:
* Hashmap: `O(k)`
* Priority Queue: `O(k)`
* Binary Tree `O(2k)`
therefore space complexity will be only depending by number of letters and be `O(N)`

is clear that encoding complexity is function of the length of the string and of the number
of characters, the latest being predominant for small sentence with many characters.

**Decoding:** following events are happening:
1. The encoded sentence is traversed with at least O(N) complexity.
1. for each element we are moving through the binary tree, so at most with complexity O(logk). At most
because the whole tree is traversed with many letters.
1. Decoded list is traversed with O(N) complexity to be returned as string.

The Time complexity of the function is:
```
O(N) + O(logk) + O(N) -> O(2N)
```
so length of string is predominant in this case.

Space Complexity here is related to string output, which will be `O(N)` and the Binary Tree `O(2k)`,
and then it will be depending on 2 factors, being the length of the string to decode the most impacting


## Active Directory

The look up has been implemented via recursion, first is checked whether user is in current group,
then the function is called recursively on groups belonging to the parent group.
The Time complexity is therefore at worst case:
```
O(N)
```

Being N the number of groups in the hierarchy. Space Complexity will be also `O(N` because of variable
used to hold boolean values, it can be reduced performing calculation in place.



## Blockchain

Block-chain has been implemented by usage of a Linked List, where the *tail* is stored as an attribute, 
and not the head, as it happens in a traditional Linked List.

A new attribute has been added to the block to keep track of the previous block, since is not 
possible to point back only with the hash. The Block-chain has same performance of a linked list, therefore:

**Insert:** `O(1)` since is appended directly to the tail.

**Delete:** `O(N)` traversing all the *linked list*.

**Search:** `O(N)` traversing all the *linked list*.

**Size:** `O(N)` traversing all the *linked list*.

Space Complexity will be  ` O(N` because of Linked List usage.



## Union and Intersection

The implementation of the two functions is based on a *linked list* and takes advantage of a *set* 
in the case of intersection. 

**Union:** the first Linked List is traversed till the end, and each element is inserted in the new 
 output, then the second is traversed and the new elements gets inserted, therefore it has Time complexity: 
```
O(2N) --> O(N)
```
Space Complexity will be also `O(N)` since the Linked List will be created from scratch.

**Intersection:** the first linked list is traversed, and each element is inserted into 
a set. the second is then traversed, and if the element is present in the set, gets also inserted 
in the output linked list.
Considering lookup into the set as O(1), for the low number of element, complexity is:
```
O(N) + O(N)*O(1) --> O(2N)--> O(N)
```

Space Complexity will be also `O(2N) --> O(N` since the new Linked List will be created from scratch 
and we will need space also for a set.




