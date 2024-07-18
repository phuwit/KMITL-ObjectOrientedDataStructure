"""
Chapter : 5 - item : 1 - Locomotive-(101)

มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)


 *** Locomotive ***
Enter Input : 2 3 1 0 4 5 6
Before : 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6
After : 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1


 *** Locomotive ***
Enter Input : 1 2 3 0
Before : 1 <- 2 <- 3 <- 0
After : 0 <- 1 <- 2 <- 3
"""

from typing import Any, List, Union


class Node:
    def __init__(self, item, next) -> None:
        self.__item: Any = item
        self.__next: Node | None = next

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
    def next(self, value: Union["Node", None]) -> None:
        self.__next = value

    def __str__(self) -> str:
        return str(self.item)


class SinglyLinkedList:
    def __init__(self, _list: List[Node]) -> None:
        self.__list: List[Node] = _list
        self.__head: Node | None = None
        self.__tail: Node | None = None
        if self.__list:
            self.__head = self.__list[0]
            self.__tail = self.__list[-1]

    @property
    def list(self) -> List[Node]:
        return self.__list

    @list.setter
    def list(self, value: List[Node]) -> None:
        self.__list = value
        if self.__list:
            self.__head = self.__list[0]
            self.__tail = self.__list[-1]

    @property
    def head(self) -> Node | None:
        return self.__head

    @head.setter
    def head(self, value: Node | None) -> None:
        self.__head = value

    @property
    def tail(self) -> Node | None:
        return self.__tail

    @tail.setter
    def tail(self, value: Node | None) -> None:
        self.__tail = value

    def add_at_index(self, index: int, item: Any):
        current_node = self.__list[index]
        new_node = Node(item=item, next=self.__list[index])
        if current_node != self.__head:
            previous_node = self.__list[index - 1]
            previous_node.next = new_node

    def append(self, item: Any):
        new_node = Node(item=item, next=None)
        if not self.__head:
            self.__head = new_node
        if self.__tail:
            self.__tail.next = new_node
        self.__list.append(new_node)
        self.__tail = new_node


print(" *** Locomotive ***")
before = input("Enter Input : ").split()
BEFORE_FORMATTED = " <- ".join(before)
print(f"Before : {BEFORE_FORMATTED}")

train_before = SinglyLinkedList([])
before_ll = [train_before.append(int(n)) for n in before]

for i in before:
    train_before.append(int(i))

for node in train_before.list:
    if node.next and node.next.item == 0:
        train_locomotive = node.next
        node_item = node.item
        node = Node(node_item, next=None)
        if train_before.tail and train_before.head:
            train_before.tail.next = train_before.head
        train_before.head = train_locomotive

        train_after = SinglyLinkedList([train_before.head])
        if train_before.head.next:
            node = train_before.head.next
            while node.next and node.item != 0:
                train_after.append(str(node.item))
                node = node.next
        break

after = [str(i) for i in train_after.list]

AFTER_FORMATTED = " <- ".join(after)
print(f"After : {AFTER_FORMATTED}")
