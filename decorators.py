import time

def timer(func):
    def wrapper(*args, **kwargs):          # Its a Closure ; *args so it works with ANY function
        start = time.time()
        print('Before!')
        result = func(*args, **kwargs)     # run the actual function
        end = time.time()
        print('After!')
        print(f"took {end - start:.2f}s")
        return result
    return wrapper

@timer  # Same as saying slow_computation = timer(slow_computation(n))
def slow_computation(n):
    time.sleep(3)
    print('Function is running')
    return n * 2

slow_computation(5)   # prints: took 1.00s