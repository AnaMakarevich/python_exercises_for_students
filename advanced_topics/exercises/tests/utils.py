def skip_if_not_implemented(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except NotImplementedError:
            pass

    return wrapper