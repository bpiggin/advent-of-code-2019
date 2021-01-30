import networkx as nx

f = open("input.txt", "r")
f_input = f.read().split("\n")


def part_one():
    graph = nx.Graph(x.split(")") for x in f_input)
    orbits = sum(nx.shortest_path_length(graph, node, "COM") for node in graph.nodes)
    print(orbits)


# --------------------------------------------------------------


def part_two():
    graph = nx.Graph(x.split(")") for x in f_input)
    transfers = nx.shortest_path_length(graph, "YOU", "SAN") - 2
    print(transfers)


if __name__ == "__main__":
    # part_one()
    part_two()
