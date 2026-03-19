class MinStack:

    def __init__(self):
        self.stack = []       # основной стек
        self.min_stack = []   # стек минимумов

    def push(self, val):
        self.stack.append(val)

        # если стек минимумов пуст или новый элемент меньше
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        # если удаляем минимум — убираем и из min_stack
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]