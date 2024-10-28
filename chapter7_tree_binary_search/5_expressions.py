"""
Chapter : 7 - item : 5 - Expression Tree

ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /


Enter Postfix : ab+cde+**
Tree :
                e
           +
                d
      *
           c
 *
           b
      +
           a
--------------------------------------------------
Infix : ((a+b)*(c*(d+e)))
Prefix : *+ab*c+de


Enter Postfix : abc*+de*f+g*+
Tree :
           g
      *
                f
           +
                     e
                *
                     d
 +
                c
           *
                b
      +
           a
--------------------------------------------------
Infix : ((a+(b*c))+(((d*e)+f)*g))
Prefix : ++a*bc*+*defg


Enter Postfix : ab+c*de-fg+*-
Tree :
                g
           +
                f
      *
                e
           -
                d
 -
           c
      *
                b
           +
                a
--------------------------------------------------
Infix : (((a+b)*c)-((d-e)*(f+g)))
Prefix : -*+abc*-de+fg

"""

from typing import List


class TreeNode:
    def __init__(self, data: str):
        self.data = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def __str__(self):
        return str(self.data)

    def is_orphan(self):
        if self.left and self.right:
            return False
        return True


class Tree:
    def __init__(self, root: TreeNode | None = None):
        self.root = None
        if root is not None:
            self.root = root

    def insert(self, node_data: str):
        new_node = TreeNode(node_data)

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

    def print(self, node: TreeNode | None = None, level=0):
        if node is not None:
            self.print(node.right, level + 1)
            print("     " * level, node)
            self.print(node.left, level + 1)

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

    def infix_expressions(self, node: TreeNode):
        result: str = ""

        if not node.is_orphan():
            result += "("

        if node.left:
            result += self.infix_expressions(node=node.left)
        result += str(node)
        if node.right:
            result += self.infix_expressions(node=node.right)

        if not node.is_orphan():
            result += ")"
        print(result)
        return result

    def traversal_formatter(self, traversal_result: List[TreeNode], seperator: str):
        formatted = []
        for i in traversal_result:
            formatted.append(str(i.data))
        return seperator.join(formatted)


class Stack:
    def __init__(self, ls=None):
        if ls is None:
            self.__stack: List[TreeNode] = []
        else:
            self.__stack = ls

    def push(self, i: TreeNode):
        self.__stack.append(i)

    def pop(self):
        return self.__stack.pop()

    def isEmpty(self):
        return bool(self.__stack)

    def size(self):
        return len(self.__stack)


def postfix_parser(tokens: List[str]):
    stack = Stack()
    expressions_token = "+-*/"
    for token in tokens:
        if token in expressions_token:
            n2 = stack.pop()
            n1 = stack.pop()
            token_node = TreeNode(token)
            token_node.left = n1
            token_node.right = n2
            stack.push(token_node)
            continue
        stack.push(TreeNode(token))
        continue
    return stack.pop()


input_tokens = list(i for i in input("Enter Postfix : "))
# print(input_tokens)

tree = Tree(postfix_parser(input_tokens))
print("Tree :")
tree.print(tree.root)

print("--------------------------------------------------")

if tree.root:
    infix_result = tree.infix_expressions(tree.root)
    print(f"Infix : {infix_result}")
    prefix_result = tree.traversal_formatter(
        traversal_result=tree.preorder(tree.root), seperator=""
    )
    print(f"Prefix : {prefix_result}")
