import time

def new_decorator(func):
    def wrapper():
        tic = time.perf_counter()
        func()
        toc = time.perf_counter()
        print(f"Runtime:{toc - tic:0.7f} seconds")
    return wrapper

@new_decorator
def print_hello_world():
    print("Hello World")

@new_decorator
def print_hello_world_longer():
    time.sleep(0.25)
    print("Hello World")

print_hello_world()
print_hello_world_longer()