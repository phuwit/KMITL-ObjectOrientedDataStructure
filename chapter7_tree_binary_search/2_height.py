"""
Chapter : 7 - item : 2 - หาค่า height

ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ

จากนั้นหาความสูงของ Binary Search Tree  นั้น

Enter Input : 3 5 2 1 4 6
Height of this tree is : 2

Enter Input : 3 5 2 1 4 6 7
Height of this tree is : 3

Enter Input : 1
Height of this tree is : 0

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

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print("     " * level, node)
            self.printTree(node.left, level + 1)

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


tree = Tree()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    tree.insert(i)
height = tree.get_height(tree.root)
print(f"Height of this tree is : {height}")
