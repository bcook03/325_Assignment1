# CS 325 Assignment 1
Brennan Cook (brecook@siue.edu)

## First Python File 
The first python being uplodaded is a simple Hello World program using a decorator.

<code>
def greeter(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper

@greeter
def greet(greeting):
    print(greeting)

greet("Hello, World!")
</code>
(A file is also included with the proper indentation)

### Charlie's Picture
This a picture of my cat Charlie. We've had her for about 8 years now.

[Charlie]()
