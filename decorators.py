import time

def decorator_timer_fx(func):
    def wrapper(*args, **kwargs):          # Its a Closure ; *args so it works with ANY function
        start = time.time()
        print('Before!')
        result = func(*args, **kwargs)     # run the actual function
        end = time.time()
        print('After!')
        print(f"took {end - start:.2f}s")
        return result
    return wrapper

class decorator_timer_class(object):

    def __init__(self,original_func):
        self.original_func = original_func

    def __call__(self,*args,**kwargs):
        print('call method executed before {}'.format(self.original_func.__name__))
        return self.original_func(*args,**kwargs)
    
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done")
        return result
    return wrapper

@log_call
def ask_ai(question):
    return "42"



# @decorator_timer_fx  # Same as saying slow_computation = timer(slow_computation(n))
# def slow_computation(n):
#     time.sleep(3)
#     print('Function is running')
#     return n * 2

@decorator_timer_class  # Can use a class as a decorator too
def slow_computation(n):
    time.sleep(3)
    print('Function is running')
    return n * 2

slow_computation(5)   # prints: took 1.00s