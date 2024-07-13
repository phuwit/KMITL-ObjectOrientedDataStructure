# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# *************************************************

class StackCalc:
    EXPRESSIONS_TOKEN = '+-*/'
    DIGITS_TOKEN = '0123456789'
    def __init__(self) -> None:
        self.__stack = []

    def run(self, commands):
        for command in commands:
            if command == 'DUP':
                self.__stack.append(self.__stack[-1])
                continue
            elif command == 'POP':
                self.__stack.pop()
                continue
            elif command in self.EXPRESSIONS_TOKEN:
                n2 = self.__stack.pop()
                n1 = self.__stack.pop()
                if command == '+':
                    value = n2 + n1
                elif command == '-':
                    value = n2 - n1
                elif command == '*':
                    value = n2 * n1
                elif command == '/':
                    value = n2 / n1
                self.__stack.append(int(value))
            elif command[0] in self.DIGITS_TOKEN:
                self.__stack.append(int(command))
            else:
                print(f'Invalid instruction: {command}')
                exit()

    def getValue(self):
        if not self.__stack:
            return 0
        return self.__stack[-1]

print("* Stack Calculator *")
args = input("Enter arguments : ").split(' ')
machine = StackCalc()
machine.run(args)
print(machine.getValue())
