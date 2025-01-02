"""
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
"""

from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def peek(self):
        raise NotImplementedError

    @abstractmethod
    def pop(self):
        raise NotImplementedError

    @abstractmethod
    def push(self, x: int) -> None:
        raise NotImplementedError


class MyQueue(Queue):
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        while self.stack:
            self.temp.append(self.stack.pop())
        self.stack.append(x)
        while self.temp:
            self.stack.append(self.temp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)

    peeked = queue.peek()
    popped = queue.pop()

    print(peeked)
    print(popped)
