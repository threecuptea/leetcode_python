import threading
from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        """
        Initializes the queue with a fixed maximum capacity.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.queue = deque()

        # Mutex to guard the internal deque modification
        self.lock = threading.Lock()

        # Tracks available spaces for producers to write
        self.track_full = threading.Semaphore(capacity)

        # Tracks available elements for consumers to read
        self.track_empty = threading.Semaphore(0)

    def size(self) -> int:
        """
        Returns the current number of elements in the queue safely.
        """
        with self.lock:
            return len(self.queue)

    def enqueue(self, element) -> None:
        """
        Adds an element to the queue. Blocks if the queue is full.
        """
        self.track_full.acquire()
        with self.lock:
            self.queue.append(element)
        self.track_empty.release()

    def dequeue(self):
        """
        Removes and returns an element from the queue. Blocks if the queue is empty.
        """
        self.track_empty.acquire()
        with self.lock:
            e = self.queue.popleft()
        self.track_full.release()
        return e






