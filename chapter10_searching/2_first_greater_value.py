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
