class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not len(self.data):
            None
        return self.data.pop(0)

    def search(self, index):
        if not (0 <= index <= len(self.data) - 1):
            raise IndexError
        return self.data[index]
