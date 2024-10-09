'''
ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา
def bi_search(l, r, arr, x):
    # Code Here

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
'''

def binary_search(
    range_start, range_end, sorted_list, target
) -> bool:
    if range_end < range_start:
        return False
    middle_index = (range_start + range_end) // 2
    middle_value = sorted_list[middle_index]
    if middle_value == target:
        return True
    if middle_value < target:
        return binary_search(
            range_start=middle_index + 1,
            range_end=range_end,
            sorted_list=sorted_list,
            target=target,
        )

    return binary_search(
        range_start=range_start,
        range_end=middle_index - 1,
        sorted_list=sorted_list,
        target=target,
    )



data_string, target_string = input("Enter Input : ").split("/")
data = list(map(int, data_string.split()))
target = int(target_string)
print(binary_search(0, len(data) - 1, sorted(data), target))
