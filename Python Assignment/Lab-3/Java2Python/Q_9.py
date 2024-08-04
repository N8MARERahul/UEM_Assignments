# Write a Java program to implement Queue using array.

class Queue:
    def __init__(self, capacity):
        """Initialize the queue with a given capacity."""
        self.capacity = capacity
        self.queue = []  # Using a Python list to represent the queue
        self.front = 0   # The front index
        self.rear = -1   # The rear index
        self.size = 0    # Current size of the queue

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        if self.is_full():
            print("Queue is full! Cannot enqueue more elements.")
            return

        self.rear += 1
        self.queue.append(value)
        self.size += 1
        print(f"Enqueued {value}. Current queue: {self.queue}")

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.is_empty():
            print("Queue is empty! Cannot dequeue elements.")
            return None

        value = self.queue[self.front]
        self.queue.pop(self.front)
        self.size -= 1
        print(f"Dequeued {value}. Current queue: {self.queue}")
        return value

    def peek(self):
        """Get the front element of the queue without removing it."""
        if self.is_empty():
            print("Queue is empty! No elements to peek.")
            return None

        value = self.queue[self.front]
        print(f"Front element: {value}")
        return value

    def current_size(self):
        """Return the current size of the queue."""
        print(f"Current queue size: {self.size}")
        return self.size

# Example Usage
def main():
    queue_capacity = int(input("Enter the Size of Queue: "))
    queue = Queue(queue_capacity)

    while True:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Size")
        print("5. Exit")
        choice = int(input("Enter your Choice: "))

        match choice:
            case 1:
                val = int(input("Enter the value: "))
                queue.enqueue(val)

            case 2: 
                queue.dequeue()

            case 3: 
                queue.peek()

            case 4: 
                queue.current_size()

            case 5: 
                print("Exiting...")
                exit()
            
            case default: 
                print("Wrong input!")

if __name__ == "__main__":
    main()
