"""
Least Recently Used Cache
We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.

"""


class LRU_Cache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        """
        Time complexity: O(1)
        since we are using a dictionary to store the cache, and the lookup time for a dictionary is O(1)
        Space complexity: O(n)
        where n is the capacity of the cache
        """
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            return self.cache[key]
        return -1

    def set(self, key, value):
        """
        Time complexity: O(1)
        since we are using a dictionary to store the cache, and the lookup time for a dictionary is O(1),
        Space complexity: O(n)
        where n is the capacity of the cache
        """
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem()
            self.cache[key] = value


def included_test():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    our_cache.get(1)  # returns 1
    our_cache.get(2)  # returns 2
    our_cache.get(9)  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    our_cache.get(3)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Test for empty cache
def test_01():
    test_cache = LRU_Cache(5)

    assert test_cache.get(1) == -1, print("Failed Test Case 01")
    print("Test Case 1 - Pass")


# Test Case 2
# Test for None key and value
def test_02():
    test_cache = LRU_Cache(5)

    test_cache.set(None, None)

    assert test_cache.get(None) == None, print("Failed Test Case 02")
    print("Test Case 2 - Pass")


# Test Case 3
# Test for Large keys and values
def test_03():
    test_cache = LRU_Cache(5)

    test_cache.set(100000, 100000)
    test_cache.set(200000, 200000)
    test_cache.set(-400000, "Negative")
    test_cache.set(-500000, "Also negative")

    test_cache.get(100000)
    test_cache.get(200000)
    test_cache.get(-300000)

    assert test_cache.get(100000) == 100000, print("Failed Test Case 03")
    assert test_cache.get(200000) == 200000, print("Failed Test Case 03")
    assert test_cache.get(-300000) == -1, print("Failed Test Case 03")
    print("Test Case 3 - Pass")


if __name__ == "__main__":
    included_test()
    test_01()
    test_02()
    test_03()
