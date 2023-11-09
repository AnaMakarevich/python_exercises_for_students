from abc import ABC, abstractmethod


# Interface for workers who can work
class WorkInterface(ABC):
    @abstractmethod
    def work(self):
        pass


# Interface for workers who can eat
class EatInterface(ABC):
    @abstractmethod
    def eat(self):
        pass


# Worker classes implementing specific interfaces
class Manager(WorkInterface, EatInterface):
    def work(self):
        print("Manager is working")

    def eat(self):
        print("Manager is eating")


class Developer(WorkInterface):
    def work(self):
        print("Developer is working")


if __name__ == '__main__':
    manager = Manager()
    developer = Developer()

    # All workers can work
    manager.work()
    developer.work()

    # Workers who can eat also eat
    if isinstance(manager, EatInterface):
        manager.eat()

    # Developer class does not have to implement an unnecessary method
    # No need to check isinstance for EatInterface
