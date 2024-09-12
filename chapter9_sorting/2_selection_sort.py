def get_max_index(int_list, max_index, current_pointer):
    if current_pointer >= len(int_list):
        return max_index
    if int_list[current_pointer] > int_list[max_index]:
        return get_max_index(int_list=int_list, max_index=current_pointer, current_pointer=current_pointer+1)
    return get_max_index(int_list=int_list, max_index=max_index, current_pointer=current_pointer+1)

def selection_sort(int_list, current_pointer):
    if current_pointer >= len(int_list):
        return int_list

    find_max_until_index = len(int_list) - current_pointer
    max_index = get_max_index(int_list=int_list[:find_max_until_index:], max_index=0, current_pointer=1)

    max_should_be_at_index = find_max_until_index - 1

    max_value = int_list[max_index]
    current_value = int_list[max_should_be_at_index]

    if max_should_be_at_index != max_index:
        int_list[max_should_be_at_index], int_list[max_index] = int_list[max_index], int_list[max_should_be_at_index]
        print(f'swap {current_value} <-> {max_value} : {int_list}')
    sorted_sublist = selection_sort(int_list=int_list, current_pointer=current_pointer+1)
    return sorted_sublist

input_numbers = list(map(int, input('Enter Input : ').split()))

input_len = len(input_numbers) - 1
print(selection_sort(input_numbers, 0))
