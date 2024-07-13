'''
Chapter : 4 - item : 4 - Canteen

โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก


Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,D,D
Empty
101
201

Enter Input : 1 101,1 102,2 201,2 202/D,E 101,E 201,E 102,D,D,D,D
Empty
101
102
201
Empty

Enter Input : 1 41,1 42,1 43,2 201,2 202,2 203/E 41,E 201,D,E 202,E 42,E 43,D,E 203,D,D,D
41
201
202
203
42

Enter Input : 1 41,1 42,1 43,2 201,2 202,2 203,3 301,3 302,3 303/D,E 41,E 201,E 42,D,D,E 43,E 303,E 41,E 202,E 302,D,D,D,D,D,D,D
Empty
41
42
201
202
43
41
303
302
Empty

Enter Input : 1 41,1 42,1 43,2 201,2 202,2 203,3 301,3 302,3 303/D,E 41,E 201,E 42,D,D,E 43,E 303,E 41,E 202,E 302,D,D,D,D,D,D,D,E 301,E 302,E 43,E 42,E 201,E 202,D,E 303,D,D,D,D,D,E 303,D,D,D
Empty
41
42
201
202
43
41
303
302
Empty
301
302
303
43
42
201
202
303
Empty

'''


class Queue:
    def __init__(self, items) -> None:
        self.__queue = items

    def dequeue(self):
        return self.__queue.pop(0)

    def enqueue(self, item):
        self.__queue.append(item)

    def get_queue(self):
        return self.__queue

    def set_queue(self, queue):
        self.__queue = queue

    def length(self):
        return len(self.__queue)

    def __str__(self) -> str:
        return self.__queue.__str__()


all_employess_data, queue_instruction_data = input('Enter Input : ').split('/')

employees_data = all_employess_data.split(',')
employees = list(map(lambda employee_data: employee_data.split(' '), employees_data))

commands = queue_instruction_data.split(',')

queue = Queue([])

for command in commands:
    if command[0] == 'D':
        if queue.length():
            print(queue.dequeue()[1])
            continue
        print('Empty')
    elif command[0] == 'E':
        employee_id = command.split(' ')[1]
        for source_department, source_employee in employees:
            if source_employee == employee_id:
                for i, queued_employee in enumerate(queue.get_queue()[::-1]):
                    if queued_employee[0] == source_department:
                        modified_queue = queue.get_queue()
                        modified_queue.insert(queue.length() - i, (source_department, source_employee))
                        queue.set_queue(modified_queue)
                        break
                else:
                    queue.enqueue((source_department, source_employee))
