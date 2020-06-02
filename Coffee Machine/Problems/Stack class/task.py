class Stack():

    def __init__(self):
        self.list = []

    def push(self, el):
        self.list.append(el)

    def pop(self):
        x = self.list[-1]
        self.list.remove(x)
        return x

    def peek(self):
        return self.list[-1]

    def is_empty(self):
        return not self.list
