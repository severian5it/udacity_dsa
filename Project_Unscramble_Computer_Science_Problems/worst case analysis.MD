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
pseudo code for the implementation is as below:
```

```