from typing import List, Tuple


class AVLNode:
    def __init__(self, data, left=None, right=None):
        self.data: int = data
        self.left: "AVLNode | None" = left
        self.right: "AVLNode | None" = right
        self.height = self.update_height()

    def __str__(self):
        return str(self.data)

    def update_height(self):
        a = self.getHeight(self.left)
        b = self.getHeight(self.right)
        self.height = 1 + max(a, b)
        return self.height

    def getHeight(self, node):
        if node is None:
            return -1
        return node.height

    def get_balance_factor(self):
        return self.getHeight(self.right) - self.getHeight(self.left)


class AVLTree:
    def __init__(self, root=None):
        self.root = None if root is None else root

    def subtree_rotate_left(self, current: AVLNode, child: AVLNode) -> AVLNode:
        # print(f"Rotating left: {current.data} -> {child.data}")
        # self.printTree()
        current.right = child.left
        child.left = current
        current.update_height()
        child.update_height()
        return child

    def subtree_rotate_right(self, current: AVLNode, child: AVLNode) -> AVLNode:
        # print(f"Rotating right: {current.data} -> {child.data}")
        # self.printTree()
        current.left = child.right
        child.right = current
        current.update_height()
        child.update_height()
        return child

    def get_childs(self, node: AVLNode):
        childs: List[Tuple[AVLNode, AVLNode]] = []
        if node.left:
            childs.append((node, node.left))
        if node.right:
            childs.append((node, node.right))
        return childs

    def rebalance_subtree(self, node: AVLNode):
        if node.get_balance_factor() <= 1 and node.get_balance_factor() >= -1:
            return None
        if node.left:
            left_grandchilds = self.get_childs(node.left)
            for child, grandchild in left_grandchilds:
                # left left imbalance -> rotate right
                if child.get_balance_factor() <= 0:
                    return self.subtree_rotate_right(node, child)

                # left right imbalance -> rotate left right
                else:
                    node.left = self.subtree_rotate_left(child, grandchild)
                    return self.subtree_rotate_right(node, node.left)

        if node.right:
            right_grandchilds = self.get_childs(node.right)
            for child, grandchild in right_grandchilds:
                # right right imbalance -> rotate left
                if child.get_balance_factor() >= 0:
                    return self.subtree_rotate_left(node, child)

                # right left imbalance -> rotate right left
                else:
                    node.right = self.subtree_rotate_right(child, grandchild)
                    return self.subtree_rotate_left(node, node.right)
        return None

    def append(self, node_data):
        new_node = AVLNode(node_data, None, None)
        # print(f"Inserting: {new_node.data}")

        if not self.root:
            self.root = new_node
            return

        previous_node = self.root
        current_node = self.root
        traversed_nodes: List[AVLNode] = []
        while current_node:
            traversed_nodes.append(current_node)
            previous_node = current_node
            if new_node.data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if new_node.data < previous_node.data:
            previous_node.left = new_node
        else:
            previous_node.right = new_node

        node_to_replace: None | AVLNode = None
        new_node: None | AVLNode = None
        for node in traversed_nodes[::-1]:
            node.update_height()
            if node_to_replace and new_node:
                if node.left == node_to_replace:
                    node.left = new_node
                elif node.right == node_to_replace:
                    node.right = new_node
                break
            result = self.rebalance_subtree(node)
            if result is None:
                continue
            if node == self.root:
                self.root = result
            new_node = result
            node_to_replace = node
            continue

    def postorder(self, node: AVLNode):
        _nodes: List[AVLNode] = []
        if node.left:
            _nodes.extend(self.postorder(node=node.left))
        if node.right:
            _nodes.extend(self.postorder(node=node.right))
        _nodes.append(node)
        return _nodes

    def printTree(self):
        AVLTree._printTree(self, node=self.root)
        print()

    def _printTree(self, node, level=0):
        if not node is None:
            AVLTree._printTree(self, node.right, level + 1)
            print("     " * level, node.data)
            AVLTree._printTree(self, node.left, level + 1)


avl1 = AVLTree()
inp = input("Enter Input : ").split(",")
for i in inp:
    if i[:2] == "AD":
        avl1.append(int(i[3:]))
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        if avl1.root:
            postorder_result = ' '.join(map(str, avl1.postorder(avl1.root)))
            print(f'AVLTree post-order : {postorder_result}')
        else:
            print('AVLTree post-order : ')
    print(i)
    avl1.printTree()
    print('===========================')