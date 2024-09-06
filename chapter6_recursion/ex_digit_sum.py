def get_final_digit_sum(number: int) -> int:
    sumsum = get_digit_sum(number=number)

    if sumsum >= 10:
        return get_final_digit_sum(number=sumsum)
    return sumsum

def get_digit_sum(number: int) -> int:
    if number < 0:
        number = -number
    if number == 0:
        return 0

    digit_value = number % 10
    number = number // 10

    return digit_value + get_digit_sum(number=number)


print(get_final_digit_sum(number=int(input())))