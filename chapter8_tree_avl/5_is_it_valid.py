class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            self.num += 1
        else:
            h = get_node_height(self.root)
            max_node = pow(2, h + 1) - 1
            current = self.root
            if self.num + 1 > max_node:
                while current.left is not None:
                    current = current.left
                current.left = TreeNode(val)
                self.num += 1
            elif self.num + 1 == max_node:
                while current.right is not None:
                    current = current.right
                current.right = TreeNode(val)
                self.num += 1
            else:
                if self.num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
                    insert_subtree(current.left, self.num - round(pow(2, h) / 2), val)
                else:
                    insert_subtree(current.right, self.num - pow(2, h), val)
                self.num += 1


def insert_subtree(r, num, val):
    if r is not None:
        h = get_node_height(r)
        max_node = pow(2, h + 1) - 1
        current = r
        if num + 1 > max_node:
            while current.left is not None:
                current = current.left
            current.left = TreeNode(val)
            return
        elif num + 1 == max_node:
            while current.right is not None:
                current = current.right
            current.right = TreeNode(val)
            return
        if num + 1 <= max_node - ((max_node - (pow(2, h) - 1)) / 2):
            insert_subtree(current.left, num - round(pow(2, h) / 2), val)
        else:
            insert_subtree(current.right, num - pow(2, h), val)
    else:
        return


def get_node_height(root):
    if root is None:
        return -1
    else:
        left = get_node_height(root.left)
        right = get_node_height(root.right)
        if left > right:
            return left + 1
        else:
            return right + 1


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print("     " * level, node)
        print_tree(node.left, level + 1)


def is_valid_bst_node(node):
    current = node.data
    if not 0 <= node.data <= 100:
        return False

    if node.right and not node.right.data > current:
        return False
    if node.left and not node.left.data < current:
        return False
    return True


def is_valid_bst_tree(root, data_encountered):
    if root is None:
        return True

    if root.data in data_encountered:
        return False
    data_encountered.append(root.data)

    result = is_valid_bst_node(root)

    if root.left:
        result = result and is_valid_bst_tree(root.left, data_encountered)

    if root.right:
        result = result and is_valid_bst_tree(root.right, data_encountered)

    return result



tree = Tree()
tree_inputs = input("Enter Input : ").split()
for e in tree_inputs:
    tree.insert(int(e))

print_tree(tree.root)
print(is_valid_bst_tree(tree.root, []))
