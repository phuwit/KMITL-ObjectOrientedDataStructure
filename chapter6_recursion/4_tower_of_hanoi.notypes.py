class Peg:
    def __init__(self, symbol):
        self.__disks = []
        self.symbol = symbol

    def add_disk(self, disk):
        if not self.__disks:
            self.__disks.append(disk)
            return True
        if self.__disks[-1] < disk:
            self.__disks.append(disk)
            return True
        return False

    def remove_disk(self):
        return self.__disks.pop()

    def get_all_disks(self):
        return self.__disks

def print_tower(pegs):
    tower = ['|  |  |']
    max_height = max(len(peg.get_all_disks()) for peg in pegs)
    for i in range(max_height, 0, -1):
        row = []
        for peg in pegs:
            if len(peg.get_all_disks()) >= i:
                row.append(str(peg.get_all_disks()[::-1][i-1]))
            else:
                row.append('|')
        tower.append('  '.join(row))
    while len(tower) < print_height:
        tower.insert(0, '|  |  |')
    print('\n'.join(tower))

def get_helper_peg(pegs, peg1, peg2):
    index = 3 - pegs.index(peg1) - pegs.index(peg2)
    return pegs[index]

def solve(num_disks, from_peg, to_peg):
    if num_disks <= 0:
        return

    helper_peg = get_helper_peg(pegs, from_peg, to_peg)
    solve(num_disks=num_disks-1, from_peg=from_peg, to_peg=helper_peg)
    to_peg.add_disk(from_peg.remove_disk())
    solve(num_disks=num_disks-1, from_peg=helper_peg, to_peg=to_peg)

    print(f'move {num_disks} from  {from_peg.symbol} to {to_peg.symbol}')
    print_tower(pegs)

num_disks = int(input("Enter Input : "))
print_height = num_disks + 1

pegs = [Peg('A'), Peg('B'), Peg('C')]

source_peg = pegs[0]
for i in range(1, num_disks+1):
    source_peg.add_disk(i)
print_tower(pegs)

solve(num_disks=num_disks, from_peg=pegs[0], to_peg=pegs[-1])