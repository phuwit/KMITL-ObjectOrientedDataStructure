'''
basis for this chapter haha yes emoji freezing
'''


from typing import Any, List, Union


class SinglyLinkedNode:
    def __init__(self, item, next) -> None:
        self.__item: Any = item
        self.__next: SinglyLinkedNode | None = next

    @property
    def item(self) -> Any:
        return self.__item

    @item.setter
    def item(self, value: Any) -> None:
        self.__item = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value: Union['SinglyLinkedNode', None]) -> None:
        self.__next = value

    def __str__(self) -> str:
        return str(self.item)


class DoublyLinkedNode:
    def __init__(self, item, next, previous) -> None:
        self.__item: Any = item
        self.__next: DoublyLinkedNode | None = next
        self.__previous: DoublyLinkedNode | None = previous

    @property
    def item(self) -> Any:
        return self.__item

    @item.setter
    def item(self, value: Any) -> None:
        self.__item = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value: Union['DoublyLinkedNode', None]) -> None:
        self.__next = value

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value: Union['DoublyLinkedNode', None]) -> None:
        self.__previous = value

    def __str__(self) -> str:
        return str(self.item)


class SinglyLinkedList:
    def __init__(self, circular = False):
        self.__head: SinglyLinkedNode | None = None
        self.__circular: bool = circular

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        self.__head = value

    def __str__(self):
        if self.is_empty():
            return "Empty"
        if self.__head:
            current_node, string = self.__head, str(self.__head.item) + " "
            while current_node.next is not None:
                string += str(current_node.next.item) + " "
                current_node = current_node.next
            return string[:-1:]

    def is_empty(self):
        return self.__head is None

    def append(self, item):
        new_node = SinglyLinkedNode(item=item, next=None)
        if not self.__head:
            self.__head = new_node
            return
        current_node = self.__head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def append_head(self, item):
        old_node = self.__head
        new_node = SinglyLinkedNode(item=item, next=old_node)
        self.__head = new_node

    def search(self, item):
        current_node = self.__head
        while current_node:
            if current_node.item == item:
                return current_node
            current_node = current_node.next
        return None

    def get_index(self, item):
        index = 0
        current_node = self.__head
        while current_node:
            if current_node.item == item:
                return index
            index += 1
            current_node = current_node.next
        return -1

    def size(self):
        size = 0
        current_node = self.__head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def pop(self, pos):
        index = 1
        if pos > self.size() - 1 or pos < 0:
            return "Out of Range"
        elif pos == 0 and self.__head and not self.__head.next:
            self.__head = None
            return "Success"
        elif self.__head and self.__head.next:
            pre_node = self.__head
            current_node = self.__head.next

            while current_node.next:
                if index == pos:
                    pre_node.next = current_node.next
                    return "Success"
                index += 1
                pre_node = current_node
                current_node = current_node.next
        return "Out of Range"


class DoublyLinkedList:
    def __init__(self, circular = False):
        self.__head: DoublyLinkedNode | None = None
        self.__circular: bool = circular

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        self.__head = value

    def __str__(self):
        if self.is_empty():
            return "Empty"
        if self.__head:
            current_node, string = self.__head, str(self.__head.item) + " "
            while current_node.next is not None:
                string += str(current_node.next.item) + " "
                current_node = current_node.next
            return string[:-1:]

    def append(self, item) -> None:
        new_node = DoublyLinkedNode(item=item, next=None, previous=None)
        if not self.__head:
            self.__head = new_node
            return

        current_node = self.__head
        while current_node.next and current_node.next != self.__head:
            current_node = current_node.next
        new_node.previous = current_node
        current_node.next = new_node

        if self.__circular:
            new_node.next = self.__head
            self.__head.previous = new_node

    def append_head(self, item):
        old_node = self.__head
        new_node = DoublyLinkedNode(item=item, next=old_node, previous=None)
        self.__head = new_node

    def is_empty(self):
        return self.__head is None

    def search(self, item):
        current_node = self.__head
        while current_node:
            if current_node.item == item:
                return current_node
            current_node = current_node.next
        return None

    def get_index(self, item):
        index = 0
        current_node = self.__head
        while current_node:
            if current_node.item == item:
                return index
            index += 1
            current_node = current_node.next
        return -1

    def size(self):
        size = 0
        current_node = self.__head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    def pop(self, pos):
        index = 1
        if pos > self.size() - 1 or pos < 0:
            return "Out of Range"
        elif pos == 0 and self.__head and not self.__head.next:
            self.__head = None
            return "Success"
        elif self.__head and self.__head.next:
            pre_node = self.__head
            current_node = self.__head.next

            while current_node.next:
                if index == pos:
                    pre_node.next = current_node.next
                    return "Success"
                index += 1
                pre_node = current_node
                current_node = current_node.next
        return "Out of Range"