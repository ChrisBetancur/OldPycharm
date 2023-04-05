
class Node:
    def __init__(self, data):
        self._data = data
        self._node_list = []

    def get_node(self, data):
        for curr_node in self._node_list:
            if curr_node.get_data == data:
                print(curr_node.get_data())
                return True
        return False

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_node_list(self):
        return self._node_list

    def set_list(self, node_list):
        self._node_list = node_list


class Graph:
    def __init__(self):
        self._graph = []

    def get_graph(self):
        return self._graph

    def set_graph(self, _graph):
        self._graph = _graph

    def get_node(self, data):
        for curr_node in self._graph:
            if curr_node.get_data() == data:
                return curr_node
        return None


def append_node(curr_graph, source_data, destination_data):
    source_node = curr_graph.get_node(source_data)
    destination_node = curr_graph.get_node(destination_data)

    if source_node is None:
        source_node = Node(source_data)
        curr_graph.get_graph().append(source_node)

    if destination_node is None:
        destination_node = Node(destination_data)
        curr_graph.get_graph().append(destination_node)

    if source_node.get_node(destination_data) is not True:
        source_node.get_node_list().append(destination_node)

    if destination_node.get_node(destination_node) is not True:
        destination_node.get_node_list().append(source_node)


def delete_node_from_graph(curr_graph, data):
    node = curr_graph.get_node(data)

    if node is None:
        return

    for curr_node in curr_graph.get_graph():
        for neighbour in curr_node.get_node_list():
            if neighbour.get_data() is data:
                curr_node.get_node_list().remove(node)
    curr_graph.get_graph().remove(node)


# def delete_node_from_list()

def print_graph(curr_graph):
    if curr_graph is not None:
        for current_node in curr_graph.get_graph():
            print(current_node.get_data(), ": ", end='')
            for neighbour in current_node.get_node_list():
                print(neighbour.get_data(), ", ", end='')
            print("\n")


graph = Graph()

append_node(graph, 3, 8)
append_node(graph, 3, 10)
append_node(graph, 10, 7)
delete_node_from_graph(graph, 10)
print_graph(graph)
