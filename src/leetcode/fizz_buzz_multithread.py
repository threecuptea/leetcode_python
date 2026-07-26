# https://leetcode.com/problems/fizz-buzz-multithreaded/

from threading import Semaphore
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.sem_f = Semaphore(0)
        self.sem_b = Semaphore(0)
        self.sem_fb = Semaphore(0)
        self.sem_n = Semaphore(1) # This can proceed because coming with one token
        self.done = False

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.sem_f.acquire()
            if self.done:
                break
            printFizz()
            self.sem_n.release() # increment 1 token so that self.sem_n can be acquire in the next round

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.sem_b.acquire()
            if self.done:
                break
            printBuzz()
            self.sem_n.release()

            # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.sem_fb.acquire()
            if self.done:
                break
            printFizzBuzz()
            self.sem_n.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem_n.acquire() # decrement token to 0 so that it cannot be aquired() again
            if i % 15 == 0:
                self.sem_fb.release()
            elif i % 3 == 0:
                self.sem_f.release()
            elif i % 5 == 0:
                self.sem_b.release()
            else:
                printNumber(i)
                self.sem_n.release()
        # Need to make sure all other sems finished their jobs
        self.sem_n.acquire()
        self.done = True
        self.sem_f.release()
        self.sem_b.release()
        self.sem_fb.release()
