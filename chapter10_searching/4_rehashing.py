'''
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด
'''

def sieve_of_eratosthenes(int_list):
    primes = []
    list_max = max(int_list)
    while int_list:
        current_prime = int_list.pop(0)
        primes.append(current_prime)
        for multiplier in range(2, (list_max // current_prime) + 1):
            current_prime_multiples = current_prime * multiplier
            if current_prime_multiples > list_max:
                break
            try:
                int_list.remove(current_prime_multiples)
            except ValueError:
                pass
    return primes

def is_prime(number: int):
    sieve_result = sieve_of_eratosthenes(list(range(2, number+1)))
    if sieve_result[-1] == number:
        return True
    return False

def get_next_prime(number: int):
    number += 1
    while not is_prime(number):
        number += 1
    return number

class Data:
    def __init__(self, _key, _value):
        self.key: str = _key
        self.value: str = _value

    def __str__(self):
        return str(self.value)

class Table:
    def __init__(self, size: int) -> None:
        self.table = [None] * size

    def __str__(self) -> str:
        output = ''
        for index, _data in enumerate(self.table, 1):
            output += f'#{index}	{str(_data)}\n'
        output += '----------------------------------------'
        return output

    def __len__(self):
        return len(self.table)

    def insert(self, _data: Data):
        new_data_hash = self.get_data_hash(_data)
        # print('hash=',new_data_hash)
        loop_index = 0
        offset = new_data_hash + loop_index ** 2
        insert = True
        while self.table[offset] is not None:
            print(f'collision number {loop_index+1} at {offset}')
            if loop_index + 1 >= max_collision:
                print('****** Max collision - Rehash !!! ******')
                insert = False
                self.rehash()
                self.insert(_data)
                break
            loop_index += 1
            offset = new_data_hash + loop_index ** 2
            if offset >= len(self):
                offset %= len(self)

        if insert:
            self.table[offset] = _data

    def rehash(self):
        new_size = get_next_prime(len(self) * 2)
        old_table = self.table.copy()[::-1]
        self.table = [None] * new_size
        for _data in old_table:
            if _data is not None:
                self.insert(_data)

    def get_data_hash(self, data: Data):
        return int(data.value) % len(self)

    def get_none_count(self):
        return self.table.count(None)

    def get_data_count(self):
        return len(self) - self.get_none_count()



print(' ***** Rehashing *****')
table_info, data_raw = input('Enter Input : ').split('/')

table_size, max_collision, rehashing_threshold = map(int, table_info.split())
table = Table(table_size)

print('Initial Table :')
print(table)

for data_string in data_raw.split():
    print(f'Add : {data_string}')

    if ((table.get_data_count() + 1) / len(table)) * 100 > rehashing_threshold:
        print('****** Data over threshold - Rehash !!! ******')
        table.rehash()

    new_data = Data(data_string, data_string)
    table.insert(new_data)

    print(table)
