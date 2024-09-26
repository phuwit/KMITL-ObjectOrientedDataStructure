def binary_search(
    range_start, range_end, sorted_list, target
) -> bool:
    if range_end < range_start:
        return False
    middle_index = (range_start + range_end) // 2
    middle_value = sorted_list[middle_index]
    if middle_value == target:
        return True
    if middle_value > target:
        return binary_search(
            range_start=middle_index + 1,
            range_end=range_end,
            sorted_list=sorted_list,
            target=target,
        )
    if middle_value < target:
        return binary_search(
            range_start=range_start,
            range_end=middle_index - 1,
            sorted_list=sorted_list,
            target=target,
        )

    return False


data_string, target_string = input("Enter Input : ").split("/")
data = list(map(int, data_string.split()))
target = int(target_string)
print(binary_search(0, len(data) - 1, sorted(data), target))
