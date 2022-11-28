"""
Active Directory
In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.
"""


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Time complexity: O(n)
    the time complexity is O(n) where n is the number of groups in the hierarchy
    Space complexity: O(n)
    since we are using a dictionary to store the cache,
    the space complexity is O(n) where n is the number of groups in the hierarchy

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not group or not user:
        print("There should be a user and group in the function call")
        return False

    if user in group.get_users():
        return True
    else:
        for group in group.get_groups():
            return is_user_in_group(user, group)
    return False


# Default test case
def default_test():
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    assert is_user_in_group("sub_child_user", parent) == True, "Default test failed, sub_child_user should be in parent"
    assert is_user_in_group("sub_child_user", child) == True, "Default test failed, sub_child_user should be in child"
    assert (
        is_user_in_group("sub_child_user", sub_child) == True
    ), "Default test failed, sub_child_user should be in sub_child"

    assert is_user_in_group("parent_user", parent) == False, "Default test failed, parent_user should not be in parent"
    assert is_user_in_group("child_user", child) == False, "Default test failed, child_user should not be in child"

    print("Default test passed")


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Test where None is passed in as a user or group
def test_01():
    assert is_user_in_group(None, None) == False, "Test 01 Failed"

    print("Test 01 Passed")


# Test Case 2
# Test where empty string is passed in as a user or group
def test_02():
    assert is_user_in_group("", "") == False, "Test 02 Failed"

    print("Test 02 Passed")


# Test Case 3
# Test for very large hierarchy
def test_03():
    groups = {}
    for i in range(500):
        new_user = "user" + str(i)
        new_group = Group("group" + str(i))
        groups[i] = new_group
        groups[i].add_user(new_user)
        if i > 0:
            groups[i - 1].add_group(groups[i])

    assert is_user_in_group("user499", groups[499]) == True, "Test 03 failed, user499 should be in group499"
    assert is_user_in_group("user499", groups[0]) == True, "Test 03 failed, user499 should be in group0"
    assert is_user_in_group("user2", groups[499]) == False, "Test 03 failed, user2 should not be in group499"
    assert is_user_in_group("user2", groups[2]) == True, "Test 03 failed, user2 should be in group2"
    assert is_user_in_group("user2", groups[0]) == True, "Test 03 failed, user2 should be in group0"

    print("Test 03 Passed")


if __name__ == "__main__":
    default_test()
    test_01()
    test_02()
    test_03()
