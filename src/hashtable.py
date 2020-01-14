# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None



class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count=0
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index=self._hash_mod(key)
        if self.storage[index] is None:
            self.storage[index]=LinkedPair(key, value)
            return
        current = self.storage[index]
        previous=self.storage[index]
        while current is not None:
            previous = current
            if previous.key==key:
                previous.value=value
            current = current.next
        if self.count == self.capacity:
            self.resize()
            return
		# Add a new node at the end of the list with provided key/value

        previous.next = LinkedPair(key, value)
        self.count+=1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index=self._hash_mod(key)
        current = self.storage[index]
        while current.key!=key:
            current=current.next
        if current.value==None:
            print("return_value is None")
        else:
            current.value=None
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index=self._hash_mod(key)
        current = self.storage[index]
        if current.key==key:
            return current.value
        while current.key!=key:
            current=current.next
        return current.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity*=2
        new_storage=[None]*self.capacity
        old_storage=self.storage
        self.storage=new_storage
        for i in old_storage:
            if i is not None:
                self.insert(i.key,i.value)
                while i.next:
                    i=i.next
                    self.insert(i.key,i.value)
 




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
