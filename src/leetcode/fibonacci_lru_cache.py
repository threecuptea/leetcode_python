from functools import lru_cache
import argparse

# Python has LRU cache.  We can easily use it as an annotation.
@lru_cache(maxsize=100)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def main(fibonacci_range):
    fibs = [fib(n) for n in range(fibonacci_range)]
    print(fibs)
    print(fib.cache_info())

if __name__ == "__main__":
    parser = argparse.ArgumentParser('A simple program that implement "fibonacci" using lru_cache')
    # Make Fibonacci range dynamic
    parser.add_argument('numbers', type=int, help='Fibonacci range to generate') # positional arguments
    # parser.add_argument('-n', '--numbers', type=int, help='Fibonacci range to generate')
    args = parser.parse_args()
    main(args.numbers)
