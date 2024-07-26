'''
Chapter : 6 - item : 4 - หอคอยแห่งฮานอย

เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
และให้ระวังเรื่องการสลับ list ให้ดีๆ

หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html
def move(n,A,B,C,maxn):
    #code here
n = int(input("Enter Input : "))


Enter Input : 3
|  |  |
1  |  |
2  |  |
3  |  |
move 1 from  A to C
|  |  |
|  |  |
2  |  |
3  |  1
move 2 from  A to B
|  |  |
|  |  |
|  |  |
3  2  1
move 1 from  C to B
|  |  |
|  |  |
|  1  |
3  2  |
move 3 from  A to C
|  |  |
|  |  |
|  1  |
|  2  3
move 1 from  B to A
|  |  |
|  |  |
|  |  |
1  2  3
move 2 from  B to C
|  |  |
|  |  |
|  |  2
1  |  3
move 1 from  A to C
|  |  |
|  |  1
|  |  2
|  |  3

=================================================================================

Enter Input : 4
|  |  |
1  |  |
2  |  |
3  |  |
4  |  |
move 1 from  A to B
|  |  |
|  |  |
2  |  |
3  |  |
4  1  |
move 2 from  A to C
|  |  |
|  |  |
|  |  |
3  |  |
4  1  2
move 1 from  B to C
|  |  |
|  |  |
|  |  |
3  |  1
4  |  2
move 3 from  A to B
|  |  |
|  |  |
|  |  |
|  |  1
4  3  2
move 1 from  C to A
|  |  |
|  |  |
|  |  |
1  |  |
4  3  2
move 2 from  C to B
|  |  |
|  |  |
|  |  |
1  2  |
4  3  |
move 1 from  A to B
|  |  |
|  |  |
|  1  |
|  2  |
4  3  |
move 4 from  A to C
|  |  |
|  |  |
|  1  |
|  2  |
|  3  4
move 1 from  B to C
|  |  |
|  |  |
|  |  |
|  2  1
|  3  4
move 2 from  B to A
|  |  |
|  |  |
|  |  |
|  |  1
2  3  4
move 1 from  C to A
|  |  |
|  |  |
|  |  |
1  |  |
2  3  4
move 3 from  B to C
|  |  |
|  |  |
|  |  |
1  |  3
2  |  4
move 1 from  A to B
|  |  |
|  |  |
|  |  |
|  |  3
2  1  4
move 2 from  A to C
|  |  |
|  |  |
|  |  2
|  |  3
|  1  4
move 1 from  B to C
|  |  |
|  |  1
|  |  2
|  |  3
|  |  4

'''

from typing import List


num_disks = int(input("Enter Input : "))
print_height = num_disks + 1

class Peg:
    def __init__(self, symbol) -> None:
        self.__disks: List[int] = []
        self.symbol: str = symbol

    def add_disk(self, disk: int):
        if not self.__disks:
            self.__disks.append(disk)
            return True
        if disk < self.__disks[-1]:
            self.__disks.append(disk)
            return True
        return False

    def remove_disk(self):
        return self.__disks.pop()

    def get_all_disks(self):
        return self.__disks

def print_tower(pegs: List[Peg]):
    tower: List[str] = ['|  |  |']
    max_height = max(len(peg.get_all_disks()) for peg in pegs)
    for i in range(max_height, 0, -1):
        row = []
        for peg in pegs:
            if len(peg.get_all_disks()) >= i:
                row.append(str(peg.get_all_disks()[i-1]))
            else:
                row.append('|')
        tower.append('  '.join(row))
    while len(tower) < print_height:
        tower.insert(0, '|  |  |')
    print('\n'.join(tower))

pegs = [Peg('A'), Peg('B'), Peg('C')]

source_peg = pegs[0]
for i in range(num_disks, 0, -1):
    source_peg.add_disk(i)
print_tower(pegs)

def get_helper_peg(pegs: List[Peg], peg1: Peg, peg2: Peg):
    index = 3 - pegs.index(peg1) - pegs.index(peg2)
    return pegs[index]

def solve(num_disks: int, from_peg: Peg, to_peg: Peg):
    if num_disks <= 0:
        return

    helper_peg = get_helper_peg(pegs, from_peg, to_peg)
    solve(num_disks=num_disks-1, from_peg=from_peg, to_peg=helper_peg)
    to_peg.add_disk(from_peg.remove_disk())

    print(f'move {num_disks} from  {from_peg.symbol} to {to_peg.symbol}')
    print_tower(pegs)

    solve(num_disks=num_disks-1, from_peg=helper_peg, to_peg=to_peg)

solve(num_disks=num_disks, from_peg=pegs[0], to_peg=pegs[-1])