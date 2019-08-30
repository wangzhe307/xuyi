import time
import functools
def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        a = func(*args,**kwargs)
        end = time.time()
        print(round(end-start,2))
        return a
    return wrapper

@decorator
def fn():
    time.sleep(2)
    print('test')
    pass

fn()
