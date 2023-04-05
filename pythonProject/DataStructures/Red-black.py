class Node:
    def __init__(self, data, color):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None


def insert_node(root, data, parent):
    if root is None:
        root = Node(data, True)
        root.parent = parent
        return root
    elif root.data < data:
        root.right = insert_node(root.right, data, root)
    else:
        root.left = insert_node(root.left, data, root)
    return root


def insertion(root, data):
    insert_node(root, data)

    if root.color is True:
        root.color = False

    parent = get_parent(root, data)
    sibling = get_sibling(root, data)

    if parent.color is False:
        return

    if parent.color is True:
        if sibling is None or sibling.color == False:
            print()


def left_rotate(root, left_curr_node):
    right_curr_child = left_curr_node.right
    left_curr_node.right = right_curr_child.left

    if right_curr_child.left is not None:
        right_curr_child.left.parent = left_curr_node


def get_sibling(root, parent):
    if root.left.data == parent.data:
        return root.right
    if root.right.data == parent.data:
        return root.left
    if root.data < parent.data:
        get_parent(root.right, parent.data)
    if root.data > parent.data:
        get_parent(root.left, parent.data)


def get_parent(root, data):
    if root.left.data == data or root.right.data == data:
        return root
    if root.data < data:
        get_parent(root.right, data)
    if root.data > data:
        get_parent(root.left, data)


def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    if root.parent is not None:
        print(root.data, " Parent: ", root.parent.data)
    else:
        print(root.data)
    print_tree(root.right)


root = Node(4, False)

insert_node(root, 5, None)

insert_node(root, 3, None)

insert_node(root, 9, None)

print_tree(root)
