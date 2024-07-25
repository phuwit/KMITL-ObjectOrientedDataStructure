'''
Chapter : 5 - item : 5 - แม่งูเอ๋ย กินน้ำบ่อไหน?

เเม่งูเอ๋ยกินน้ำบ่อไหน กินน้ำบ่อทราย ย้ายไปก็ย้ายมา~

แม่งูต้องการสอนลูกงูเล่นให้รู้จักกับ linked-list โดยทำการนัดกับพ่องูให้เล่นเกมงูกินหางด้วยกัน โดยแม่งูจะเรียกลูกงูให้มาเกาะแม่งูกันเป็นเส้นตรง และให้งูทุกตัวแสดงน้ำหนักตัวเอง (แม่งูจะอยู่หัวเสมอ) ต่อมาแม่งูได้สอนการละเล่นงูกินหาง ให้ลูกงูดังนี้

ถ้าพ่องูร้องว่า “กินน้ำบ่อไหน” และถ้าแม่งูตอบว่า

    “กินน้ำบ่อทราย ย้ายไปก็ย้ายมา”

เมื่อลูกงูได้ยินคำสั่ง “ย้ายไปก็ย้ายมา” ให้ลูกงูที่เกาะเเม่งูอยู่นั้นสลับตำแหน่งเลขคู่เลขคี่กัน (1->2, 2->1) (ระวังลูกงูสับสน)

    “กินน้ำบ่อโศก โยกไปก็โยกมา”

เมื่อลูกงูได้ยินคำสั่ง “โยกไปก็โยกมา”  ให้ลูกงูโยก แต่เผอิญว่าแม่งูก็โยกเช่นกัน และโยกแรงเกิน ทำให้ลูกงูที่มีขนาดเล็กกว่าแม่งูนั้นหลุดออกจากวงไป โดยลูกงูที่หลุดออกจากขบวน จะมานั่งดูแม่งูและลูกคนอื่นๆเล่นเกมต่อไป (แสดงตัวเลขที่หลุดออกจาก  linked-list)

    “กินน้ำบ่อหิน บินไปก็บินมา”

“บินไปก็บินมา” เป็นคำสั่งที่ให้แม่งูติดปีกบินไปขโขยลูกงูชาวบ้านมา โดยลูกงูที่แม่งูขโมยมาให้ไปต่อท้ายลูกงูตัวสุดท้ายในขบวนตลอด (แสดงตัวเลขที่แม่งูไปขโมยมาด้วย)

    “กินหัวกินหาง กินกลางตลอดตัว”

“กินกลางตลอดตัว” เป็นคำสั่งที่ให้แม่งูและลูกงูเตรียมพร้อมรับแรงกระแทกจากพ่องู

    โดยหากน้ำหนักของแม่งูและลูกงูรวมกันน้อยกว่าพ่องู แม่งูต้องเสียลูกงูจนกว่า พ่องูจะเจอลูกงูที่มีขนาดที่หารขนาดพ่องูลงตัว (ขนาดพ่องู mod ขนาดลูกงู = 0)

    แต่หากไม่มีลูกงูตัวไหนที่หารน้ำหนักพ่องูได้เลย แม่งูจึงตัดสินใจสลับหัว-หางกับลูกตัวเอง

(0 เป็นลูกรัก แม่งูจะไม่ให้ตัวนี้ไปหารกับพ่องูเด็ดขาด)

	โดยลูกงูที่หลุดออกจากขบวน จะมานั่งดูแม่งูและลูกคนอื่นๆเล่นเกมต่อไป (แสดงตัวเลขที่หลุดออกจาก  linked-list)

แม่งูจะตายหากไม่มีลูกงูเกาะแม่งูอยู่เลย แม้ว่าคำสั่งต่อมาจะบอกให้แม่งูบินไปขโมยลูกงูมาก็ตาม

คำสั่ง:

- บันทัดแรกแรกจะเป็นการรับตัวเลขเพื่อสร้างครอบครัวงู และรับคำสั่ง

เช่น 	Snake family : 10 9 8 7 (แม่งูคือ 10, และมีลูกงูได้แก่ 9 8 7)

	(10)->9->8->7

- บรรทัดต่อมาจะเป็นการรับคำสั่ง โดย

“ย้ายไปก็ย้ายมา” : SW

“โยกไปก็โยกมา” : SH

“บินไปก็บินมา” : F <input>

“กินกลางตลอดตัว” : D <input>

เช่น 	Snake Game : 10 9 8 7/D 7,SH,SW,F 8

	(10)->9->8->7 (แม่งูคือ 10, และมีลูกงูได้แก่ 9 8 7)

จะเป็นการเล่นกับพ่องูที่มีขนาดเท่ากับ 7, แม่งูโยก, ลูกสลับตำแหน่ง, แม่งูขโมยลูกงูที่มีขนาด 8 ตามลำดับ

Snake Game : 10 9 8 7/D 7,SH,SW,F 8
(10)->9->8->7
Play success!->[]
(10)->9->8->7
------------------------------
Shake success!->[]
(10)->9->8->7
------------------------------
Swap success!
(10)->8->9
------------------------------
Steal success!->8
(10)->8->9->8
------------------------------
Snake Game :

Snake Game : 5 1 2 3 4 5 6 7 8 9 10/SW,SH,F 4,D 63
(5)->1->2->3->4->5->6->7->8->9->10
Swap success!
(5)->2->1->4->3->6->5->8->7->10->9
------------------------------
Shake success!->[6, 8, 7, 10, 9]
(5)->2->1->4->3->5
------------------------------
Steal success!->4
(5)->2->1->4->3->5->4
------------------------------
Play success!->[5, 4]
(5)->2->1->4->3
------------------------------
Snake Game :

Snake Game : 10 5 7 3/SH,SH,SW,SW,D 44
(10)->5->7->3
Shake success!->[]
(10)->5->7->3
------------------------------
Shake success!->[]
(10)->5->7->3
------------------------------
Swap success!
(10)->7->5
------------------------------
Swap success!
(10)->5->7
------------------------------
Play success!->[]
(7)->5->10
------------------------------
Snake Game :

Snake Game : 1 2 3/SH,D 99,SW
(1)->2->3
Shake success!->[2, 3]
(1)->Empty
------------------------------
Mom is dead
Snake Game :

Snake Game : 4 0 0/F 8,F 7,F 6,D 71,D 122,D 77,D 88,SW,D 31
(4)->0->0
Steal success!->8
(4)->0->0->8
------------------------------
Steal success!->7
(4)->0->0->8->7
------------------------------
Steal success!->6
(4)->0->0->8->7->6
------------------------------
Play success!->[]
(6)->0->0->8->7->4
------------------------------
Play success!->[]
(4)->0->0->8->7->6
------------------------------
Play success!->[6]
(4)->0->0->8->7
------------------------------
Play success!->[7]
(4)->0->0->8
------------------------------
Swap success!
(4)->0->0
------------------------------
Play success!->[]
(0)->0->4
------------------------------
Snake Game :

Snake Game : -4 -3 -2 -1 0/SW,F 0,F 0,F 0,D 0,D 0,SW,SH
(-4)->-3->-2->-1->0
Swap success!
(-4)->-2->-3->0->-1
------------------------------
Steal success!->0
(-4)->-2->-3->0->-1->0
------------------------------
Steal success!->0
(-4)->-2->-3->0->-1->0->0
------------------------------
Steal success!->0
(-4)->-2->-3->0->-1->0->0->0
------------------------------
Play success!->[0, 0, 0]
(-4)->-2->-3->0->-1
------------------------------
Play success!->[]
(-4)->-2->-3->0->-1
------------------------------
Swap success!
(-4)->-3->-2->-1->0
------------------------------
Shake success!->[-3, -2, -1, 0]
(-4)->Empty
------------------------------
Mom is dead
Snake Game :

Snake Game : 7 8 9/F 10,SW,SW,SH
(7)->8->9
Steal success!->10
(7)->8->9->10
------------------------------
Swap success!
(7)->9->8
------------------------------
Swap success!
(7)->8->9
------------------------------
Shake success!->[8, 9]
(7)->Empty
------------------------------
Mom is dead
Snake Game :

Snake Game : 9 9 9 9 9/SH,F -100,D 101,D -40,F -100,SW,SH,D -20,SH,SW
(9)->9->9->9->9
Shake success!->[]
(9)->9->9->9->9
------------------------------
Steal success!->-100
(9)->9->9->9->9->-100
------------------------------
Play success!->[]
(-100)->9->9->9->9->9
------------------------------
Play success!->[]
(9)->9->9->9->9->-100
------------------------------
Steal success!->-100
(9)->9->9->9->9->-100->-100
------------------------------
Swap success!
(9)->9->9->9->9->-100->-100
------------------------------
Shake success!->[]
(9)->9->9->9->9->-100->-100
------------------------------
Play success!->[]
(-100)->9->9->9->9->-100->9
------------------------------
Shake success!->[9, 9, 9, 9, 9]
(-100)->-100
------------------------------
Swap success!
(-100)->Empty
------------------------------
Mom is dead
Snake Game :
'''

