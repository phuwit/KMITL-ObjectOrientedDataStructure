"""
Chapter : 7 - item : 3 - สีแดงแรง 3 เท่า

ให้น้องๆรับ input เป็น list และ k โดยให้สร้าง Binary Search Tree จาก list ที่รับมา และหลังจากนั้นให้ทำการดูว่าใน Tree มีค่าไหนที่มากกว่าค่า k หรือไม่ ถ้ามีให้ทำการคูณ 3 เพิ่มเข้าไป

Enter Input : 67 102 81 35 15 7 99 196 202 152/90
                202
           196
                152
      102
                99
           81
 67
      35
           15
                7
--------------------------------------------------
                606
           588
                456
      306
                297
           81
 67
      35
           15
                7


Enter Input : 5 3 -1 4 7 6 8/-5
           8
      7
           6
 5
           4
      3
           -1
--------------------------------------------------
           24
      21
           18
 15
           12
      9
           -3


Enter Input : 5 3 1 4 7 6 8/4
           8
      7
           6
 5
           4
      3
           1
--------------------------------------------------
           24
      21
           18
 15
           4
      3
           1

"""


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Node | None = None
        self.right: Node | None = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, node_data: int):
        new_node = Node(node_data)

        if not self.root:
            self.root = new_node
            return

        previous_node = self.root
        current_node = self.root
        while current_node:
            previous_node = current_node
            if new_node.data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if new_node.data < previous_node.data:
            previous_node.left = new_node
        else:
            previous_node.right = new_node

    def print(self, node, level=0):
        if node is not None:
            self.print(node.right, level + 1)
            print("     " * level, node)
            self.print(node.left, level + 1)

    def get_height(self, node=None) -> int:
        if node is None:
            node = self.root

        left_height = -1
        if node and node.left:
            left_height = self.get_height(node=node.left)

        right_height = -1
        if node and node.right:
            right_height = self.get_height(node=node.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def times_n_if_more_than_k(self, _n: int, _k: int, node=None):
        if node is None:
            node = self.root

        if node and node.data > _k:
            node.data *= _n

        if node and node.left:
            self.times_n_if_more_than_k(node=node.left, _n=_n, _k=_k)

        if node and node.right:
            self.times_n_if_more_than_k(node=node.right, _n=_n, _k=_k)


tree = Tree()
inputs = [i for i in input("Enter Input : ").split("/")]
k = int(inputs.pop())
nodes = [int(i) for i in inputs.pop().split()]
for i in nodes:
    tree.insert(i)
tree.print(tree.root)
print("--------------------------------------------------")
tree.times_n_if_more_than_k(_n=3, _k=k, node=tree.root)
tree.print(tree.root)
