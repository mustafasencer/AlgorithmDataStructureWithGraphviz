import sys


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def __str__(self) -> str:
        return " ".join([str(i) for i in self.queue])

    def is_empty(self):
        return self.queue == []

    def insert(self, data) -> None:
        self.queue.append(data)

    def delete(self):
        try:
            max_value = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_value]:
                    max_value = i
            item = self.queue[max_value]
            del self.queue[max_value]
            return item
        except IndexError:
            sys.exit()


if __name__ == "__main__":
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    while not myQueue.is_empty():
        pass
