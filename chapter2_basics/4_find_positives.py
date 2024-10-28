# Chapter : 2 - item : 4 - 3 SUM

# จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***


from typing import List, Set, Tuple


input_string = input("Enter Your List : ")
numbers = [int(n) for n in input_string.split(" ")]

if len(numbers) < 3:
    print("Array Input Length Must More Than 2")
    exit()

sum_positives_set: Set[Tuple[int, int, int]] = set()

found: bool = False

for i, n1 in enumerate(numbers):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            n2 = numbers[j]
            n3 = numbers[k]
            if (n1 + n2 + n3) == 0 and not found:
                sum_positives_set.add((n1, n2, n3))

sum_positives_list = []

for sum_positive_tuple in sum_positives_set:
    sum_positives_list.append(list(sum_positive_tuple))

print(list(reversed(sum_positives_list)))
