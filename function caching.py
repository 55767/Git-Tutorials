import time
from functools import lru_cache
@lru_cache(maxsize=32)
def some_work(n):
    time.sleep(n)
    return n
    #some task doinf in n seconds

if __name__== '__main__':
    print("Now running a task")
    some_work(2)
    print("Calling the person......")
    some_work(3)
    print("Done")
    some_work(3)
    input()
    print("now say to call whom?")



