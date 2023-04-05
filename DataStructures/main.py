import random

from graph import Graph, append_node, print_graph, print_edges
from pathFindingAlg import dfs


def main():
    graph = Graph()

    for i in range(10):
        two_way = random.randint(0,1)
        is_two_way = False

        if two_way == 0:
            is_two_way = True
        if i == 1 :
            append_node(graph, 2, random.randint(0, 15), False, 4)
        if i == 10:
            append_node(graph, 15, 4, False, 1)
        append_node(graph, random.randint(0,15), random.randint(0, 15), is_two_way, random.randint(0, 5))

    '''append_node(graph, 2, 10, True, 4)
    append_node(graph, 8, 10, True, 4)
    append_node(graph, 1, 4, True, 4)
    append_node(graph, 1, 6, True, 4)
    append_node(graph, 6, 10, True, 4)
    append_node(graph, 6, 15, True, 4)'''



    print_graph(graph)

    print()
    print()

    #print_edges(graph)

    # print(graph.get_node(15).data)

    #print(graph.get_node(2).data, " : ", graph.get_node(15).data)

    print(dfs(graph, 2, 15))


if __name__ == "__main__":
    main()
