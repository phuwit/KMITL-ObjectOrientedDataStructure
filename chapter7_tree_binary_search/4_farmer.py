"""
Chapter : 7 - item : 4 - Have even more fun with Binary Search Tree

วันนี้มีเกษตรกรท่านหนึ่งจะพามาปลูกต้นบ้วยกัน แต่ต้นบ้วยต้นนี้ไม่ธรรมดา เพราะเป็นต้นบ้วยที่มีเชื้อสายมาจาก binary search tree ที่ใช้ ascii table ในการเรียงโดยการจะดูแลให้ต้นบ้วยต้นนี้มีสภาพที่ดีที่สุดเพื่อนำไปขายโดยระหว่างที่ต้นบ้วยกำลังโตจะมีเหตุการเกิดขึ้น 4 อย่างได้แก่

1. ต้นบ้วยโต โดยใช้ตัวย่อว่า AP  โดยถ้ามีค่าน้อยจะไปอยู่ด้วนซ้าย ค่ามากกว่าหรือเท่ากันอยู่ด้านขวา

2. ตัดกิ่งต้นบ้วย โดยใช้ตัวย่อว่า CU โดยถ้าระบุตำแหน่งไหนให้ทำการหักกิ่งขวาของตัวที่ระบุก่อนถ้าไม่มีให้หักกิ่งซ้าย เช่น ถ้าหักกิ่ง b จะเป็นแบบข้างล่าง

	e				e

d				d

		c	->		b

	b					a

		a

3. มุมมองที่เปลี่ยนไป โดยใช้ตัวย่อว่า CH โดยให้พิมพ์ต้นบ้วยออกมาในรูปแบบ preorder, inorder, postorder ตามลำดับ โดยให้พิมพ์ออกมาเป็นตัวเลข ASCII ถึงค่าที่กำหนดไว้ หากไม่เข้าใจดูตัวอย่างข้างล่าง

4. เกษตรแอบมองดูต้นบ้วยจากในบ้าน โดยใช้ตัวย่อว่า MI ทำให้เกษตรเห็นต้นบ้วยจากด้านหลังทำให้เห็นต้นบ้วยกลับด้านทั้งหมดจงแสดงต้นบ้วยแบบกลับซ้ายขวาทั้งหมด

Example:

Enter Input : Z M E H P N O Q X Y a b j x/AP v,CH Z

Input แบ่งออกเป็น 2 ส่วนโดยใช้ ”/” ในการขั้น ส่วนแรกใช้ในการสร้างต้นไม้เริ่มต้น

ส่วนที่ 2 จะเป็นเหตุการที่จะเกิดขึ้นโดยมีการทำงานดังนี้

    AP F คือการเพิ่ม F เข้าไปในต้นไม้โดยใช้หลักการเดียวกับ binary search tree

    CU Z คือการตัดกิ่งที่อยู่ข้างใต้ node Z ออกไป 1 ข้างโดยตัดจากข้างขวาก่อนเสมอถ้าตัดไม่ได้ให้พิมพ์"Not thing change"

    CH Z โดยให้พิมพ์ preorder, inorder, postorder ตามลำดับโดยให้พิมพ์เป็นตัวเลข ASCII จนกว่าค่าจะเกินค่าที่กำหนดไว้จากตัวอย่างคือ Z ถ้าจำเป็นต้องพิมพ์เลข ASCII ของ string ให้พิมพ์เลขของทุกตัวเรยงติดกันเลย

    MI ให้พิมพ์ต้นไม้สลับซ้ายขวาทั้งหมด

***หมายเหตุ ไมเคยมีใครกล่าวว่า input จะเป็น char ไม่มี string นะ ***
start code สู้ๆ

```
class Node:
    def __init__(self, data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def append(self, data):
        # code Here

    def cut(self, data):
        # code Here

    def preorder(self, node,stop):
        # code Here

    def inorder(self, node,stop):
        # code Here

    def postorder(self, node,stop):
        # code Here

    def printMirrorTree(self, node, level=0):
        # code Here

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
print("What is this a plum tree")
first,inp = input('Enter Input : ').split('/')
first = first.split()
for i in first:
    T.append(i)
T.printTree(T.root)
print("********************************************")
inp = inp.split(',')
for i in inp:
    print(i)
    if i[:2] == "AP":
        T.append(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CU":
        T.cut(i[3:])
        T.printTree(T.root)
    elif i[:2] == "CH":
        print('preorder  :',end=' ')
        T.preorder(T.root,i[3:])
        print('\ninorder   :',end=' ')
        T.inorder(T.root,i[3:])
        print('\npostorder :',end=' ')
        T.postorder(T.root,i[3:])
        print()
    elif i[:2] == "MI":
        T.printMirrorTree(T.root)
    print("********************************************")
print("the last result")
T.printTree(T.root)
```

What is this a plum tree
Enter Input : H D O B F M Q/AP Z,CH H
FIrst look of this plum tree
           Q
      O
           M
 H
           F
      D
           B
********************************************
AP Z
                Z
           Q
      O
           M
 H
           F
      D
           B
********************************************
CH H
preorder  : 72 68 66 70 O M Q Z
inorder   : 66 68 70 72 M O Q Z
postorder : 66 70 68 M Z Q O 72
********************************************
the last result
                Z
           Q
      O
           M
 H
           F
      D
           B


What is this a plum tree
Enter Input : H D O A B F M Q/AP a,CU Q,CU Q
FIrst look of this plum tree
           Q
      O
           M
 H
           F
      D
                B
           A
********************************************
AP a
                a
           Q
      O
           M
 H
           F
      D
                B
           A
********************************************
CU Q
           Q
      O
           M
 H
           F
      D
                B
           A
********************************************
CU Q
Not thing change
           Q
      O
           M
 H
           F
      D
                B
           A
********************************************
the last result
           Q
      O
           M
 H
           F
      D
                B
           A


What is this a plum tree
Enter Input : Z M E H P N O Q X Y a b j x/AP v,MI
FIrst look of this plum tree
                     x
                j
           b
      a
 Z
                          Y
                     X
                Q
           P
                     O
                N
      M
                H
           E
********************************************
AP v
                     x
                          v
                j
           b
      a
 Z
                          Y
                     X
                Q
           P
                     O
                N
      M
                H
           E
********************************************
MI
           E
                H
      M
                N
                     O
           P
                Q
                     X
                          Y
 Z
      a
           b
                j
                          v
                     x
********************************************
the last result
                     x


What is this a plum tree
Enter Input : a g u Z Z E G H/AP a,CU a,CU a,CU a
FIrst look of this plum tree
           u
      g
 a
           Z
      Z
                     H
                G
           E
********************************************
AP a
           u
      g
           a
 a
           Z
      Z
                     H
                G
           E
********************************************
CU a
 a
           Z
      Z
                     H
                G
           E
********************************************
CU a
 a
********************************************
CU a
Not thing change
 a
********************************************
the last result
 a

"""


