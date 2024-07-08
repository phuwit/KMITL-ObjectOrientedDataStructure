def get_possible_insertions(number, target_list):
    insertions = []
    for i in range(len(target_list) + 1):
        insertion = list(target_list)
        insertion.insert(i, number)
        insertions.append(insertion)
    return insertions

def permute(original_list, active_permutation, current_index=0):
    permutations = []
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

print("*** Fun with permute ***")
input_string = input("input : ")
input_list = [int(n) for n in input_string.split(",")]

print(f"Original Cofllection:  {input_list}")
possible_permutations = []
possible_permutations.extend(
    permute(original_list=input_list, active_permutation=[], current_index=0) or []
)

print(f"Collection of distinct numbers:\n {possible_permutations}")