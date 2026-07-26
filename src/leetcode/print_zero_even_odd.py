# https://leetcode.com/problems/print-zero-even-odd

from threading import Semaphore
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.sem_z = Semaphore(1)
        self.sem_o = Semaphore(0)
        self.sem_e = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem_z.acquire()
            printNumber(0)
            (self.sem_e if i % 2 == 0 else self.sem_o).release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.sem_e.acquire()
            printNumber(i)
            self.sem_z.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.sem_o.acquire()
            printNumber(i)
            self.sem_z.release()