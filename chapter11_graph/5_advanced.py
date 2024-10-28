# def generate_dijkstra(nodes: dict[str, dict[str, int]], start: str):
def generate_dijkstra(nodes, start):
    dijkstra: dict[str, tuple[int, str]] = {start: (0, start)}
    visit_queue = set()
    visit_queue.add(start)
    history = set()

    while visit_queue:
        # print(visit_queue)
        source = visit_queue.pop()
        history.add(source)
        try:
            edges = nodes[source]
            source_weight, _ = dijkstra[source]
        except KeyError:
            continue

        for destination, edge_weight in edges.items():
            if destination == start:
                continue
            if destination not in history:
                visit_queue.add(destination)

            accumulated_weight = source_weight + edge_weight
            if not destination in dijkstra:
                dijkstra[destination] = (accumulated_weight, source)
                continue

            saved_weight, _ = dijkstra[destination]
            if accumulated_weight < saved_weight:
                dijkstra[destination] = (accumulated_weight, source)
                continue
        # print(source, dijkstra)

    visit_queue = set()
    visit_queue.add(start)
    history = set()

    while visit_queue:
        # print(visit_queue)
        source = visit_queue.pop()
        history.add(source)
        try:
            edges = nodes[source]
            source_weight, _ = dijkstra[source]
        except KeyError:
            continue

        for destination, edge_weight in edges.items():
            if destination == start:
                continue
            if destination not in history:
                visit_queue.add(destination)

            accumulated_weight = source_weight + edge_weight
            if not destination in dijkstra:
                dijkstra[destination] = (accumulated_weight, source)
                continue

            saved_weight, _ = dijkstra[destination]
            if accumulated_weight < saved_weight:
                dijkstra[destination] = (accumulated_weight, source)
                continue
        # print(source, dijkstra)

    return dijkstra


# def get_path(paths: dict[str, tuple[int, str]], destination: str):
def get_path(paths, destination):
    history = []
    current_node = destination
    while current_node:
        try:
            path_weight, next_node = paths[current_node]
        except KeyError:
            break
        history.append(current_node)
        if path_weight == 0:
            break
        current_node = next_node
        # print(current_node, cost)
        continue
    return history


# weighted_nodes: dict[str, dict[str, int]] = {}
weighted_nodes = {
    "A": {"B": 1, "C": 2},
    "B": {"D": 12, "A": 1},
    "C": {"D": 9, "F": 3, "A": 2},
    "D": {"C": 9, "E": 7, "G": 1},
    "E": {"G": 5, "D": 7},
    "F": {"G": 4},
    "G": {"D": 1, "E": 5, "F": 4},
}

print(" *** Dijkstra's shortest path ***")
query_raw = input("Enter start and target vertex : ")

from_node, to_node = query_raw.split()

dijkstra_paths = generate_dijkstra(weighted_nodes, from_node)
path = get_path(dijkstra_paths, to_node)[::-1]
distance, _ = dijkstra_paths[to_node]

print(f"Shortest distance is {distance}")
print(f"And the path is {path}")
