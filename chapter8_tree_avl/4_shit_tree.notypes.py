class AVLNode:
    def __init__(self, data) -> None:
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

    def __str__(self) -> str:
        return str(self.data)


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def get_vertical_image(self, node: AVLNode | None) -> "tuple[list, int, int, int]":
        """
        return
        - tree image: list[str]
        - left spacing: int
        - value width: int
        - right spacing: int
        """
        if node is None:
            return [], 0, 0, 0
        left_subtree, lf, lv, lb = self.get_vertical_image(node.left)
        right_subtree, rf, rv, rb = self.get_vertical_image(node.right)
        data = str(node.data)
        if not left_subtree and not right_subtree:
            return [data], 0, len(data), 0
        add_left, add_right = int(bool(left_subtree)), int(bool(right_subtree))
        line = (
            (" " * (lf + lv) + "/" + " " * (lb)) * add_left
            + " " * len(data)
            + (" " * rf + "\\" + " " * (rv + rb)) * add_right
        )
        out = [
            " " * (lf + lv + add_left)
            + "_" * lb
            + data
            + "_" * rf
            + " " * (rv + rb + add_right),
            line,
        ]
        if len(left_subtree) > len(right_subtree):
            right_subtree.extend([" " * (rf + rv + rb)] * (len(left_subtree) - len(right_subtree)))
        elif len(left_subtree) < len(right_subtree):
            left_subtree.extend([" " * (lf + lv + lb)] * (len(right_subtree) - len(left_subtree)))
        for left_node, right_node in zip(left_subtree, right_subtree):
            out.append(left_node + " " * (len(data) + add_left + add_right) + right_node)
        return out, (lf + lv + lb + add_left), len(data), (rf + rv + rb + add_right)

    def inorder(self, node):
        _nodes = []
        if node.left:
            _nodes.extend(self.inorder(node=node.left))
        _nodes.append(node)
        if node.right:
            _nodes.extend(self.inorder(node=node.right))
        return _nodes

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

    def find_node(self, data):
        if not self.root:
            return None
        traversed_nodes = []
        current_node = self.root
        while current_node is not None:
            traversed_nodes.append(current_node)
            if data == current_node.data:
                break

            if data > current_node.data:
                current_node = current_node.right
            else:
                current_node = current_node.left
        else:
            return None
        return traversed_nodes


good_tree = AVLTree()
straighten_at, straighten_direction, datas = input("Enter input: ").split(",")
for insert_data in map(int, datas.split()):
    good_tree.insert(data=insert_data)

print("Before")
good_image = good_tree.get_vertical_image(good_tree.root)
print("\n".join(good_image[0]))
print("-" * sum(good_image[1:]))

shit_tree = AVLTree()
shit_tree.root = good_tree.root

straighten_at = int(straighten_at)
straighten_from_node = shit_tree.find_node(straighten_at)
if straighten_from_node:
    # get sorted datas
    inorder_nodes = shit_tree.inorder(straighten_from_node[-1])
    inorder_datas = [i.data for i in inorder_nodes]

    if straighten_direction == "right":
        inorder_datas = inorder_datas[::-1]

    # create new straightened nodes
    straightened_node_root = AVLNode(inorder_datas.pop())
    current_node = straightened_node_root
    while inorder_datas:
        data = inorder_datas.pop()
        if straighten_direction == "right":
            current_node.right = AVLNode(data)
            current_node = current_node.right
        else:
            current_node.left = AVLNode(data)
            current_node = current_node.left

    # insert node into tree
    if shit_tree.root and straighten_from_node[-1].data == shit_tree.root.data:
        shit_tree.root = straightened_node_root

    elif straighten_at >= straighten_from_node[-2].data:
        straighten_from_node[-2].right = straightened_node_root
    elif straighten_at < straighten_from_node[-2].data:
        straighten_from_node[-2].left = straightened_node_root

    print("After")
    shit_image = shit_tree.get_vertical_image(shit_tree.root)
    print("\n".join(shit_image[0]))
else:
    print(f"No {straighten_at} in this tree")
