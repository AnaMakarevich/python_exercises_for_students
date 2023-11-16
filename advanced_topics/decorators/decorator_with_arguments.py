def repeat(n):
    # top level: decorator factory
    def decorator(func):
        # nested: decorator function that performs some action around the original function
        def wrapper(*args, **kwargs):
            # nested: the call to the original function via the wrapper that
            # allows us to pass the original arguments
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
