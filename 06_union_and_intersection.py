"""
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, the union of A = [1, 2] and B = [3, 4] is [1, 2, 3, 4].

The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both sets A and B. For example, the intersection of A = [1, 2, 3] and B = [2, 3, 4] is [2, 3].

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def as_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next

        return out_list


# Find the union of two linked lists
# Time complexity: O(n + m)
# Because we are iterating through both linked lists,
# and also using a hash table and iterating through it, the time complexity is O(n + m + k)
# Space complexity: O(n + m + k)
# This is worst case only as we don't know the size of the union
def union(llist_1, llist_2):
    hash_table = {}
    union_list = LinkedList()
    while llist_1.head:
        hash_table[llist_1.head.value] = 1
        llist_1.head = llist_1.head.next
    while llist_2.head:
        hash_table[llist_2.head.value] = 1
        llist_2.head = llist_2.head.next
    for key in hash_table:
        union_list.append(key)
    return union_list


# Find the intersection of two linked lists
# Time complexity: O(n + m)
# Because we are iterating through both linked lists,
# and also using a hash table and iterating through it, the time complexity is O(n + m + k1 + k2)
# Space complexity: O(n + m + k1 + k2)
# This is worst case only as we don't know the size of the intersection
def intersection(llist_1, llist_2):
    hash_list_1 = {}
    hash_list_2 = {}
    intersection_list = LinkedList()
    while llist_1.head:
        hash_list_1[llist_1.head.value] = 1
        llist_1.head = llist_1.head.next
    while llist_2.head:
        hash_list_2[llist_2.head.value] = 1
        llist_2.head = llist_2.head.next
    for key in hash_list_1:
        if key in hash_list_2:
            intersection_list.append(key)
    return intersection_list


# Default test case 1
def default_test_case_1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)
        linked_list_3.append(i)

    for i in element_2:
        linked_list_2.append(i)
        linked_list_4.append(i)

    union_result = union(linked_list_1, linked_list_2)
    interestion_result = intersection(linked_list_3, linked_list_4)

    assert union_result.as_list() == [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11], "Default test 1 Failed: Union is incorrect"
    assert interestion_result.as_list() == [4, 6, 21], "Default test 1 Failed: Intersection is incorrect"

    print("Default test 1 Passed")


# Default test case 2
def default_test_case_2():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)
        linked_list_3.append(i)

    for i in element_2:
        linked_list_2.append(i)
        linked_list_4.append(i)

    union_result = union(linked_list_1, linked_list_2)
    interestion_result = intersection(linked_list_3, linked_list_4)

    assert union_result.as_list() == [
        3,
        2,
        4,
        35,
        6,
        65,
        23,
        1,
        7,
        8,
        9,
        11,
        21,
    ], "Default test 2 Failed: Union is incorrect"
    assert interestion_result.as_list() == [], "Default test 2 Failed: Intersection is incorrect"

    print("Default test 2 Passed")


# Test Case 1
# Test for empty linked list
def test_01():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    union_result = union(linked_list_1, linked_list_2)
    interestion_result = intersection(linked_list_3, linked_list_4)

    assert union_result.as_list() == [], "Test case 01 Failed: Union is incorrect"
    assert interestion_result.as_list() == [], "Test case 01 Failed: Intersection is incorrect"

    print("Test case 01 Passed")


# Test Case 2
# Test for single element linked list
def test_02():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [1]
    element_2 = [1]

    for i in element_1:
        linked_list_1.append(i)
        linked_list_3.append(i)

    for i in element_2:
        linked_list_2.append(i)
        linked_list_4.append(i)

    union_result = union(linked_list_1, linked_list_2)
    interestion_result = intersection(linked_list_3, linked_list_4)

    assert union_result.as_list() == [1], "Test case 02 Failed: Union is incorrect"
    assert interestion_result.as_list() == [1], "Test case 02 Failed: Intersection is incorrect"

    print("Test case 02 Passed")


# Test Case 3
# Test for None linked list
def test_03():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [None]
    element_2 = [None]

    for i in element_1:
        linked_list_1.append(i)
        linked_list_3.append(i)

    for i in element_2:
        linked_list_2.append(i)
        linked_list_4.append(i)

    union_result = union(linked_list_1, linked_list_2)
    interestion_result = intersection(linked_list_3, linked_list_4)

    assert union_result.as_list() == [None], "Test case 03 Failed: Union is incorrect"
    assert interestion_result.as_list() == [None], "Test case 03 Failed: Intersection is incorrect"

    print("Test case 03 Passed")


if __name__ == "__main__":
    default_test_case_1()
    default_test_case_2()
    test_01()
    test_02()
    test_03()
