Decorators in Python are a powerful and flexible way to modify the behavior of functions or methods. They allow you to wrap another function in order to extend its behavior without permanently modifying it. Here’s a detailed explanation and examples to illustrate how decorators work:

### How Decorators Work

A decorator is a function that takes another function as an argument, and returns a new function that usually extends the behavior of the original function. Decorators are often used for logging, enforcing access control, instrumentation, caching, and more.

### Basic Structure of a Decorator

Below is a simple example of a decorator that prints a message before and after the execution of a function.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Explanation:

1. **Define the Decorator:**
   - `my_decorator` is defined as a function that takes another function `func` as an argument.
   - Inside `my_decorator`, a nested function `wrapper` is defined, which adds some behavior before and after calling `func`.
   - `my_decorator` returns the `wrapper` function.

2. **Apply the Decorator:**
   - The `@my_decorator` syntax is a shorthand for applying `my_decorator` to `say_hello`.
   - This is equivalent to: `say_hello = my_decorator(say_hello)`

3. **Call the Function:**
   - When `say_hello` is called, it is actually the `wrapper` function that gets executed.

### More Practical Example: Logging

Here’s a more practical example of using a decorator to log the execution of functions.

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Example usage:
sum_result = add(5, 3)
print(sum_result)

greeting_message = greet("Alice", greeting="Hi")
print(greeting_message)
```

### Explanation:

1. **Define the Decorator:**
   - `log_function_call` is defined to log the name of the function being called, its arguments, and its return value.
   - The `wrapper` function uses `*args` and `**kwargs` to handle any number of positional and keyword arguments.

2. **Apply the Decorator:**
   - The `@log_function_call` syntax applies the `log_function_call` decorator to `add` and `greet`.

3. **Call the Functions:**
   - When `add(5, 3)` is called, the `wrapper` function logs the call and the result.
   - Similarly, `greet("Alice", greeting="Hi")` logs the call and the result.

### Summary

Decorators are a powerful feature in Python that allows you to modify the behavior of functions in a clean and readable way. They are widely used for logging, enforcing access control, and other cross-cutting concerns. By understanding and using decorators, you can write more modular and maintainable code.
