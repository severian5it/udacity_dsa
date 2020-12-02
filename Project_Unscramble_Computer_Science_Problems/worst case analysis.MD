# Worst Case Analyis
Time complexity for basic operations in Python is coming from  [Python wiki: Time complexity](https://wiki.python.org/moin/TimeComplexity)
## Task0
pseudo code for the implementation is as below:
```
Open Call File.
Open Text File.
Access first Element Call.
Access Last Element Texts.
```
Getting an item at a specific index for a list is an operation of O(1) complexity, since a hash table
under the hood is keeping track of position, therefore the worst case complexity is:

2*O(1) --> O(1)

## Task1
pseudo code for the implementation is as below:
```
Open Call File.
Open Text File.
for call in calls
    if not in unique number
        add it

for text in Texts
    if not in unique number
        add it

```
A set is used to store unique numbers, a set is implemented as a hash table. So lookup/insert/delete 
are O(1). and the set len is O(1),
looping through the 2 files is O(k)+ O(n), if we assume having same length, worst case complexity is:
2O(n)*O(1) + O(1) --> O(n)


## Task2
pseudo code for the implementation is as below:
```

```
## Task3
pseudo code for the implementation is as below:
```

```
## Task4
**Input:** list of calls and text.

**Output:** Sorted List of Number who never texted **and** never received a call or a text.

pseudo code for the implementation is as below:
```
* Create a Set of Caller.
* Create a Set of Call Receiver.
* Create a Set of Texter.
* Create a Set of Text Receiver.
* Remove from the Caller all Call Receiver.
* Remove from the caller all Texter.
* Remove from the caller all text receiver.
* Sort the remaining caller.
* Go through each remaining caller and print one by one.
```

The Ideal Data structure I used for each step is a `set`, knowing that:
1. adding each element to a set as complexity O(1), but to do that we have to go through each 
element of a list, with complexity O(N).
1. Difference between set is performed with O(n) complexity in the best cases, but in worst cases 
(maximizing collisions with hashes) it can raise to O(n**2).
1. Sorting a set with Sorted method is implementation of *TimSort* and has complexity O(nlogn)

Complexity will be in the best case, assuming N as number of elements of both call and texts:
```
O(N) + O(N) + O(N) + O(N) + O(N) + O(N) + O(N) + O(NlogN) + O(N) --> 8O(N) + O(NlogN) --> O(NlogN)
```

growing the number of element in the calls and texts, and maximizing the number of collision, we 
will have for the worst case:
```
O(N) + O(N) + O(N) + O(N) + O(N**2) + O(N**2) + O(N**2) + O(NlogN) + O(N) --> 5O(N) + 3O(N**2) + O(NlogN) --> O(N**2)
```