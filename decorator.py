def outer()
    pass

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
hello()

