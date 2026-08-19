class MinStack:
    def __init__(self):
        # We will store tuples of (value, current_min)
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            # If stack is empty, the first value is also the minimum
            self.stack.append((val, val))
        else:
            # Compare the new value with the current minimum at the top of the stack
            current_min = self.stack[-1][1]
            self.stack.append((val, min(val, current_min)))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1 # Or raise an exception depending on requirements

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return -1 # Or raise an exception depending on requirements