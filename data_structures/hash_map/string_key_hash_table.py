"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """TODO: Input a string that's stored in
        the table."""
        idx = self.calculate_hash_value(string)
        if idx != -1:  # if the string is a new one
            if self.table[idx] != None:  # if the bucket is non-empty
                self.table[idx].append(string)  # append the string in the list at that bucket
            else:
                self.table[idx] = [string]

    def lookup(self, string):
        """TODO: Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        idx = self.calculate_hash_value(string)
        if self.table[idx] != None:
            if string in self.table[idx]:
                return idx
        return -1

    def calculate_hash_value(self, string):
        """TODO: Helper function to calulate a
        hash value from a string."""

        return ord(string[0])*100+ord(string[1])

# Setup
hash_table = HashTable()

# Test calculate_hash_value
print (hash_table.calculate_hash_value('UDACITY'))    # Should be 8568

# Test lookup edge case
print (hash_table.lookup('UDACITY'))                  # Should be -1

# Test store
hash_table.store('UDACITY')
print (hash_table.lookup('UDACITY'))                  # Should be 8568

# Test store edge case
hash_table.store('UDACIOUS')
print (hash_table.lookup('UDACIOUS'))                 # Should be 8568

