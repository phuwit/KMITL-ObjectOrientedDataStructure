"""
เขียน function bubble sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***

"""


def bubble_sort(int_list, pointer):
    if pointer >= len(int_list) - 1:
        return int_list

    if int_list[pointer] > int_list[pointer + 1]:
        int_list[pointer], int_list[pointer + 1] = (
            int_list[pointer + 1],
            int_list[pointer],
        )

    return bubble_sort(int_list, pointer + 1)


def bubble_sort_until_sorted(int_list):
    if len(int_list) <= 1:
        return int_list
    int_list = bubble_sort(int_list, 0)
    if len(int_list) >= 2:
        sorted_num = int_list.pop()
        sorted_sublist = bubble_sort_until_sorted(int_list)
        sorted_sublist.append(sorted_num)
        return sorted_sublist
    return bubble_sort_until_sorted(int_list)


input_numbers = list(map(int, input("Enter Input : ").split()))

print(bubble_sort_until_sorted(input_numbers))
