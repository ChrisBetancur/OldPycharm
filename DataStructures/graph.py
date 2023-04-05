from model import Node, Edge


class Graph:
    def __init__(self):
        self.list = []
        self.edges = []

    def get_node(self, data):
        for node in self.list:
            #print(node.data)
            if node.data == data:
                return node
        return None


def append_node(graph, src_data, dest_data, is_two_way, weight=None):
    if graph is None or src_data == dest_data:
        return

    src = graph.get_node(src_data)
    dest = graph.get_node(dest_data)

    if src is None:
        src = Node(src_data)
        graph.list.append(src)

    if dest is None:
        dest = Node(dest_data)
        graph.list.append(dest)

    if src.get_adjacent(dest_data) is None:
        src.adjacency_list.append(dest)

        if weight is not None:
            graph.edges.append(Edge(src, dest, weight))

    if is_two_way is True and dest.get_adjacent(src_data):
        dest.adjacency_list.append(src)

        if weight is not None:
            graph.edges.append(Edge(dest, src, weight))


def delete_node(graph, data):
    pass


def print_graph(graph):
    if graph is None:
        return

    for node in graph.list:
        node.print_node()


def print_edges(graph):
    if graph is None:
        return

    for edge in graph.edges:
        print(edge.src.data, " -> ", edge.dest.data, " weight = ", edge.weight)
