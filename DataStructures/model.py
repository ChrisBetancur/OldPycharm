class Node:
    def __init__(self, data):
        self.data = data
        self.adjacency_list = []

    def get_adjacent(self, data):
        for node in self.adjacency_list:
            if node.data is data:
                return node
        return None

    def print_node(self):
        print(self.data, ": ", end="")

        for node in self.adjacency_list:
            print(node.data, ", ", end="")

        print()


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
