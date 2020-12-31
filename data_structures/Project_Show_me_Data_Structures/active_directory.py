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
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    is_in_group = False
    is_in_subgroup = False

    for u in group.get_users():
        if u == user:
            is_in_group = True

    for g in group.get_groups():
        if is_user_in_group(user, g):
            is_in_subgroup = True

    return is_in_group or is_in_subgroup


if __name__ == "__main__":
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    # Test Case1
    print(f"is sub child user in parent group? {is_user_in_group(sub_child_user, parent)}") # expected True
    # Test Case2
    print(f"is sub child user in child group? {is_user_in_group(sub_child_user, child)}")  # expected True
    # Test Case3
    print(f"is sub child user in sub child group? {is_user_in_group(sub_child_user, sub_child)}")  # expected True
    # Test Case4
    print(f"is sub child user2 in sub child group? {is_user_in_group('sub_child_user2', parent)}")  # expected False
