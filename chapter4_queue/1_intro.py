# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา


# E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

# D  ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูลปัจจุบันของ Queue

# ***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
# ***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty


# Testcase : #1
# Enter Input : E 1,E 2,E 3,D,D,E 4
# 1
# 1, 2
# 1, 2, 3
# 1 <- 2, 3
# 2 <- 3
# 3, 4
# 1, 2 : 3, 4

# Testcase : #2
# Enter Input : E 1,E 2,D,D,D
# 1
# 1, 2
# 1 <- 2
# 2 <- Empty

# Testcase : #3
# Enter Input : D
# Empty
# Empty : Empty

input_string = input("Enter Input : ")
commands = input_string.split(",")

# print(commands)

queue = []
queue_removed = []
for command in commands:
    # print(command)
    if command[0] == "E":
        command_type, value = command.split(" ")
        queue.append(value)
        output_string = ", ".join(queue)
        print(output_string)
    elif command[0] == "D":
        if len(queue) >= 1:
            value = queue.pop(0)
            queue_removed.append(value)
            output_string = ", ".join(queue)
            if not queue:
                output_string = "Empty"
            output_string = f"{value} <- {output_string}"
            print(output_string)
            continue
        print("Empty")


queue_string = ", ".join(queue)
queue_removed_string = ", ".join(queue_removed)
if not queue:
    queue_string = "Empty"
if not queue_removed:
    queue_removed_string = "Empty"
print(f"{queue_removed_string} : {queue_string}")
