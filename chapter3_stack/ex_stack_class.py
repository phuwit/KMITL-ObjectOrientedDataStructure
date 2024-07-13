"""
    example on how to create a stack class
"""

from typing import List, TypeVar, Union


class Stack:
    """
    create an empty stack
    then log the total number of initialized stacks into initialized_stacks
    """
    T = TypeVar('T')
    initialized_stacks = 0
    def __init__(self, init_list: Union[List[T], None] = None) -> None:
        if init_list is not None:
            self.items = init_list
            self.size = len(init_list)
        else:
            self.items = []
            self.size = 0
        self.initialized_stacks += 1

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()