import typing
import queue
import collections


def data_from_file(filename: str) -> typing.Tuple[typing.Dict, typing.Dict]:
    structure, weights = {}, {}
    with open(filename) as fh:
        for l in fh:
            node, weight, children = parse_data_line(l)
            structure[node] = children
            weights[node] = weight
    return structure, weights


def parse_data_line(line: str) -> typing.Tuple[str, int, typing.List[str]]:
    if '->' in line:
        node, weight, arrow, *children = line.split()
        children = [c.strip(',') for c in children]
    else:
        node, weight = line.split()
        children = []
    weight = int(weight[1:-1])
    return node, weight, children


def get_root(structure: dict) -> str:
    all_nodes = set(structure)
    child_nodes = sum(list(structure.values()), [])
    root_nodes = all_nodes - set(child_nodes)
    assert len(root_nodes) == 1
    return next(iter(root_nodes))


def sum_of_weighs(structure, weights, start_node):
    return weights[start_node] + children_weights(structure, weights, start_node)


def children_weights(structure, weights, start_node):
    return sum(sum_of_weighs(structure, weights, child) for child in structure[start_node])


def get_unbalanced_node_and_expected_weight(structure, weights, start_node):
    stack = prepare_nodes_to_visit(structure, start_node)

    while stack:
        node_to_check = stack.pop()
        if not structure[node_to_check]:
            continue
        balance_sheet = {child: sum_of_weighs(structure, weights, child)
                         for child in structure[node_to_check]}
        if len(set(balance_sheet.values())) > 1:
            to_check = sorted(balance_sheet.items(), key=lambda pair: pair[1])
            if to_check[0][1] == to_check[1][1]:
                node_name = to_check[-1][0]
                total_weight = to_check[0][1]
            else:
                node_name = to_check[0][0]
                total_weight = to_check[-1][1]
            return node_name, total_weight - children_weights(structure, weights, node_name)
    raise Exception("No imbalanced node found!")



def prepare_nodes_to_visit(structure: typing.Dict, start_node: str) -> typing.List[str]:
    # we effectively build
    stack = [start_node]
    for child in structure[start_node]:
        stack.extend(prepare_nodes_to_visit(structure, child))
    return stack


def main():
    test_structure, test_weights = data_from_file('test.txt')
    test_root = get_root(test_structure)
    assert test_root == 'tknk'

    structure, weights = data_from_file('data.txt')
    root = get_root(structure)
    print("Problem 1 root:", root)

    test_structure, test_weights = data_from_file('test.txt')
    assert get_unbalanced_node_and_expected_weight(test_structure, test_weights, test_root) == ('ugml', 60)

    print("Problem 2 solution is:", get_unbalanced_node_and_expected_weight(structure, weights, root))


if __name__ == "__main__":
    main()
