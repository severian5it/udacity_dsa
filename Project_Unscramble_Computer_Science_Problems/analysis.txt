# Worst Case Analyis
Time complexity for basic operations in Python is coming from  [Python wiki: Time complexity](https://wiki.python.org/moin/TimeComplexity)
In the pseudo code I didn't include the opening of the two files.
## Task0
pseudo code for the implementation is as below:
```
* Access first Element Call.
* Access Last Element Texts.
```
Getting an item at a specific index for a list is an operation of O(1) complexity, since a hash table
under the hood is keeping track of position, therefore the worst case complexity is:
```
2O(1) --> O(1)
```

## Task1
pseudo code for the implementation is as below:
```
* Loop through all calls, add caller and receiver to set.
* Loop through all text, add texter and receiver to set.
* Print length of the set.
```
Ideal data structure is a `set` to store all those results.
Worst case complexity will be:
```
O(N) + O(N) --> 2O(N) --> O(N)
```


## Task2
pseudo code for the implementation is as below:
```
* Loop through all calls, populating a dictionary with key the number and value the duration
* Loop through key, value pairs in dictionary, storing the highest duration and the key that spent
the most time
* print the results accessing the dictionary
```
Ideal data structure is a `hashmap` to store all those results.
Worst case complexity will be:
```
O(N) + O(N) + O(1) --> 2O(N) + O(1) --> O(N)
```

## Task3
pseudo code for the implementation is as below:
```
* Loop through all calls: if they are from bangalore include in set of Caller.
* Sort the result set
* Loop through it and print it
* Loop through all calls: if they are from bangalore include in dictionary with prefix as key and 
raise the number of total calls.
* access the dictionary with bangalore key and print it agains the total.
```

Ideal data structure are a `set` to store the distinct prefix and a `hashmap` to store the number of
calls by prefix.
Worst case complexity will be:
```
O(N) + O(NLogN) + O(N) + O(N) + O(1) --> 2O(N) + O(NLogN) + O(1) --> O(NLogN)
```

## Task4
**Input:** list of calls and text.

**Output:** Sorted List of Number who never texted **and** never received a call or a text.

pseudo code for the implementation is as below:
```
* Loop through all calls to create a Set of Caller.
* Loop through all calls to create a Set of Call Receiver.
* Loop through all texts to create a Set of Texter.
* Loop through all texts to create a Set of Text Receiver.
* Remove from the Caller all Call Receiver via set difference.
* Remove from the caller all Texter via set difference.
* Remove from the caller all text receiver via set difference.
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