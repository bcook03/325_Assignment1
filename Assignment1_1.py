def greeter(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper

@greeter
def greet(greeting):
    print(greeting)

greet("Hello, World!")