class NormalClass:
    pass


normal_obj1 = NormalClass()
normal_obj2 = NormalClass()

print(normal_obj1 is normal_obj2)  # False, both references point to different instances
print(normal_obj1 == normal_obj2)  # False, both references point to different instances


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # If the instance doesn't exist, create it
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# Example Usage:


obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True, both references point to the same instance
print(obj1 == obj2)  # True, both references point to the same instance
