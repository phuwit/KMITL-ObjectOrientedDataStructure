user_input = input('Enter edges: ').split(',')
edges = {}
reverse_edges = {}

for edge_input in user_input:
    start, end = map(int, edge_input.split('>'))
    edges.setdefault(start, []).append(end)
    reverse_edges.setdefault(end, []).append(start)

isolated_nodes = [node for node in reverse_edges if node not in edges]
intersection_nodes = [node for node, starts in reverse_edges.items() if len(starts) > 1]

if not intersection_nodes:
    print('No intersection')
    exit()

intersection_nodes.sort()

for node in intersection_nodes:
    current_node = node
    path_length = 1
    visited = {node}
    while node in edges:
        node = edges[node][0]
        if node in visited:
            break
        visited.add(node)
        path_length += 1
    print(f'Node({current_node}, size={path_length})')

print('Delete intersection then swap merge:')
edges = {k: v for k, v in edges.items() if k not in intersection_nodes}

paths = []
for start, ends in edges.items():
    end = ends[0]
    for path in paths:
        if end == path[0][0]:
            path.insert(0, (start, end))
            break
        if start == path[-1][1]:
            path.append((start, end))
            break
    else:
        paths.append([(start, end)])

valid_paths = []
for path in paths:
    seen = set()
    for start, end in path:
        if end in seen:
            break
        seen.add(start)
    else:
        valid_paths.append(path)

for node in isolated_nodes:
    if node in intersection_nodes:
        continue
    for path in valid_paths:
        if node == path[-1][1]:
            path.append((node, None))
            break
    else:
        valid_paths.append([(node, None)])

valid_paths.sort(key=lambda path: path[0][0])
max_length = max(len(path) for path in valid_paths)
ordered_nodes = [str(path[index][0]) for index in range(max_length) for path in valid_paths if index < len(path)]
print(' -> '.join(ordered_nodes))