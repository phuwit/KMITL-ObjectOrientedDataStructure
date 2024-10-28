'''
Chapter : 11 - item : 2 - Traversals

ส่งมาแล้ว 8 ครั้ง

รับ input เป็น list คู่ตัวเลข(เช่น A B.B C = A ไปหา B ได้ และ B ไปหา C ได้) ให้สร้าง Undirected Graph จากนั้นให้แสดงผล  graph  แบบ Depth First Traversals และ Bredth First Traversals โดยเริ่มต้นที่ vertex ที่น้อยที่สุด

**หมายเหตุ**เนื่องจาก Depth First Traversal อาจมี solutions ที่แตกต่างกันเพื่อให้ได้ solution ที่เหมือนกัน จะกําหนดว่าถ้า traverse ไปได้หลาย node ให่ไป node ที่มีค่าน้อยที่สุดเสมอ

*หากใครงงลองวาดรูปกราฟดูนะครับ*
'''

# nodes: dict[str, list[str]] = {}
nodes = {}

edges_raw = input('Enter : ').split(',')
for edge_raw in edges_raw:
    from_node, to_node = edge_raw.split()
    if from_node not in nodes:
        nodes[from_node] = []
    nodes[from_node].append(to_node)
    if to_node not in nodes:
        nodes[to_node] = []
    nodes[to_node].append(from_node)

sorted_nodes = dict(sorted(nodes.items()))
smallest_vertex = min(nodes.items())[0]
# print(1)

# def breadth_first_traversal(_nodes: dict[str, list[str]], start: str):
def breadth_first_traversal(_nodes, start, history):
    visiting_queue = [start]
    while visiting_queue:
        unconnected_node = visiting_queue.pop(0)
        if unconnected_node in history:
            continue
        history.append(unconnected_node)
        connected_to = _nodes[unconnected_node]
        visiting_queue.extend(sorted(connected_to))

    unconnected_nodes = []
    for node, _ in _nodes.items():
        if node not in history:
            unconnected_nodes.append(node)

    if unconnected_nodes:
        history = breadth_first_traversal(_nodes, sorted(unconnected_nodes)[0], history)

    return history
# print(2)

# def depth_first_traversal(_nodes: dict[str, list[str]], start: str):
def depth_first_traversal(_nodes, start, history):
    visiting_stack = [start]
    while visiting_stack:
        node = visiting_stack.pop()
        if node in history:
            continue
        history.append(node)
        connected_to = _nodes[node]
        visiting_stack.extend(sorted(connected_to, reverse=True))

    unconnected_nodes = []
    for node, _ in _nodes.items():
        if node not in history:
            unconnected_nodes.append(node)

    if unconnected_nodes:
        history = breadth_first_traversal(_nodes, sorted(unconnected_nodes)[0], history)

    return history
# print(3)

depth_first_result = ' '.join(depth_first_traversal(sorted_nodes, smallest_vertex, []))
print(f'Depth First Traversals : {depth_first_result}')
breadth_first_result = ' '.join(breadth_first_traversal(sorted_nodes, smallest_vertex, []))
print(f'Bredth First Traversals : {breadth_first_result}')