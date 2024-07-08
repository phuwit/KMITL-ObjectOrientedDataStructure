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


from typing import List


print("*** Fun with permute ***")
input_string = input("input : ")
input_list = [int(n) for n in input_string.split(",")]

print(f"Original Cofllection:  {input_list}")


def get_possible_insertions(number: int, target_list: List[int]):
    insertions: List[List[int]] = []
    for i in range(len(target_list) + 1):
        insertion = list(target_list)
        insertion.insert(i, number)
        insertions.append(insertion)
    return insertions


# def permute(
#     original_list: List[int], current_permutation: List[int], current_index: int = 0
# ):
#     permutations: List[List[int]] = []
#     if current_index >= len(original_list) - 1:
#         return get_possible_insertions(
#             number=original_list[current_index], target_list=current_permutation
#         )
#     else:
#         for index, value in enumerate(original_list[current_index:-1:]):
#             edited_permutation = list(current_permutation)
#             edited_permutation.insert(index, value)
#             permutations.extend(
#                 permute(
#                     original_list=original_list,
#                     current_permutation=edited_permutation,
#                     current_index=current_index + 1,
#                 )
#             )

#     return permutations

def permute(
    original_list: List[int], active_permutation: List[int], current_index: int = 0
):
    permutations: List[List[int]] = []
    if len(active_permutation) == 0:
        permutations.extend(permute(original_list=original_list, active_permutation=[original_list[current_index]], current_index=current_index + 1))
    else:
        insert_number = original_list[current_index]
        insertions = get_possible_insertions(number=insert_number, target_list=active_permutation)
        if len(insertions[0]) == len(original_list):
            return insertions
        else:
            for permutation in insertions:
                permutations.extend(permute(original_list=original_list, active_permutation=permutation, current_index=current_index + 1))

    return permutations


possible_permutations: List[List[int]] = []
possible_permutations.extend(
    permute(original_list=input_list, active_permutation=[], current_index=0) or []
)


print(f"Collection of distinct numbers:\n {possible_permutations}")