class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

alive = True

class Snake:
    global alive

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyLinkedNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node
        new_node.previous = cur_node
        self.tail = new_node

    def swap_nodes(self, node1, node2):
        if node1.data == node2.data:
            return

        prev1, next1 = node1.previous, node1.next
        prev2, next2 = node2.previous, node2.next


        node1.previous = node2
        node1.next = next2
        node2.previous = prev1
        node2.next = node1

        if prev1:
            prev1.next = node2
        else:
            self.head = node2

        if next2:
            next2.previous = node1
        else:
            self.tail = node1

    def swap_odd_even(self):
        if not self.head or not self.head.next:
            return

        if not self.head.next.next:
            self.delete_node(self.head.next)

        mom = self.head
        current = mom.next

        while current and current.next:
            new_current = current.next.next
            self.swap_nodes(current, current.next)
            current = new_current
            if not current:
                print("Swap success!")
                return
            if not current.next:
                prev_node = current.previous
                prev_node.next = None
                self.tail = prev_node

        print("Swap success!")

    def dad(self, number):
        mom = self.head
        current = mom.next
        width = mom.data

        while current:
            width += current.data
            current = current.next

        if number == 0:
            result = []
            current = self.tail
            while current.previous:
                pre_node = current.previous
                if current.data == 0:
                    result.append(0)
                    self.delete_node(current)
                else:
                    print(f'Play success!->{result}')
                    return
                current = pre_node

        if width < number:
            current = self.tail
            nodes = []
            result = []
            while current.previous:
                prev_node = current.previous
                if current.data == 0 and number != 0:
                    nodes.append(current)
                elif number % current.data == 0:
                    for i in nodes:
                        self.delete_node(i)
                        result.append(i.data)
                    result.reverse()
                    print(f'Play success!->{result}')
                    return
                else:
                    nodes.append(current)
                current = prev_node

            print("Play success!->[]")
            self.swap_head_tail()
        else:
            print("Play success!->[]")
            return

    def swap_head_tail(self):
        if not self.head.next:
            return

        if self.head.next == self.tail:
            head = self.head
            tail = self.tail
            self.swap_nodes(head, tail)
            return

        head, previous1, next1 = self.head, self.head.previous, self.head.next
        tail, previous2, next2 = self.tail, self.tail.previous, self.tail.next

        self.head = tail
        self.tail = head

        self.head.previous = previous1
        self.head.next = next1
        next1.previous = self.head

        self.tail.previous = previous2
        self.tail.next = next2
        previous2.next = self.tail

    def shake(self):
        mom = self.head
        current = mom.next
        result = []
        while current:
            next_node = current.next
            if current.data > mom.data:
                result.append(current.data)
                self.delete_node(current)
            current = next_node
        print(f'Shake success!->{result}')

    def steal(self, number):
        self.append(number)
        print(f"Steal success!->{number}")

    def delete_node(self, node):
        if not node:
            return

        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
            return

        if node == self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return

        node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous

    def __str__(self):
        global alive
        if not self.head:
            return "List is empty"

        mom = self.head
        current_child = mom.next
        _list = []

        while current_child:
            _list.append(str(current_child.data))
            current_child = current_child.next
        if not _list:
            alive = False
        return f'({mom.data})->{"->".join(_list)}' if _list else f'({mom.data})->Empty'

snake = Snake()

command_string = input("Snake Game : ").split(",")
snake_data = command_string[0].split("/")

command_string.pop(0)
command_string.insert(0, snake_data[1])
snake_data = snake_data[0].split()

for i in snake_data:
    snake.append(int(i))

print(snake)

for i in command_string:
    command = i.split()
    action = command.pop(0)
    if not alive:
        break
    elif action == "SW":
        snake.swap_odd_even()
    elif action == "SH":
        snake.shake()
    elif action == "F":
        snake.steal(int(command.pop()))
    elif action == "D":
        snake.dad(int(command.pop()))
    print(snake)
    print("------------------------------")

if not alive:
    print("Mom is dead")
print("Snake Game : ")