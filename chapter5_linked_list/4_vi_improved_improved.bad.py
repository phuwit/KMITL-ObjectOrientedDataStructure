"""
Chapter : 5 - item : 4 - VIM Text Editor

กฤษฎาได้มีไอเดียสุดบรรเจิดคือการสร้างโปรแกรม Text Editor แบบ VIM ขึ้นมาใช้งานเอง โดยโปรแกรมนี้จะมีอยู่แค่ 1 Mode คือ Command Mode (inputของเรานั่นแหละ) โดยจะมีคำสั่งอยู่ 5 แบบ คือ Insert (I) , Left (L) , Right (R) , Backspace (B) และ Delete (D) (โดยความสามารถของคำสั่งต่างๆจะอธิบายด้านล่าง) แต่กฤษฎาไม่มีความสามารถทางด้านการสร้างโปรแกรมเลย กฤษฎาจึงได้มาขอร้องน้องๆที่เรียนอยู่วิศวกรรมคอมพิวเตอร์ ให้ช่วยสร้างโปรแกรม Text Editor ที่กฤษฎาต้องการให้หน่อย โดยผลลัพธ์ให้แสดงออกมาเป็น word ที่เหลืออยู่จาก Command ที่เราใส่ลงไป พร้อมกับตำแหน่งของ Cursor

***** อธิบาย Input 5 แบบ *****

1.  I <word > :   เป็นการนำ word ลงไปใส่ในตำแหน่งของ Cursor ปัจจุบัน หลังจากใส่ word เสร็จ ตำแหน่งของ Cursor จะมาอยู่ด้านหลังของ word ที่ใส่ลงไป

2.  L              :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านซ้าย 1 ตำแหน่ง หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

3.  R             :   เป็นการเลื่อน Cursor จากตำแหน่งปัจจุบันไปทางด้านขวา 1 ตำแหน่ง หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร

4.  B             :   เป็นการลบ word 1 ตัวทางด้านซ้ายของ Cursor หากอยู่ทางซ้ายสุดอยู่แล้วจะไม่เกิดผลอะไร

5.  D             :   เป็นการลบ word 1 ตัวทางด้านขวาของ Cursor หากอยู่ทางขวาสุดอยู่แล้วจะไม่เกิดผลอะไร


Enter Input : I Apple,I Bird,I Cat
Apple Bird Cat |

Enter Input : I Apple,I Bird,I Cat,L
Apple Bird | Cat

Enter Input : I Apple,I Bird,I Cat,L,L
Apple | Bird Cat

Enter Input : I Apple,I Bird,I Cat,L,L,L,L,L
| Apple Bird Cat

Enter Input : I Apple,I Bird,I Cat,L,L,R
Apple Bird | Cat

Enter Input : I Apple,I Bird,I Cat,L,L,R,B
Apple | Cat

Enter Input : I Apple,I Bird,L,L,R,D,D
Apple |

Enter Input : L,R,I ABC,I DE,L,I FGHI
ABC FGHI | DE

Enter Input : I A,I B,L,L,R,D,D,L,L,R,I BCD,L,L,B,D,R,R,L,L
| BCD

Enter Input : I I,I KMITL,L,L,R,I Love
I Love | KMITL

Enter Input : I I,I KMITL,L,L,R,I Love,D,I DataStructure,L,L,R,L,R,B,I Hate
I Hate | DataStructure
"""

from base_linked_list import SinglyLinkedList


class Cursor:
    def __init__(self, _linked_list) -> None:
        self.__linked_list: SinglyLinkedList = _linked_list
        self.__index: int = 0

    def move_left(self):
        self.__index -= 1
        if self.__index < 0:
            self.__index = 0

    def move_right(self):
        self.__index += 1
        if self.__index > self.__linked_list.size():
            self.__index = self.__linked_list.size()


commands = input("Enter Input : ").split(",")

linked_list = SinglyLinkedList()
cursor = Cursor(linked_list)

for command in commands:
    try:
        word = command.split().pop()
        linked_list.append(word)

    except Exception:
        if command[0] == "L":
            cursor.move_left()
            continue
        elif command[0] == "R":
            cursor.move_right()
            continue

print()
