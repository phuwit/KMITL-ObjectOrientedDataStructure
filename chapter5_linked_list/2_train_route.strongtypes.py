class Node[T]:
    def __init__(self, item: 'T', next_node: 'Node | None'):
        self.item = item
        self.next = next_node

    def __str__(self) -> str:
        return str(self.item)


class DoublyLinkedNode:
    def __init__(self, item, next, previous):
        self.__item = item
        self.__next = next
        self.__previous = previous

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        self.__item = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value):
        self.__previous = value

    def __str__(self):
        return str(self.item)


class SinglyLinkedList:
    def __init__(self, circular=False):
        self.__head = None
        self.__circular = circular

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
        new_node = Node(item=item, next=None)
        if not self.__head:
            self.__head = new_node
            return
        current_node = self.__head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def append_head(self, item):
        old_node = self.__head
        new_node = Node(item=item, next=old_node)
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
    def __init__(self, circular=False):
        self.__head = None
        self.__circular = circular

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

    def append(self, item):
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

def get_forward_route(start, terminate):
    route = SinglyLinkedList()
    current_node = start
    while current_node != terminate:
        if current_node:
            route.append(item=current_node.item)
            current_node = current_node.next
            continue
        break
    route.append(item=current_node.item)
    return route


def get_backward_route(start, terminate):
    route = SinglyLinkedList()
    current_node = start
    while current_node != terminate:
        if current_node:
            route.append(item=current_node.item)
            current_node = current_node.previous
            continue
        break
    route.append(item=current_node.item)
    return route

print('***Railway on route***')
stations_string, routing_string = input('Input Station name/Source, Destination, Direction(optional): ').split('/')

routing_data = routing_string.split(',')
routing_direction = None
if len(routing_data) >= 3:
    routing_direction = routing_data.pop()
start_name, terminate_name = routing_data


stations = DoublyLinkedList(circular=True)

for station_name in stations_string.split(','):
    stations.append(item=station_name)

station_start = stations.search(item=start_name)
station_terminate = stations.search(item=terminate_name)


if station_start and station_terminate:
    if routing_direction:
        if routing_direction == 'F':
            route = get_forward_route(start=station_start, terminate=station_terminate)
            route_string = str(route).replace(' ', '->')
            route_size = route.size() - 1
            print(f'Forward Route: {route_string},{route_size}')
        elif routing_direction == 'B':
            route = get_backward_route(start=station_start, terminate=station_terminate)
            route_string = str(route).replace(' ', '->')
            route_size = route.size() - 1
            print(f'Backward Route: {route_string},{route_size}')

    else:
        forward_route = get_forward_route(start=station_start, terminate=station_terminate)
        backward_route = get_backward_route(start=station_start, terminate=station_terminate)

        if (forward_route.size() <= backward_route.size()):
            route = forward_route
            route_string = str(route).replace(' ', '->')
            route_size = route.size() - 1
            print(f'Forward Route: {route_string},{route_size}')
        if (backward_route.size() <= forward_route.size()):
            route = backward_route
            route_string = str(route).replace(' ', '->')
            route_size = route.size() - 1
            print(f'Backward Route: {route_string},{route_size}')