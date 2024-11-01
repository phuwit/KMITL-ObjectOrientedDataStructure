"""
จงเขียนโปรแกรมเพื่อรับข้อมูล แล้วสร้าง AVL tree และแสดงการแวะผ่านโหนดต่าง ๆ แบบ post-order

โดยแก้ไข method add คือการเพิ่มข้อมูลเข้าใน AVLTree และ method postOrder คือ บริการแวะผ่านโหนดทุกโหนดแบบหลังลำดับ จากส่วนของโปรแกรมต่อไปนี้


class AVLTree:

    class AVLNode:

        def __init__(self, data, left = None, right = None):

            self.data = data

            self.left = None if left is None else left

            self.right = None if right is None else right

            self.height = self.setHeight()



        def __str__(self):

            return str(self.data)



        def setHeight(self):

                a = self.getHeight(self.left)

                b = self.getHeight(self.right)

                self.height = 1 + max(a,b)

                return self.height



        def getHeight(self, node):

            return -1 if node == None else node.height



        def balanceValue(self):

            return self.getHeight(self.right) - self.getHeight(self.left)



    def __init__(self, root = None):

        self.root = None if root is None else root



    def add(self, data):

        # code here



    def _add(root, data):

        # code here


    def rotateLeftChild(root) :

         # code here


    def rotateRightChild(root) :

          # code here


    def postOrder(self):

         # code here


   def _postOrder(root):

         # code here


    def printTree(self):

        AVLTree._printTree(self.root)

        print()



    def _printTree(node , level=0):

        if not node is None:

            AVLTree._printTree(node.right, level + 1)

            print('     ' * level, node.data)

            AVLTree._printTree(node.left, level + 1)



avl1 = AVLTree()

inp = input('Enter Input : ').split(',')

for i in inp:

    if i[:2] == "AD":

        avl1.add(i[3:])

    elif i[:2] == "PR":

        avl1.printTree()

    elif i[:2] == "PO":

        avl1.postOrder()
"""

from __future__ import annotations
from typing import List


class AVLNode[T]:
    def __init__(self, data) -> None:
        self.data: "T" = data
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.height = 1

    def update_height(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = max(left_height, right_height) + 1

    def get_balance_factor(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return right_height - left_height

    def is_balanced(self):
        if -1 <= self.get_balance_factor() <= 1:
            return True
        return False

    def __str__(self) -> str:
        return str(self.data)


class AVLTree[T]:
    def __init__(self) -> None:
        self.root: AVLNode | None = None

    def postorder(self, node: AVLNode):
        _nodes: List[AVLNode] = []
        if node.left:
            _nodes.extend(self.postorder(node=node.left))
        if node.right:
            _nodes.extend(self.postorder(node=node.right))
        _nodes.append(node)
        return _nodes

    def print(self):
        AVLTree.print_subtree(self, node=self.root)
        print()

    def print_subtree(self, node, level=0):
        if node is not None:
            AVLTree.print_subtree(self, node.right, level + 1)
            print("     " * level, node.data)
            AVLTree.print_subtree(self, node.left, level + 1)

    def rotate_left(self, node: AVLNode) -> AVLNode:
        # print(f'rotating left {node}')
        child = node.right
        if not child:
            raise AttributeError

        node.right = child.left
        child.left = node

        node.update_height()
        child.update_height()

        return child

    def rotate_right(self, node: AVLNode) -> AVLNode:
        # print(f'rotating right {node}')
        child = node.left
        if not child:
            raise AttributeError

        node.left = child.right
        child.right = node

        node.update_height()
        child.update_height()

        return child

    def rebalance(self, node: AVLNode):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        # AVL Violation on right child
        if right_height > left_height:
            # Right Right imbalance -> Rotate Left
            if node.right and node.right.get_balance_factor() >= 0:
                node = self.rotate_left(node)
                return node

            # Right Left imbalance -> Rotate Right-Left
            if node.right and node.right.left and node.right.get_balance_factor() < 0:
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)
                return node

        # AVL Violation on left child
        else:
            # Left Left imbalance -> Rotate Right
            if node.left and node.left.get_balance_factor() <= 0:
                node = self.rotate_right(node)
                return node

            # Left Right imbalance -> Rotate Left-Right
            if node.left and node.left.right and node.left.get_balance_factor() > 0:
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
                return node

    def rebalance_child(self, node: AVLNode):
        if node.right and not node.right.is_balanced():
            node.right = self.rebalance(node=node.right)
            node.update_height()
            return node

        if node.left and not node.left.is_balanced():
            node.left = self.rebalance(node=node.left)
            node.update_height()
            return node

    def rebalance_root(self):
        if not self.root:
            return
        if not self.root.is_balanced():
            self.root = self.rebalance(self.root)
            # print(f'rebalancing root with {self.root}')

    def _recursive_insert(self, current_node: AVLNode, to_insert: AVLNode):
        if to_insert.data >= current_node.data:
            if current_node.right is None:
                current_node.right = to_insert
            else:
                self._recursive_insert(
                    current_node=current_node.right, to_insert=to_insert
                )
        else:
            if current_node.left is None:
                current_node.left = to_insert
            else:
                self._recursive_insert(
                    current_node=current_node.left, to_insert=to_insert
                )

        current_node.update_height()

        rebalance_result = self.rebalance_child(node=current_node)
        if rebalance_result:
            # print(f'replacing {current_node} with {rebalance_result}')
            current_node = rebalance_result

    def insert(self, data: "T"):
        # print(f'inserting {data}')
        new_node: AVLNode = AVLNode(data=data)
        if self.root is None:
            self.root = new_node
            return
        self._recursive_insert(current_node=self.root, to_insert=new_node)
        self.rebalance_root()


tree: AVLTree = AVLTree()
input_string = input("Enter Input : ").split(",")
for command in input_string:
    # print(command)
    if command[:2] == "AD":
        tree.insert(int(command[3:]))
    elif command[:2] == "PR":
        tree.print()
    elif command[:2] == "PO":
        if tree.root:
            postorder_result = " ".join(map(str, tree.postorder(tree.root)))
            print(f"AVLTree post-order : {postorder_result}")
        else:
            print("AVLTree post-order : ")
    # tree.print()
    # print('===========================')


# tree: AVLTree = AVLTree()
# datas = [33,13,53,11,21,61,8,9]

# for data in datas:
#     tree.insert(int(data))

#     tree.print()
#     print('===========================')
