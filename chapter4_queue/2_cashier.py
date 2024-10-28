"""
Chapter : 4 - item : 2 - คอยนาน

จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด

Testcase : #1 1
Enter people : Lorem_Ipsum
1 ['o', 'r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L'] []
2 ['r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o'] []
3 ['e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o', 'r'] []
4 ['m', '_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e'] []
5 ['_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm'] []
6 ['I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm', '_'] []
7 ['p', 's', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] []
8 ['s', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p']
9 ['u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p', 's']
10 ['m'] ['e', 'm', '_', 'I', 'u'] ['s']
11 [] ['e', 'm', '_', 'I', 'u'] ['s', 'm']

Testcase : #2 2
Enter people : JUST_DO_IT!!!!
1 ['U', 'S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J'] []
2 ['S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U'] []
3 ['T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U', 'S'] []
4 ['_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T'] []
5 ['D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_'] []
6 ['O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_', 'D'] []
7 ['_', 'I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] []
8 ['I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_']
9 ['T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_', 'I']
10 ['!', '!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I']
11 ['!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I', '!']
12 ['!', '!'] ['T', '_', 'D', 'O', 'T'] ['!', '!']
13 ['!'] ['_', 'D', 'O', 'T', '!'] ['!', '!']
14 [] ['_', 'D', 'O', 'T', '!'] ['!', '!']

Testcase : #3 3
Enter people : A_is_stand_for_amazing
1 ['_', 'i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A'] []
2 ['i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_'] []
3 ['s', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_', 'i'] []
4 ['_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's'] []
5 ['s', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_'] []
6 ['t', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_', 's'] []
7 ['a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] []
8 ['n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a']
9 ['d', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a', 'n']
10 ['_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n']
11 ['f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n', '_']
12 ['o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['_', 'f']
13 ['r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['_', 'f']
14 ['_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r']
15 ['a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r', '_']
16 ['m', 'a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_']
17 ['a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_', 'm']
18 ['z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['_', 'm', 'a']
19 ['i', 'n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['_', 'm', 'a']
20 ['n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i']
21 ['g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i', 'n']
22 [] ['d', 'o', 'a', 'z', 'g'] ['a', 'i', 'n']
"""


class Queue:
    def __init__(self, items) -> None:
        self.__queue = items

    def dequeue(self):
        return self.__queue.pop(0)

    def enqueue(self, item):
        self.__queue.append(item)

    def get_queue(self):
        return self.__queue

    def length(self):
        return len(self.__queue)

    def __str__(self) -> str:
        return self.__queue.__str__()


class Cashier:
    def __init__(self, queue, processing_time, max_queue_length) -> None:
        self.__queue = queue
        self.__processing_time = processing_time
        self.__max_queue_length = max_queue_length
        self.__last_added_timestamp = 0
        self.__current_process_tick = 0

    def get_queue(self):
        return self.__queue

    def set_queue(self, queue, timestamp):
        self.__queue = queue
        self.__last_added_timestamp = timestamp

    def get_processing_time(self):
        return self.__processing_time

    def get_max_queue_length(self):
        return self.__max_queue_length

    def get_last_added_timestamp(self):
        return self.__last_added_timestamp

    def process(self, timestamp):
        if (
            self.__current_process_tick < self.__processing_time
            and self.get_queue().length()
        ):
            self.__current_process_tick += 1
        else:
            if self.__queue.length():
                self.__queue.dequeue()
            self.__current_process_tick = 1


input_string = input("Enter people : ")
characters = list(char for char in input_string)

main_queue = Queue(characters)
cashier1 = Cashier(Queue([]), 3, 5)
cashier2 = Cashier(Queue([]), 2, 5)

for timestamp in range(main_queue.length()):
    character = main_queue.dequeue()

    # if not cashier1_processed:
    cashier1.process(timestamp)
    # if not cashier2_processed:
    cashier2.process(timestamp)

    if cashier1.get_queue().length() < cashier1.get_max_queue_length():
        cashier1.get_queue().enqueue(character)
    elif cashier2.get_queue().length() < cashier2.get_max_queue_length():
        cashier2.get_queue().enqueue(character)

    print(f"{timestamp + 1} {main_queue} {cashier1.get_queue()} {cashier2.get_queue()}")
