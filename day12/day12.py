import collections

def get_undirected_graph_from_file(filename):
    adj_graph = collections.defaultdict(set)
    with open(filename) as fh:
        for line in fh:
            vertex, adj = parse_line(line)
            adj_graph[vertex].update(adj)
            for v in adj:
                adj_graph[v].add(vertex)
    print(adj_graph)
    return adj_graph

def parse_line(s):
    vertex, adj = s.split("<->")
    return int(vertex), list(map(int, adj.split(',')))

def traverse(adj_graph, vertex):
    visited = [False] * len(adj_graph)
    nodes_to_visit = [vertex]
    while(nodes_to_visit):
        v = nodes_to_visit.pop()
        visited[v] = True
        for adj_node in adj_graph[v]:
            if visited[adj_node]:
                continue
            nodes_to_visit.append(adj_node)
    return [idx for idx, was_visited in enumerate(visited) if was_visited]

def get_connected_components_count(adj_graph):
    # this is fully-fledged graph travelsal solution
    group_number = [False] * len(adj_graph)
    number = 0
    for v in adj_graph:
        if group_number[v]:
            continue
        number += 1
        group_content = traverse(adj_graph, v)
        for vg in group_content:
            group_number[vg] = number
    assert 0 not in group_number
    return max(group_number)

assert(len(traverse(get_undirected_graph_from_file('test.txt'), 0)))  == 6
print("Solution for part 1:", len(traverse(get_undirected_graph_from_file('data.txt'), 0)))
print("Solution for part 2:", get_connected_components_count(get_undirected_graph_from_file('data.txt')))
