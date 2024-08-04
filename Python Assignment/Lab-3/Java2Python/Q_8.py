# Write a Java program to implement stack using array.

class Stack:
    def __init__(self, capacity):
        """Initialize the stack with a given capacity."""
        self.capacity = capacity
        self.stack = []  # Using a Python list to represent the stack
        self.top = -1    # To track the index of the top element in the stack

    def push(self, value):
        """Push a value onto the stack."""
        if self.is_full():
            print("Stack is full! Cannot push more elements.")
            return

        self.stack.append(value)
        self.top += 1
        print(f"Pushed {value} to stack. Current stack: {self.stack}")

    def pop(self):
        """Pop the top value from the stack."""
        if self.is_empty():
            print("Stack is empty! Cannot pop elements.")
            return None

        value = self.stack.pop()
        self.top -= 1
        print(f"Popped {value} from stack. Current stack: {self.stack}")
        return value

    def peek(self):
        """Return the top value of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty! No elements to peek.")
            return None

        value = self.stack[self.top]
        print(f"Peeked value: {value}")
        return value

    def is_empty(self):
        """Check if the stack is empty."""
        return self.top == -1

    def is_full(self):
        """Check if the stack is full."""
        return self.top == self.capacity - 1

    def size(self):
        """Return the current size of the stack."""
        current_size = self.top + 1
        print(f"Current stack size: {current_size}")
        return current_size

def main():
    stack_capacity = int(input("Enter the Size of Stack: "))
    stack = Stack(stack_capacity)

    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Exit")
        choice = int(input("Enter your Choice: "))

        match choice:
            case 1:
                val = int(input("Enter the value: "))
                stack.push(val)

            case 2: 
                stack.pop()

            case 3: 
                stack.peek()

            case 4: 
                stack.size()

            case 5: 
                print("Exiting...")
                exit()
            
            case default: 
                print("Wrong input!")
    
if __name__ == "__main__":
    main()
