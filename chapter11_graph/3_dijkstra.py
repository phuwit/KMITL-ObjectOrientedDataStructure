"""
Chapter : 11 - item : 3 - shortest path

ส่งมาแล้ว 18 ครั้ง

รับ input เป็น list คู่อันดับ เพื่อนำไปสร้าง Directed Graph แบบมี weight จากนั้นให้แสดงผล shortest path โดยใช้ Dijkstra’s Shortest Path Algorithm

เช่น A 3 B,B 1 C/A B,A C = สร้างกราฟที่ A ไปหา B ได้โดยมีweight=3 และ B ไปหา C ได้โดยมีweight=1 / แสดง shortest path จากA>BและA>C)
"""
# weighted_nodes: dict[str, dict[str, int]] = {}

weighted_nodes = {}

edges_raw, queries_raw = input("Enter : ").split("/")
for edge_raw in edges_raw.split(","):
    from_node, weight, to_node = edge_raw.split()
    weight = int(weight)

    if from_node not in weighted_nodes:
        weighted_nodes[from_node] = {}
    weighted_nodes[from_node][to_node] = weight
    # if to_node not in weighted_nodes:
    #     weighted_nodes[to_node] = {}
    # weighted_nodes[to_node][from_node] = weight

sorted_weighted_nodes = dict(sorted(weighted_nodes.items()))
smallest_vertex = min(weighted_nodes.items())[0]


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
        except KeyError:
            continue

        for destination, edge_weight in edges.items():
            accumulated_weight, _ = dijkstra[source]
            if destination == start:
                continue
            if destination not in history:
                visit_queue.add(destination)

            accumulated_weight += edge_weight
            if destination not in dijkstra:
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


# # def find_path(paths: dict[str, tuple[int, str]], source: str, destination: str):
# def find_path(paths, source, destination):
#     cost = 0
#     history = []
#     current_node = destination
#     while current_node != source:
#         history.append(current_node)
#         path_weight, next_node  = paths[current_node]
#         if path_weight == 0:
#             raise AttributeError
#         cost += path_weight
#         current_node = next_node
#         # print(current_node, cost)
#         continue
#     history.append(source)
#     return history, cost

# print(dijkstra_paths)

for query_raw in queries_raw.split(","):
    from_node, to_node = query_raw.split()

    # try:
    #     if to_node in weighted_nodes[from_node]:
    #         print(f'{from_node} to {to_node} : {from_node}->{to_node}')
    #         continue
    # except KeyError:
    #     pass

    dijkstra_paths = generate_dijkstra(weighted_nodes, from_node)
    path = get_path(dijkstra_paths, to_node)
    if not path:
        print(f"Not have path : {from_node} to {to_node}")
        continue

    formatted_path = "->".join(path[::-1])
    print(f"{from_node} to {to_node} : {formatted_path}")
