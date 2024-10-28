class Node[T]:
    def __init__(self, item: "T", next_node: "Node | None"):
        self.item = item
        self.next = next_node

    def __str__(self) -> str:
        return str(self.item)


class SinglyLinkedList[T]:
    def __init__(self):
        self.head: Node | None = None
        self.__iterator_current = None
        self.__length = 0

    def __iter__(self):
        self.__iterator_current = self.head
        if not self.__iterator_current:
            raise StopIteration
        return self

    def __next__(self):
        if self.__iterator_current is None:
            raise StopIteration
        previous = self.__iterator_current
        self.__iterator_current = self.__iterator_current.next
        return previous

    def __len__(self) -> int:
        return self.__length

    def __getitem__(self, index) -> Node:
        if index >= len(self):
            raise IndexError
        current_index = 0
        for item in self:
            if current_index >= index:
                return item
            current_index += 1
        raise IndexError

    def __str__(self) -> str:
        items = list(str(i) for i in self)
        return " <- ".join(items)

    def append(self, item: "T", index: None | int = None):
        new_node = Node(item=item, next_node=None)
        if not self.head:
            self.head = new_node
            self.__length += 1
            return new_node

        if index:
            current_node = self[index]
            next_node = current_node.next
            new_node.next = next_node
        else:
            current_node = self[len(self) - 1]

        current_node.next = new_node
        self.__length += 1
        return new_node


print(" *** Locomotive ***")
before = input("Enter Input : ").split()

train = SinglyLinkedList()

for i in before:
    train.append(int(i))

print(f"Before : {train}")

for node in train:
    if node.next and node.next.item == 0:
        new_tail = node
        new_head = node.next
        train_length = len(train)
        old_head = train.head
        old_tail = train[train_length - 1]

        new_tail.next = None
        train.head = new_head
        if old_tail:
            old_tail.next = old_head

print(f"After : {train}")
