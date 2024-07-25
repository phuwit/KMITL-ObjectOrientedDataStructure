class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class Vim:
    def __init__(self):
        cursor_node = DoublyLinkedNode("|")
        self.head_node = cursor_node
        self.tail_node = cursor_node

    def search(self, target_value):
        current_node = self.head_node
        while current_node:
            if current_node.value == target_value:
                return current_node
            current_node = current_node.next
        print("Cursor not found")
        return None

    def insert(self, new_value):
        new_node = DoublyLinkedNode(new_value)
        cursor_node = self.search("|")
        if cursor_node is None:
            return

        new_node.next = cursor_node
        new_node.previous = cursor_node.previous
        if cursor_node.previous:
            cursor_node.previous.next = new_node
        cursor_node.previous = new_node
        if cursor_node == self.head_node:
            self.head_node = new_node

    def move_left(self):
        cursor_node = self.search("|")
        if cursor_node is None:
            return

        if cursor_node.previous:
            previous = cursor_node.previous
            if previous.previous:
                previous.previous.next = cursor_node
            cursor_node.previous = previous.previous
            previous.previous = cursor_node
            previous.next = cursor_node.next
            if cursor_node.next:
                cursor_node.next.previous = previous
            cursor_node.next = previous
            if self.head_node == previous:
                self.head_node = cursor_node

    def move_right(self):
        cursor_node = self.search("|")
        if cursor_node is None:
            return

        if cursor_node.next:
            next = cursor_node.next
            cursor_node.next = next.next
            if next.next:
                next.next.previous = cursor_node
            next.next = cursor_node
            next.previous = cursor_node.previous
            if cursor_node.previous:
                cursor_node.previous.next = next
            cursor_node.previous = next
            if self.head_node == cursor_node:
                self.head_node = next

    def backspace(self):
        cursor_node = self.search("|")
        if cursor_node is None:
            return

        if cursor_node.previous:
            previous = cursor_node.previous
            cursor_node.previous = previous.previous
            if previous.previous:
                previous.previous.next = cursor_node
            if self.head_node == previous:
                self.head_node = cursor_node

    def delete(self):
        cursor_node = self.search("|")
        if cursor_node is None:
            return

        if cursor_node.next:
            next = cursor_node.next
            cursor_node.next = next.next
            if next.next:
                next.next.previous = cursor_node
            if self.tail_node == next:
                self.tail_node = cursor_node

    def show(self):
        current_node = self.head_node
        linked_list_values = []
        while current_node:
            linked_list_values.append(current_node.value)
            current_node = current_node.next
        return " ".join(linked_list_values)

user_input = input("Enter Input : ").split(",")
commands_list = []

for command_input in user_input:
    commands_list.append(command_input.split())

vim = Vim()

for command in commands_list:
    action = command[0]
    word = None

    if len(command) == 2:
        word = command[1]

    if action == "I":
        vim.insert(word)
    elif action == "L":
        vim.move_left()
    elif action == "R":
        vim.move_right()
    elif action == "B":
        vim.backspace()
    elif action == "D":
        vim.delete()
    else:
        print("Command", action, "not found")

print(vim.show())