import networkx as nx


def read_input_as_graph(input_filename) -> nx.DiGraph:
    bg = nx.DiGraph()

    for rule in open(input_filename, "r"):  # generator
        rule = rule.strip("\n").strip()

        container, contents = rule.split("contain")

        # remove bags
        container_bag = container.strip().replace(" bags", "")
        bg.add_node(container_bag)

        if contents != " no other bags.":
            for content in contents.split(","):

                # remove bags or bag
                content = (
                    content.replace(".", "")
                    .replace("bags", "")
                    .replace("bag", "")
                    .strip()
                )
                bag = content[2:]
                weight = int(content[:2])

                bg.add_node(bag)
                bg.add_edge(container_bag, bag, weight=weight)

    return bg


def walk_preds(graph: nx.DiGraph, node, nodes_agg):
    predecessors = list(graph.predecessors(node))

    for pred in predecessors:
        if pred in nodes_agg:
            continue

        walk_preds(graph, pred, nodes_agg)
        nodes_agg.append(pred)

    return


def walk_to_root(graph: nx.DiGraph, starting_node):
    nodes = []

    walk_preds(graph, starting_node, nodes)

    return len(nodes)


def walk_succ(graph: nx.DiGraph, node):
    successors = list(graph.successors(node))
    total = 0

    for succ in successors:
        succ_weight = graph.get_edge_data(node, succ)["weight"]
        total += succ_weight * (1 + walk_succ(graph, succ))

    return total


def walk_to_leaves(graph, starting_node):
    return walk_succ(graph, starting_node)


if __name__ == "__main__":
    # Let's do a graph !
    # Directed (container has contents) and weighted (how many contained bag)
    # And then go back up the graph from the shiny gold bag

    # tests
    example_graph = read_input_as_graph("example")
    to_root = walk_to_root(example_graph, "shiny gold")
    assert to_root == 4

    # puzzle
    puzzle_graph = read_input_as_graph("puzzle")
    to_root = walk_to_root(puzzle_graph, "shiny gold")
    print(f"part_1 - possible_containers {to_root}")

    # part 2
    # tests
    to_leaves = walk_to_leaves(example_graph, "shiny gold")
    assert to_leaves == 32

    example_graph_2 = read_input_as_graph("example_2")
    to_leaves = walk_to_leaves(example_graph_2, "shiny gold")
    assert to_leaves == 126

    to_leaves = walk_to_leaves(puzzle_graph, "shiny gold")
    print(f"part_2 - number bags to leaves {to_leaves}")
