"""
Chapter : 5 - item : 3 - Intersection and Swap merge

จากการหา portal ในคราวก่อน น้องๆมอง "เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่" เป็นแค่ประโยคขู่เปล่าๆ ดังนั้นในข้อนี้จึงไม่มีข้อบังคับ แค่แลกมากับความยากนิดหน่อย ใช้ความขี้โกงของ python ให้เต็มที่ พี่ซันฟงไม่ได้ติดในฝัน ไม่มีนิยายให้อ่าน แต่รอบนี้พี่ต้องการโปรแกรมที่มีรายละเอียดดังนี้

Input

การเชื่อมต่อของ node แทนด้วย '>' ซึ่งแต่ละการเชื่อมต่อจะขั้นด้วย ','

รับประกันว่าจะไม่มีการ reassign node.next

หมายถึงจะไม่มี input แบบนี้: 1>2,1>3

Output

แสดงตัว node ที่ linked list เชื่อมเข้าหากัน (เรียงค่าจากน้อยไปมาก)

แสดงค่าและขนาด (ความยาว) ของ node นั้น โดยขนาดนับเริ่มตั้งแต่ตัวมันเองจนถึงตัวสุดท้ายหรือเจอตัวซ้ำ

หากไม่มีให้แสดงว่า "No intersection"

หากมี intersection ให้นำ node ที่เป็น intersection ออกไป แล้วนำ linked list ที่ไม่ใช่ circular มาเรียงใส่สลับกัน

อธิบาย test case 1

Input: 1>2,2>3,6>7,7>3,4>5,3>4

linked list ที่ได้จะมีลักษณะแบบนี้

  6 → 7 ↴
1 → 2 → 3 → 4 → 5

intersection คือ 3

linked list ที่มี 3 เป็น head คือ 3 → 4 → 5

ทำให้ขนาดมีค่าเท่ากับ 3

จึงพิมพ์ Node(3, size=3) ออกมา

ต่อไปนำ node 3 ออกจะได้

  6 → 7 ↴
1 → 2 →   → 4 → 5

นำ linked list มาเรียงใหม่ (เรียงด้วยค่าของ head จากน้อยไปมาก)


Enter edges: 1>2,2>3,6>7,7>3,4>5,3>4
Node(3, size=3)
Delete intersection then swap merge:
1 -> 4 -> 6 -> 2 -> 5 -> 7

Enter edges: 5>2,1>4,2>1,6>7,4>0,7>4,8>2
Node(2, size=4)
Node(4, size=2)
Delete intersection then swap merge:
0 -> 1 -> 5 -> 6 -> 8 -> 7

Enter edges: 5>2,1>4,2>1,6>7,4>0,7>4,8>2,0>5
Node(2, size=5)
Node(4, size=5)
Delete intersection then swap merge:
0 -> 1 -> 6 -> 8 -> 5 -> 7

Enter edges: 4>3,5>6,3>2,6>7,2>1,7>8
No intersection

Enter edges: 5>2,1>4,2>1,6>7,4>0,7>4,8>2,0>1
Node(1, size=3)
Node(2, size=4)
Node(4, size=3)
Delete intersection then swap merge:
0 -> 5 -> 6 -> 8 -> 7

Enter edges: 1>2,2>3,3>4,4>1,8>5,7>8,6>7,5>6,0>9,9>8
Node(8, size=4)
Delete intersection then swap merge:
0 -> 5 -> 9 -> 6 -> 7

Enter edges: 8>8
No intersection

"""

from typing import List, Tuple
from base_linked_list import SinglyLinkedList, SinglyLinkedNode

commands = input("Enter edges: ").split(",")

nodes_details: List[Tuple[int, int]] = []

for command in commands:
    node = (int(node) for node in command.split(">"))
    nodes_details.append(tuple(node))  # type: ignore

print(nodes_details)

first_linked_list = SinglyLinkedList()
sub_linked_lists: List[SinglyLinkedList] = [first_linked_list]
first_node, second_node = nodes_details.pop(0)
first_linked_list.append(first_node)
first_linked_list.append(second_node)

while nodes_details:
    new_list = True
    current_sub_linked_list = sub_linked_lists[-1]
    tail = current_sub_linked_list.peek()
    for sub, node_detail in enumerate(nodes_details):
        if node_detail[0] != tail:
            continue
        current_sub_linked_list.append(node_detail[1])
        nodes_details.pop(sub)
        new_list = False
        break

    if new_list:
        first_linked_list = SinglyLinkedList()
        sub_linked_lists.append(first_linked_list)
        first_node, second_node = nodes_details.pop(0)
        first_linked_list.append(first_node)
        first_linked_list.append(second_node)

tail_search_index = 0

while len(sub_linked_lists) > 1:
    cloned_sub_linked_lists = sub_linked_lists.copy()
    testing_tail_linked_list = cloned_sub_linked_lists.pop(tail_search_index)
    tail_item = testing_tail_linked_list.peek()
    for sub in cloned_sub_linked_lists:
        if sub.search(tail_item):
            i = sub.get_index(sub.search(tail_item).item)
            pre_junction = sub.search(sub.peek(i - 1))
            if isinstance(pre_junction, SinglyLinkedNode):
                pre_junction.next = testing_tail_linked_list.head
            junction = sub.search(sub.peek(i))
            sub.pop(i)
            print(f"Node({i}, size={testing_tail_linked_list.size() + 1})")
            if isinstance(junction, SinglyLinkedNode) and isinstance(
                junction.next, SinglyLinkedNode
            ):
                next_node = testing_tail_linked_list.search(
                    testing_tail_linked_list.peek()
                )
                junction.next.next = next_node
            tail_search_index = -1
            sub_linked_lists.pop(tail_search_index)
            break
        continue

    if tail_search_index == -1:
        tail_search_index = 0
        continue
    else:
        tail_search_index += 1


print([str(i) for i in sub_linked_lists])
