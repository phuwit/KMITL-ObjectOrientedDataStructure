"""
Chapter : 5 - item : 2 - รางดาว

ส่งมาแล้ว 0 ครั้ง

ณ เมืองแห่งหนึ่ง ที่มีชื่อว่า ... อืม (เอ้าผู้แต่งโจทย์คิดชื่อไม่ออก เอาเป็นว่าไม่ต้องสนใจก็ได้)

จะมีบริการคมนาคมสาธารณะ ซึ่งเป็นสิ่งที่น้องๆ พี่ๆ อาจารย์ หรือ บุคคลอื่นๆ ที่อาจจะคุณเคยกันหรือเคยนั้งก็มานั้นก็คือ "รถไฟฟ้า" นั้นเอง

โดยแต่ละเมือง จะเปรียบเหมือน Node ของ Linked List ซึ่งรถไฟฟ้าจะมีทั้งขาไปขากลับนั้นเอง และ

รถไฟฟ้าขาไป ผ่านสถานีสุดท้ายของทางรถไฟฟ้าจะวนกลับมาสถานีแรก หรือในทางกลับกัน

รถไฟฟ้าขากลับผ่านสถานีแรกก็จะวนกลับไปสถานีสุดท้ายเช่นกัน

เพื่อให้ "พี่โบ๊ท" ที่เป็นชาวเมืองนี้มีรถไฟฟ้านั้นไปทำงานหรือท่องเทียวในเมืองนี้ได้สะดวกขึ้น

ต่อไปก็เป็นหน้าที่ของน้อง ๆ แล้วล่ะ ที่จะสานฝันให้เมืองนี้และ "พี่โบ๊ท" มี ระบบรถไฟฟ้าที่ "สมบูรณ์แบบ" ที่สร้างขึ้นมาจากน้ำมือของน้องเองๆ


input จะเป็น
บรรทัดแรก จะเป็น list ของ ชื่อสถาณี
บรรทัดสอง จะเป็น สถานีต้นทาง,สถานีปลายทาง,ทิศทางของรถไฟฟ้า(ถ้าไม่ใส่ให้แสดงผลในขาที่ระยะทางสั้นที่สุด ถ้าเกิดเท่ากัน ให้แสดงผลลัพธ์ทั้งขาไปและขากลับ)
โดย F จะเป็น รถไฟฟ้าขาไป
    B จะเป็น รถไฟฟ้าขากลับ
output จะเป็น
แสดงการเดินทางของรถไฟฟ้า,จำนวนสถานีที่จะถึงปลายทาง

***Railway on route***
Input Station name/Source, Destination, Direction(optional): A,B,C,D,E,F,G/C,G
Backward Route: C->B->A->G,3

***Railway on route***
Input Station name/Source, Destination, Direction(optional): A,B,C,D,E,F/B,E
Forward Route: B->C->D->E,3
Backward Route: B->A->F->E,3

***Railway on route***
Input Station name/Source, Destination, Direction(optional): A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T/F,C,F
Forward Route: F->G->H->I->J->K->L->M->N->O->P->Q->R->S->T->A->B->C,17

***Railway on route***
Input Station name/Source, Destination, Direction(optional): A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,AA,AB,AC,AD,AE,AF,AG,AH,AI/Z,AG,B
Backward Route: Z->Y->X->W->V->U->T->S->R->Q->P->O->N->M->L->K->J->I->H->G->F->E->D->C->B->A->AI->AH->AG,28
"""

from base_linked_list import DoublyLinkedList, SinglyLinkedList, DoublyLinkedNode


def get_forward_route(start: DoublyLinkedNode, terminate: DoublyLinkedNode):
    route = SinglyLinkedList()
    current_node = start
    while current_node != terminate:
        if current_node:
            route.append(item=current_node.item)
            current_node = current_node.next
            continue
        break
    route.append(item=current_node.item)
    return route


def get_backward_route(start: DoublyLinkedNode, terminate: DoublyLinkedNode):
    route = SinglyLinkedList()
    current_node = start
    while current_node != terminate:
        if current_node:
            route.append(item=current_node.item)
            current_node = current_node.previous
            continue
        break
    route.append(item=current_node.item)
    return route


print("***Railway on route***")
stations_string, routing_string = input(
    "Input Station name/Source, Destination, Direction(optional): "
).split("/")

routing_data = routing_string.split(",")
routing_direction = None
if len(routing_data) >= 3:
    routing_direction = routing_data.pop()
start_name, terminate_name = routing_data


stations = DoublyLinkedList(circular=True)

for station_name in stations_string.split(","):
    stations.append(item=station_name)

station_start = stations.search(item=start_name)
station_terminate = stations.search(item=terminate_name)


if station_start and station_terminate:
    if routing_direction:
        if routing_direction == "F":
            route = get_forward_route(start=station_start, terminate=station_terminate)
            route_string = str(route).replace(" ", "->")
            route_size = route.size() - 1
            print(f"Forward Route: {route_string},{route_size}")
        elif routing_direction == "B":
            route = get_backward_route(start=station_start, terminate=station_terminate)
            route_string = str(route).replace(" ", "->")
            route_size = route.size() - 1
            print(f"Backward Route: {route_string},{route_size}")

    else:
        forward_route = get_forward_route(
            start=station_start, terminate=station_terminate
        )
        backward_route = get_backward_route(
            start=station_start, terminate=station_terminate
        )

        if forward_route.size() <= backward_route.size():
            route = forward_route
            route_string = str(route).replace(" ", "->")
            route_size = route.size() - 1
            print(f"Forward Route: {route_string},{route_size}")
        if backward_route.size() <= forward_route.size():
            route = backward_route
            route_string = str(route).replace(" ", "->")
            route_size = route.size() - 1
            print(f"Backward Route: {route_string},{route_size}")
