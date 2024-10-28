'''
Chapter : 11 - item : 1 - ฝึกสร้าง graph

ส่งมาแล้ว 2 ครั้ง

รับ input เป็น list คู่อันดับ(เช่น A B,B C = A ไปหา B ได้ และ B ไปหา C ได้) ให้สร้าง Directed Graph จากนั้นให้แสดงผล adjacency metrix ของ graph
'''

nodes = set()
edges = []

edges_raw = input('Enter : ').split(',')
for edge_raw in edges_raw:
    from_node, to_node = edge_raw.split()
    edges.append((from_node, to_node))
    nodes.add(from_node)
    nodes.add(to_node)

sorted_nodes = sorted(nodes)

def create_adjacency_matrix(_nodes, _edges):
    adjacency_matrix = [['0' for _ in range(len(_nodes))] for _ in range(len(_nodes))]

    for _from_node, _to_node in _edges:
        y = sorted_nodes.index(_from_node)
        x = sorted_nodes.index(_to_node)
        adjacency_matrix[y][x] = '1'

    return adjacency_matrix

def print_adjacency_matrix(_nodes, _adjacency_matrix):
    nodes_string = '  '.join(_nodes)
    print(f'    {nodes_string}')
    for index, node in enumerate(_nodes):
        adjacency = ', '.join(_adjacency_matrix[index])
        print(f'{node} : {adjacency}')

print_adjacency_matrix(sorted_nodes, create_adjacency_matrix(sorted_nodes, edges))
