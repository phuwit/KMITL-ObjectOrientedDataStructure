from typing import List

class Queue:
    def __init__(self, items: List) -> None:
        self.__list = items

    def peek(self):
        if len(self.__list) <= 0:
            return None
        return self.__list[0]

    def enqueue(self, item):
        self.__list.append(item)

    def dequeue(self):
        if len(self.__list) <= 0:
            return None
        return self.__list.pop(0)

    def get_list(self):
        return self.__list


class RadixSort:
    def get_max_item_from_list(self, items: List[int]):
        max = items[0]
        for item in items:
            if item > max:
                max = item
        return max


    def get_number_of_digits(self, number: int):
        digit = 1
        while number // (10 ** digit) > 0:
            digit += 1
        return digit


    def get_nth_digit(self, number: int, digit: int):
        nth_digit = number // (10 ** (digit - 1))
        nth_digit %= 10
        return nth_digit


    def sort(self, items: List[int]) -> List[int]:
        max = self.get_max_item_from_list(items)
        max_digits = self.get_number_of_digits(max)

        for digit in range(1, max_digits + 1):
            buckets: List[Queue] = []
            for _ in range(10):
                buckets.append(Queue([]))
                continue

            for item in items:
                extracted_digit = int(self.get_nth_digit(digit=digit, number=item))
                if 0 <= extracted_digit <= 9:
                    buckets[extracted_digit].enqueue(item)
                continue

            items = []
            for bucket in buckets:
                items.extend(bucket.get_list())

        return items


print(RadixSort().sort([170, 45, 75, 90, 2, 802, 2, 66]))