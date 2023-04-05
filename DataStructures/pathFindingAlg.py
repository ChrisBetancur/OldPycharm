def dfs(graph, src_data, dest_data):
    src = graph.get_node(src_data)
    dest = graph.get_node(dest_data)

    if src is None or dest is None:
        return False

    return dfs_start(graph, src, dest, set())


# return False

def dfs_start(graph, src, dest, visited):
    visited.add(src)

    print(src.data, end=", ")

    if src.data == dest.data:
        print("Entered")
        return True

    for node in src.adjacency_list:
        if node not in visited:
            return dfs_start(graph, node, dest, visited)

    return False


def bfs(graph, src, dest):
    queue = []
    visited = []

    queue.append()
