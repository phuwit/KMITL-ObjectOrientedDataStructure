# Chapter : 1 - item : 3 - Fun with permute

# เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด


print('*** Fun with permute ***')
input_string = input('input : ')
input_list = [int(n) for n in input_string.split(" ")]

possible_permutations = []

print(f'Original Cofllection: {input_list}')
print(f'Collection of distinct numbers:\n {possible_permutations}')

# Original Cofllection:  [1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
