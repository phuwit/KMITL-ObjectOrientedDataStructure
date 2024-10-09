'''
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value
'''


def get_first_greater_value(sorted_list, target) -> int:
    target_index = 0
    while not target_index:
        try:
            target_index = sorted_list.index(target) + 1
        except ValueError:
            target -= 1
    sliced_list = sorted_list[target_index::]
    if not sliced_list:
        return -1
    return min(sliced_list)

data_string, target_string = input("Enter Input : ").split("/")
data = sorted(list(map(int, data_string.split())))
targets = list(map(int, target_string.split()))
for target in targets:
    first_greater_value = get_first_greater_value(data, target)
    if first_greater_value == -1:
        print('No First Greater Value')
    else:
        print(first_greater_value)
