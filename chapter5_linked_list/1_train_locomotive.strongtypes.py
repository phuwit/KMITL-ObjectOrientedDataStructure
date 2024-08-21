class Node[T]:
    def __init__(self, item: 'T', next_node: 'Node | None'):
        self.item = item
        self.next = next_node

    def __str__(self) -> str:
        return str(self.item)


class SinglyLinkedList[T]:
    def __init__(self):
        self.head: Node | None = None
        self.__iterator_current = None

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
        current_node = self.head
        if not current_node:
            return 0
        length = 1
        while current_node.next:
            current_node = current_node.next
            length += 1
            continue
        return length

    def __getitem__(self, index) -> Node[T] | None:
        current_index = 0
        for item in self:
            if current_index >= index:
                return item
            current_index += 1

    def __str__(self) -> str:
        items = list(str(i) for i in self)
        return ' <- '.join(items)

    def append(self, item: 'T', index: None | int = None):
        new_node = Node(item=item, next_node=None)
        if not self.head:
            self.head = new_node
            return new_node

        current_node = self.head

        if index:
            current_index = 0
            while current_node.next and index >= current_index :
                current_node = current_node.next
                current_index += 1
                continue
            next_node = current_node.next
            current_node.next = new_node
            new_node.next = next_node
            return new_node

        while current_node.next:
            current_node = current_node.next
            continue
        current_node.next = new_node
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
