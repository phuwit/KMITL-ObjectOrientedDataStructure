"""
Chapter : 4 - item : 5 - Search Portal

พี่ซันฟงได้รับคำสั่งจากอาจารย์ให้ออกโจทย์เขียนโปรแกรมให้แก่น้องๆ พี่จึงกลับไปนอนคิดที่บ้าน รู้สึกตัวอีกทีก็อยู่ในห้องมืดๆ พี่สามารถมองเห็นและเดินไปยังพื้นที่ที่อยู่ติดกันได้ (4 ทิศ เหนือ ใต้ ออก ตก) พี่จะต้องหาประตูทางออกจากฝันเพื่อไปส่งโจทย์ให้กับอาจารย์ ต่อมาพี่ก็คิดวิธีในการเดินหาประตูทางออกได้โดยใช้วิธีหาแบบ Breadth First Search โดยพี่จะเริ่มยืนในจุดเริ่มต้นแล้วมองหาและจำทางเริ่มจากทิศเหนือ ทิศตะวันออก ทิศใต้ ทิศตะวันตก ตามลำดับ แล้วเดินไปยังช่องถัดไปแล้วหาใหม่ ในเมื่อคิดวิธีออกแล้วพี่จึงต้องการโปรแกรมที่จะบอกพี่ว่าสามารถไปถึงทางออกได้หรือพี่จะต้องติดอยู่ในฝันไปตลอดกาล ปัญหาคือพี่ขี้เกียจเขียนโค้ด พี่เลยอยากให้น้องๆเขียนโค้ดให้พี่หน่อย เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่
โดยรายละเอียดโปรแกรมจะมีดังนี้
Input
รับความกว้าง ความสูง และแผนที่ โดยแผนที่แต่ละบรรทัดจะขั้นด้วย ','
ตัวอย่าง input: 3 3 F__,##_,O__
จะมีความหมายว่าแผนที่กว้าง 3 สูง 3 และแผนที่จะเป็นแบบนี้
F__
##_
O__
ภายในแผนที่

    'F' แทนตำแหน่งเริ่มต้นของพี่
    'O' แทนประตูทางออก
    '_' แทนพื้นที่ที่สามารถเดินได้
    ตัวอักษรอื่นๆทั้งหมดแทนกำแพง ไม่สามารถเดินไปที่ช่องนั้นได้

Output
หากไม่มีพี่ (F) อยู่ในห้องหรือแผนที่ที่ใส่เข้ามาไม่ตรงกับขนาดของ width ให้แสดงว่า "Invalid map input."
แสดง queue ระหว่างหาทางออก
ถ้าหาทางออกเจอให้แสดงว่า "Found the exit portal."
ถ้าหาไม่เจอให้แสดงว่า "Cannot reach the exit portal."

F__###
##_###
##__##
###__O
Enter width, height, and room: 6 4 F__###,##_###,##__##,###__O
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(2, 1)]
Queue: [(2, 2)]
Queue: [(3, 2)]
Queue: [(3, 3)]
Queue: [(4, 3)]
Found the exit portal.

########
##___###
##_F_###
##____##
##_##_O_
##______
Enter width, height, and room: 8 6 ########,##___###,##_F_###,##____##,##_##_O_,##______
Queue: [(3, 2)]
Queue: [(3, 1), (4, 2), (3, 3), (2, 2)]
Queue: [(4, 2), (3, 3), (2, 2), (4, 1), (2, 1)]
Queue: [(3, 3), (2, 2), (4, 1), (2, 1), (4, 3)]
Queue: [(2, 2), (4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(4, 1), (2, 1), (4, 3), (2, 3)]
Queue: [(2, 1), (4, 3), (2, 3)]
Queue: [(4, 3), (2, 3)]
Queue: [(2, 3), (5, 3)]
Queue: [(5, 3), (2, 4)]
Queue: [(2, 4), (5, 4)]
Queue: [(5, 4), (2, 5)]
Found the exit portal.

Enter width, height, and room: 3 3 ###,######F,###
Invalid map input.

Enter width, height, and room: 3 3 F__,##_,O_
Invalid map input.

Enter width, height, and room: 1 1 F
Queue: [(0, 0)]
Cannot reach the exit portal.

Enter width, height, and room: 2 1 FO
Queue: [(0, 0)]
Found the exit portal.

__|__
F_|_O
__|__
Enter width, height, and room: 5 3 __|__,F_|_O,__|__
Queue: [(0, 1)]
Queue: [(0, 0), (1, 1), (0, 2)]
Queue: [(1, 1), (0, 2), (1, 0)]
Queue: [(0, 2), (1, 0), (1, 2)]
Queue: [(1, 0), (1, 2)]
Queue: [(1, 2)]
Cannot reach the exit portal.

F_____\\...
===\\___\\..
...#\\___\\.
....#|___|
...#/___/.
===/___/..
O_____/...
Enter width, height, and room: 10 7 F_____\\...,===\\___\\..,...#\\___\\.,....#|___|,...#/___/.,===/___/..,O_____/...
Queue: [(0, 0)]
Queue: [(1, 0)]
Queue: [(2, 0)]
Queue: [(3, 0)]
Queue: [(4, 0)]
Queue: [(5, 0), (4, 1)]
Queue: [(4, 1), (5, 1)]
Queue: [(5, 1)]
Queue: [(6, 1), (5, 2)]
Queue: [(5, 2), (6, 2)]
Queue: [(6, 2)]
Queue: [(7, 2), (6, 3)]
Queue: [(6, 3), (7, 3)]
Queue: [(7, 3), (6, 4)]
Queue: [(6, 4), (8, 3), (7, 4)]
Queue: [(8, 3), (7, 4), (6, 5), (5, 4)]
Queue: [(7, 4), (6, 5), (5, 4)]
Queue: [(6, 5), (5, 4)]
Queue: [(5, 4), (5, 5)]
Queue: [(5, 5)]
Queue: [(5, 6), (4, 5)]
Queue: [(4, 5), (4, 6)]
Queue: [(4, 6)]
Queue: [(3, 6)]
Queue: [(2, 6)]
Queue: [(1, 6)]
Found the exit portal.
"""

