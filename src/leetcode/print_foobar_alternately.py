# https://leetcode.com/problems/print-foobar-alternately/

from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_f = Lock() # Semaphore(1)
        self.lock_b = Lock() # Semaphore(0)
        self.lock_b.acquire() # Both Semaphore and Lock can work well

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_f.acquire()
            try:
                printFoo()
            finally:
                self.lock_b.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_b.acquire()
            try:
                printBar()
            finally:
                self.lock_f.release()  