
import time
from functools import lru_cache


@lru_cache(maxsize=5)
def func(n):
    time.sleep(n)
    return n


if __name__ == '__main__':

    func(4)
    print("done")
    func(4)
    print("done")
    func(4)
    print("done")
    func(4)
