class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
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

    def __str__(self):
        return str(self.data)


class AVLTree:
    def __init__(self):
        self.root = None

    def postorder(self, node):
        _nodes = []
        if node.left:
            _nodes.extend(self.postorder(node=node.left))
        if node.right:
            _nodes.extend(self.postorder(node=node.right))
        _nodes.append(node)
        return _nodes

    def print(self):
        AVLTree.print_subtree(self, node=self.root)

    def print_subtree(self, node, level=0):
        if not node is None:
            AVLTree.print_subtree(self, node.right, level + 1)
            print("     " * level, node.data)
            AVLTree.print_subtree(self, node.left, level + 1)

    def rotate_left(self, node):
        # print(f'rotating left {node}')
        child = node.right
        if not child:
            raise AttributeError

        node.right = child.left
        child.left = node

        node.update_height()
        child.update_height()

        return child

    def rotate_right(self, node):
        # print(f'rotating right {node}')
        child = node.left
        if not child:
            raise AttributeError

        node.left = child.right
        child.right = node

        node.update_height()
        child.update_height()

        return child

    def rebalance(self, node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        # AVL Violation on right child
        if right_height > left_height:
            # Right Right imbalance -> Rotate Left
            if node.right and node.right.get_balance_factor() >= 0 :
                print('Left Left Rotation')
                node = self.rotate_left(node)
                return node

            # Right Left imbalance -> Rotate Right-Left
            if node.right and node.right.left and node.right.get_balance_factor() < 0:
                print('Right Left Rotation')
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)
                return node

        # AVL Violation on left child
        else:
            # Left Left imbalance -> Rotate Right
            if node.left and node.left.get_balance_factor() <= 0:
                print('Right Right Rotation')
                node = self.rotate_right(node)
                return node

            # Left Right imbalance -> Rotate Left-Right
            if node.left and node.left.right and node.left.get_balance_factor() > 0:
                print('Left Right Rotation')
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
                return node

    def rebalance_child(self, node):
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

    def _recursive_insert(self, current_node, to_insert):
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

    def insert(self, data):
        # print(f'inserting {data}')
        new_node = AVLNode(data=data)
        if self.root is None:
            self.root = new_node
            return
        self._recursive_insert(current_node=self.root, to_insert=new_node)
        self.rebalance_root()



tree = AVLTree()
print(' *** AVL Tree Insert Element ***')
inputs = input("Enter Input : ").split()
for item in inputs:
    print("insert :", item)
    tree.insert(int(item))
    tree.print()
    print("====================")