'''
เขียนโปรแกรมที่ทำการรับข้อมูลเป็น list เพื่อหาค่ามัธยฐานของข้อมูลใน list โดยจะเริ่มต้นจากข้อมูลใน list เพียง 1 ตัวจากนั้นค่อยๆเพิ่มไปเรื่อยๆจนครบ โดยในการหาค่ามัธยฐานเราต้องจัดเรียงข้อมูลตามลำดับจากน้อยไปหามากเสียก่อน จากนั้นแสดงผลตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น sort, min, max,ฯลฯ***
l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    #code here


***test case พิเศษเพิ่มเติม ไม่คิดคะแนน และไม่มีผลต่อการผ่านโจทย์ข้อนี้หรือไม่***

พี่มีคำถามมาถามน้องๆว่าในกรณีโจทย์แบบนี้ ถ้าหากจำนวน  input มีจำนวนมากกว่าหมื่นตัวขึ้นไป เราสามารถ sort algorithm แบบใดมาประยุกต์ใช้จึงจะเหมาะสม และ ทำเวลาได้ดี

- bubble sort

- straight selection sort

- insertion sort

- shell sort

- merge sort

- quick sort

- minHeap and maxHeap

พิมพ์คำตอบลงในช่อง Ans = "xxx"

***ยกมือถามได้นะถ้าสงสัยว่าทำไมเป็นอันนี้***

'''

def get_median(int_list):
    middle_index_float = (len(int_list) - 1) / 2
    middle_index_int = int(middle_index_float)
    # have fraction
    less_value = int_list[middle_index_int]
    if middle_index_float % 1 != 0:
        more_value = int_list[middle_index_int + 1]
        _median  = (less_value + more_value) / 2
        return _median
    # no fraction
    return float(less_value)


def insertion_sort(int_list):
    for sort_range in range(1, len(int_list)):
        for current_index in range(sort_range, 0, -1):
            previous_index = current_index - 1
            if int_list[previous_index] < int_list[current_index]:
                break
            int_list[previous_index], int_list[current_index] = int_list[current_index], int_list[previous_index]

    return int_list


input_values = [e for e in input("Enter Input : ").split()]
if input_values[0] == 'EX':
    Ans = "insertion sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : " + Ans)
else:
    input_values = list(map(int, input_values))
    running_list = []
    for i, value in enumerate(input_values):
        running_list.append(value)
        running_list = insertion_sort(running_list)
        median = get_median(running_list)
        sliced_list = input_values[:i+1:]
        print(f'list = {sliced_list} : median = {median}')
