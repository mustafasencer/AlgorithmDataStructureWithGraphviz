class PriorityQueue:
	def __init__(self):
		self.queue = []

	def __str__(self):
		return " ".join([str(i) for i in self.queue])

	def is_empty(self):
		return self.queue == []

	def insert(self, data):
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
			print()
			exit()


if __name__ == "__main__":
	myQueue = PriorityQueue()
	myQueue.insert(12)
	myQueue.insert(1)
	myQueue.insert(14)
	myQueue.insert(7)
	print(myQueue)
	while not myQueue.is_empty():
		print(myQueue.delete())
