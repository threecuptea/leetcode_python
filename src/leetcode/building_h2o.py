# https://leetcode.com/problems/building-h2o/description

from threading import Semaphore, Barrier
class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.barrier = Barrier(3) # It requires wait() to be called 3 times before move on


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        # the following line is similar to sem_h.acquire() then try except
        with self.sem_h:
            self.barrier.wait()
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:

        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.sem_o:
            self.barrier.wait()
            releaseOxygen()