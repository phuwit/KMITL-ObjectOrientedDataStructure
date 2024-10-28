class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def get_code_points(self):
        code_point = 0
        for magnitude, char in enumerate(self.data[::-1]):
            # print(char, ord(char) * (1000 ** magnitude))
            code_point += ord(char) * (1000**magnitude)
        # print(self.data, code_point)
        return code_point


class Tree:
    def __init__(self):
        self.root = None

    def search(self, _node_data):
        queue = [self.root]
        while len(queue):
            current_node = queue.pop()
            if not current_node:
                continue
            if current_node.data == _node_data:
                return current_node
            queue.append(current_node.left)
            queue.append(current_node.right)

    def append(self, _node_data):
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

    def cut(self, _node_data):
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

    def preorder(self, node):
        _nodes = []
        _nodes.append(node)
        if node.left:
            _nodes.extend(self.preorder(node=node.left))
        if node.right:
            _nodes.extend(self.preorder(node=node.right))
        return _nodes

    def inorder(self, node):
        _nodes = []
        if node.left:
            _nodes.extend(self.inorder(node=node.left))
        _nodes.append(node)
        if node.right:
            _nodes.extend(self.inorder(node=node.right))
        return _nodes

    def postorder(self, node):
        _nodes = []
        if node.left:
            _nodes.extend(self.postorder(node=node.left))
        if node.right:
            _nodes.extend(self.postorder(node=node.right))
        _nodes.append(node)
        return _nodes

    def get_traversal_code_points(self, _node_data):
        code_point = ""
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

            if ord(i.data[0]) < ord(ascii_until):
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
print("FIrst look of this plum tree")
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
