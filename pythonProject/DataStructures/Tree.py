import random

import equals as equals


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_node(root, data):
    if root is None:
        root = Node(data)
    elif root.data < data:
        root.right = insert_node(root.right, data)
    else:
        root.left = insert_node(root.left, data)
    return root


def convert_tree_to_array(root, arr):
    if root is not None:
        convert_tree_to_array(root.left, arr)
        arr.append(root.data)
        convert_tree_to_array(root.right, arr)


def convert_array_to_tree(arr, root):
    if arr is not None:
        for curr_node in arr:
            insert_node(root, arr[0])
        return root
    return root


def get_minimum_value(root):
    if root.left is None:
        return root
    else:
        return get_minimum_value(root.left)


def delete_node(root, data):
    if root is None:
        return root
    if root.data == data:
        if root.left is None and root.right is None:
            root = None
            return root
        else:
            minimum_node = get_minimum_value(root)

            root = minimum_node

            delete_node(root, minimum_node.data)

            return root;
    else:
        if root.data < data:
            root.right = delete_node(root.right, data)

        else:
            root.left = delete_node(root.left, data)
    return root


def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.data)
        print_tree(root.right)


node = Node(4)

for x in range(10):
    if x == 6:
        insert_node(node, 8)
    if x == 8:
        insert_node(node, 12)
    insert_node(node, random.randint(0, 20))

print_tree(node)

print()
print()

delete_node(node, 8)
print_tree(node)

print()
print()

array = []

convert_tree_to_array(node, array)

#array.remove(12)

if array is not None:
    print("Entered")
    for x in array:
        print("in loop")
        if x == 12:
            print("12 is present")

'''node = None

node = convert_array_to_tree(array)

print_tree(node)'''

'''print(array)

node = None

print("Removed 12")
convert_array_to_tree(array, node)

print_tree(node)

if node is None:
    print("null")'''