from typing import List


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data: str = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def get_code_points(self):
        # code_point = 0
        # for magnitude, char in enumerate(self.data[::-1]):
        #     code_point += ord(char) + ((2 ** (7 * magnitude)) - 1)

        # # print(self.data, code_point)
        # return code_point

        code_point = 0
        for magnitude, char in enumerate(self.data[::-1]):
            print(char, ord(char) * (1000 ** magnitude))
            code_point += ord(char) * (1000 ** magnitude)
        print(self.data, code_point)
        return code_point


        # code_point = ''
        # for char in self.data[::-1]:
        #     code_point += str(ord(char))
        # # print(self.data, code_point)
        # return int(code_point)


        # code_point = ord('A')
        # for char in self.data:
        #     code_point += ord(char) - ord('A')

        # print(self.data, code_point)
        # return code_point


        # return ord(self.data[0])

        # return ord(self.data[-1])


class Tree:
    def __init__(self):
        self.root = None

    def search(self, _node_data: str):
        queue = [self.root]
        while len(queue):
            current_node = queue.pop()
            if not current_node:
                continue
            if current_node.data == _node_data:
                return current_node
            queue.append(current_node.left)
            queue.append(current_node.right)

    def append(self, _node_data: str):
        new_node = TreeNode(_node_data)
        new_node_code_points = new_node.get_code_points()
        # print('new_node_code_points', new_node_code_points)

        if not self.root:
            self.root = new_node
            return

        previous_node = self.root
        current_node = self.root

        # print('data length' , _node_data, len(_node_data))
        if len(_node_data) >= 2:
            first_char_node = self.search(_node_data[0])
            if first_char_node:
                # print('set first char node to', first_char_node)
                previous_node = first_char_node
                current_node = first_char_node

        while current_node:
            previous_node = current_node
            if new_node_code_points < current_node.get_code_points():
                current_node = current_node.left
            else:
                current_node = current_node.right

        if new_node_code_points < previous_node.get_code_points():
            previous_node.left = new_node
        else:
            previous_node.right = new_node

    def cut(self, _node_data: str):
        node = self.search(_node_data=_node_data)

        if not node:
            return False

        if node.right:
            node.right = None
            return True

        if node.left:
            node.left = None
            return True

        return False

    def preorder(self, node: TreeNode) -> List[TreeNode]:
        _nodes: List[TreeNode] = []
        _nodes.append(node)
        if node.left:
            _nodes.extend(self.preorder(node=node.left))
        if node.right:
            _nodes.extend(self.preorder(node=node.right))
        return _nodes

    def inorder(self, node: TreeNode):
        _nodes: List[TreeNode] = []
        if node.left:
            _nodes.extend(self.inorder(node=node.left))
        _nodes.append(node)
        if node.right:
            _nodes.extend(self.inorder(node=node.right))
        return _nodes

    def postorder(self, node: TreeNode):
        _nodes: List[TreeNode] = []
        if node.left:
            _nodes.extend(self.postorder(node=node.left))
        if node.right:
            _nodes.extend(self.postorder(node=node.right))
        _nodes.append(node)
        return _nodes

    def get_traversal_code_points(self, _node_data: str):
        code_point = ''
        for char in _node_data:
            code_point += str(ord(char))
        return code_point

    def traversal_formatter(self, traversal_result, ascii_until):
        formatted = []
        for i in traversal_result:
            if len(i.data) == 1:
                if i.get_code_points() <= ord(ascii_until):
                    formatted.append(self.get_traversal_code_points(i.data))
                    continue
                formatted.append(str(i.data))
                continue

            elif ord(i.data[0]) < ord(ascii_until):
                formatted.append(self.get_traversal_code_points(i.data))
                continue
            formatted.append(str(i.data))
            continue
        return " ".join(formatted)

    def get_traversals(self, from_node, ascii_until):
        preorder_result = self.traversal_formatter(
            traversal_result=self.preorder(from_node), ascii_until=ascii_until
        )
        formatted_result = "preorder  : "
        formatted_result += preorder_result

        inorder_result = self.traversal_formatter(
            traversal_result=self.inorder(from_node), ascii_until=ascii_until
        )
        formatted_result += "\ninorder   : "
        formatted_result += inorder_result

        postorder_result = self.traversal_formatter(
            traversal_result=self.postorder(from_node), ascii_until=ascii_until
        )
        formatted_result += "\npostorder : "
        formatted_result += postorder_result

        return formatted_result

    def print_mirrored(self, node, level=0):
        if node is not None:
            self.print_mirrored(node.left, level + 1)
            print("     " * level, node)
            self.print_mirrored(node.right, level + 1)

    def print(self, node, level=0):
        if node is not None:
            self.print(node.right, level + 1)
            print("     " * level, node)
            self.print(node.left, level + 1)


tree = Tree()
print("What is this a plum tree")
nodes, commands = input("Enter Input : ").split("/")
nodes = nodes.split()
for node_data in nodes:
    tree.append(node_data)
print('FIrst look of this plum tree')
tree.print(tree.root)
print("********************************************")
commands = commands.split(",")
for command in commands:
    print(command)
    if command[:2] == "AP":
        tree.append(command[3:])
        tree.print(tree.root)
    elif command[:2] == "CU":
        RESULT = tree.cut(command[3:])
        if RESULT is False:
            print("Not thing change")
        tree.print(tree.root)
    elif command[:2] == "CH" and tree.root:
        FORMATTED = tree.get_traversals(from_node=tree.root, ascii_until=command[3:])
        print(FORMATTED)
    elif command[:2] == "MI":
        tree.print_mirrored(tree.root)
    print("********************************************")
print("the last result")
tree.print(tree.root)
