# Chapter : 3 - item : 1 - รู้จักกับ STACK

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ STACK ในการแก้ปัญหา


# A  <value>  ให้นำ value ไปใส่ใน STACK และทำการแสดงผล Size ปัจจุบันของ STACK

# P                 ให้ทำการแสดงผลของvalueที่อยู่ท้ายสุดและindexของvalueนั้นจากนั้นทำการ Pop_Stack ถ้าหากไม่มี value อยู่ใน Stack ให้แสดงผลเป็น  -1

# *** ในตอนสุดท้ยถ้าหากใน Stack ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty


# Enter Input : A 10,A 20,A 30,A 40,P,P
# Add = 10 and Size = 1
# Add = 20 and Size = 2
# Add = 30 and Size = 3
# Add = 40 and Size = 4
# Pop = 40 and Index = 3
# Pop = 30 and Index = 2
# Value in Stack = 10 20


input_string = input('Enter Input : ')
commands = input_string.split(',')

# print(commands)

stack = []
for command in commands:
    # print(command)
    if command[0] == 'A':
        command_type, value = command.split(' ')
        stack.append(value)
        print(f'Add = {value} and Size = {len(stack)}')
    elif command[0] == 'P':
        if len(stack) >= 1:
            value = stack.pop()
            print(f'Pop = {value} and Index = {len(stack)}')
            continue
        print(-1)
        continue

stack_string = ' '.join(stack)

if len(stack):
    print(f'Value in Stack = {stack_string}')
else:
    print('Value in Stack = Empty')
