"""
Chapter : 3 - item : 5 - วันหนึ่งฉันเดินเข้าป่า (ต่อ)

<<<  กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก (เดินยังไงให้หลงครับเนี่ยย - -") หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป >>>

****  ด้านบนจะเป็นเนื้อหาของ  < วันหนึ่งฉันเดินเข้าป่า   version  1 >  เผื่อบางคน Random ไม่ได้ครับ

หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :  A  <Heights>  แสดงถึงความสูงของต้นไม้  ,  B  คือการหันหลังกลับมามอง , S  คือการโดนผลกระทบจากเห็ดพิษ

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง


Enter Input : A 4,A 3,B,A 5,A 8,B
2
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B
-> 3 5
-> 5 4 5 8

2
1
1

Enter Input : A 4,A 3,B,S,B,A 5,A 8,B,S,B
2
1
1
1

Enter Input : A 4,A 3,B,S,B,A 5,A 6,B,S,B
-> 3 5
2
1
1
2

Enter Input : S,S,S,B,B,A 6,S,S,S,S,S,S,S,S,B
0
0
1

Enter Input : A 10,A 9,A 8,A 7,B,S,B,A 7,A 1,B,A 50,A 31,S,S,S,S,B
-> 9 11 7 9
-> 9 11 7 9 9 3
-> 9 11 7 9 9 3 49 33
4
2
4
2

Enter Input : A 5,A 4,B,S,S,A 4,B
2
3

Enter Input : A 3,A 4,B,S,S,S,S,S,B
1
2

A 4,A 3,B,S,B,A 5,A 6,B,S,B
-> 3 5 7 5

"""


class Stack:
    def __init__(self, ls=None):
        if ls is None:
            self.__stack = []
        else:
            self.__stack = ls

    def push(self, i):
        self.__stack.append(i)

    def pop(self):
        return self.__stack.pop()

    def isEmpty(self):
        return bool(self.__stack)

    def size(self):
        return len(self.__stack)

    def get(self):
        return self.__stack


all_commands = input("Enter Input : ").split(",")
stack = Stack()

def get_mushroom_modifier(_height):
    if _height % 2 == 0:
        return -1
    else:
        return 2

for command in all_commands:
    command = command.split()
    command_type = command.pop(0)
    if command_type == "A":
        height = int(command.pop())
        stack.push(height)
        continue
    elif command_type == "S":
        new_stack = Stack()
        for height in list(stack.get()):
            height += get_mushroom_modifier(height)
            new_stack.push(height)
        stack = new_stack
        continue
    elif command_type == "B":
        cloned_stack = Stack(list(stack.get()))
        if cloned_stack.size() >= 2:
            highest = cloned_stack.pop()
            seen = 1
            for height in cloned_stack.get()[::-1]:
                if height > highest:
                    seen += 1
                    highest = height
                    continue

            print(seen)
        elif cloned_stack.size() >= 1:
            print(1)
        else:
            print(0)