START_SYMBOL = "F"
EXIT_SYMBOL = "O"
PATH_SYMBOL = "_"


class Coord:
    def __init__(self, _y, _x):
        self.y = _y
        self.x = _x

    def get_tuple(self):
        return (self.x, self.y)

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False


class Queue:
    def __init__(self, items):
        self.__queue = items

    def dequeue(self):
        return self.__queue.pop(0)

    def enqueue(self, item):
        self.__queue.append(item)

    def get_queue(self):
        return self.__queue

    def length(self):
        return len(self.__queue)

    def __str__(self):
        return str([item.get_tuple() for item in self.__queue])


def validate_input(_room, _width, _height):
    if len(_room) != _height:
        return None

    for row in _room:
        if len(row) != _width:
            return None

    coords = None

    for i, row in enumerate(_room):
        if coords:
            break
        for j, cell in enumerate(row):
            if cell == START_SYMBOL:
                coords = Coord(i, j)
                break

    if not coords:
        return None

    return coords


def get_nearby_coords(_coord, room_width, room_height):
    _north = Coord(_coord.y - 1, _coord.x)
    _east = Coord(_coord.y, _coord.x + 1)
    _south = Coord(_coord.y + 1, _coord.x)
    _west = Coord(_coord.y, _coord.x - 1)

    nearby = [_north, _east, _south, _west]
    sanitized_nearby = []

    for item in nearby:
        if item.y >= room_height or item.x >= room_width:
            continue
        elif item.y < 0 or item.x < 0:
            continue
        sanitized_nearby.append(item)

    return sanitized_nearby


def check_coord(_room, _width, _height, _coord):
    if _coord.y >= _height or _coord.x >= _width:
        return None
    elif _room[_coord.y][_coord.x] == EXIT_SYMBOL:
        return True
    elif _room[_coord.y][_coord.x] == PATH_SYMBOL:
        return False
    return None


width_string, height_string, room_data = input(
    "Enter width, height, and room: "
).split()

# width_string, height_string, room_data = '6 4 F__###,##_###,##__##,###__O'.split()

width = int(width_string)
height = int(height_string)

room = room_data.split(",")

start_coords = validate_input(room, width, height)
if not start_coords:
    print("Invalid map input.")
    exit()

visiting_queue = Queue([start_coords])
visited_coords = []
exit_coords = None

# while not exit_coords:
while visiting_queue.length():
    print(f"Queue: {str(visiting_queue)}")
    search_target = visiting_queue.dequeue()
    for coord in get_nearby_coords(search_target, width, height):
        if coord in visited_coords:
            continue

        visited_coords.append(coord)

        result = check_coord(room, width, height, coord)
        if result is True:
            print("Found the exit portal.")
            exit()
        elif result is False:
            visiting_queue.enqueue(coord)

print("Cannot reach the exit portal.")
