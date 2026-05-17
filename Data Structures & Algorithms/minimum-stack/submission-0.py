class MinStack:

    def __init__(self):
        self.array = []

    def push(self, val: int) -> None:
        self.array.append(val)

    def pop(self) -> None:
        if self.array:
            del self.array[-1]

    def top(self) -> int:
        if self.array:
            return self.array[-1]

    def getMin(self) -> int:
        if self.array:
            min_value = self.array[-1]
            for value in self.array:
                if value < min_value:
                    min_value = value
            return min_value

        
