# Chapter : 1 - item : 3 - Fun with permute

# เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด

# Original Cofllection:  [1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
#  00           01         12         20        01          12

# input : 1,1,2,3
# Original Cofllection:  [1, 1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3], [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]


print('*** Fun with permute ***')
input_string = input('input : ')
input_list = [int(n) for n in input_string.split(",")]

possible_permutations: list[list[int]] = []

print(f'Original Cofllection: {input_list}')

reversed_input_list = list(reversed(input_list))
possible_permutations.append(reversed_input_list)
LIST_LENGTH = range(len(reversed_input_list))

def swap_pairs(numbers: list[int], start_index: int = 0) -> list[list[int]]:
    permutations: list[list[int]] = [numbers]
    length = len(numbers)
    for i in range(start_index, length - 1):
        current = list(permutations[-1])
        cursor_a = i
        cursor_b = i + 1
        current[cursor_a], current[cursor_b] = current[cursor_b], current[cursor_a]
        permutations.append(current)

    return permutations


def permute(numbers: list[int]) -> list[list[int]]:
    permutations: list[list[int]] = []
    for i in swap_pairs(numbers, start_index=1):
        permutations.extend(swap_pairs(i))

    return permutations

# print(permute(reversed_input_list))
print(f'Collection of distinct numbers:\n {permute(reversed_input_list)}')
