# GAME PLAN
    #  Only uses list and tuple collection types
    #  Must have O(log n) lookup time
    #  Can set any type of value to associate it w/ a key
    #  Can get the value assocaite w/ a key
    #  Can delete a key and its associated value
    #  Can test if the has table contains a key
    #  Can get a list of all keys in the hash table
    #  Get get a list of all values in the hash table
    #  Can get a list of all entries (key-value pairs)
    #  Can calculate the length of the hash table

from linked_list import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size.
        """
        # Create new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]


    def __str__(self):
        """Return a formatted string representation of this hash table.
        """
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'


    def __repr__(self):
        """Return a string representation of this hash table.
        """
        return 'HashTable({!r})'.format(self.items())


    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored.
        """
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)


    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n), will iterate over every item
        """
        all_keys = []
        for bucket in self.buckets: #Loop thru all buckets
            for key, value in bucket.items():
                all_keys.append(key) # Collect all keys in each bucket
        return all_keys


    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n), must iterate over all items"""
        all_values = []
        for bucket in self.buckets: # Loop thru all buckets
            for key, value in bucket.items():
                all_values.append(value) # Collect all values in each bucket
        return all_values


    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Run time: O(n), must iterate over all key-value pairs?
        """
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items


    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Run time: O(n), must check all buckets?
        """
        counter = 0
        for bucket in self.buckets: # Loop thru buckets
            length = bucket.length()
            counter += length # Count key-value entries in each bucket
        return counter


    def contains(self, key):
        """Return True if this hash table has the given key, or if False.
        Run time :
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        return bucket.find(lambda item: item[0] == key) != None

    def get(self, key):
        """Return the value associated with key, or raise KeyError.
        Run time: O(1), hash tables have constant lookup time
        """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed

        index = self._bucket_index(key) # O(1) to calc index
        item = self.buckets[index].find(lambda item: item[0] == key)
        if item != None:
            return item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))


    def set(self, key, value):
        """Insert or update the given key with associated value.
        Run time: O(1), """
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key) # O(1) to calc index
        found_it = self.buckets[index].find(lambda item: item[0] == key)

        if found_it:
            self.buckets[index].delete(found_it)
        self.buckets[index].append((key,value))

        # if entry is not None:
        #     # bucket.delete(entry) #O(l)
        #     entry2 = (key,value)
        #     bucket.replace(entry, entry2)
        #
        #     entry = (key, value) #O(1)di
        #     bucket.append(entry) #O(1)
        #

    def delete(self, key):
        """Delete given key from hash table, or raise KeyError.
        Run time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key) # O(1) index
        found_it = self.buckets[index].find(lambda item: item[0] == key) #O(n), Find
        if found_it:
            self.bucket[index].delete(found_it) # O(l) b/c l entries in the list
        else:
            raise KeyError('Key not found {}'.format(key))


# TEST METHOD
def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
