"""
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value
"""


class Data:
    def __init__(self, _key, _value, _table_size: int):
        self.key: str = _key
        self.value: str = _value
        self.hash = self.get_hash(_table_size=_table_size)

    def __str__(self):
        return f"({self.key}, {self.value})"

    def get_hash(self, _table_size: int) -> int:
        ascii_sum: int = sum(map(ord, self.key))
        return ascii_sum % _table_size


def print_table(_table):
    for index, data in enumerate(_table, 1):
        print(f"#{index}	{str(data)}")
    print("---------------------------")


print(" ***** Fun with hashing *****")
table_info, data_raw = input("Enter Input : ").split("/")

table_size, max_collision = map(int, table_info.split())
table = [None] * table_size

for data_string in data_raw.split(","):
    if table.count(None) == 0:
        print("This table is full !!!!!!")
        exit()

    key, value = data_string.split()
    new_data = Data(key, value, table_size)
    loop_index = 0
    offset = new_data.hash + loop_index**2
    insert = True
    while table[offset] is not None:
        print(f"collision number {loop_index+1} at {offset}")
        if loop_index + 1 >= max_collision:
            print("Max of collisionChain")
            insert = False
            break
        loop_index += 1
        offset = new_data.hash + loop_index**2
        if offset >= table_size:
            offset %= table_size

    if insert:
        table[offset] = new_data

    print_table(table)
