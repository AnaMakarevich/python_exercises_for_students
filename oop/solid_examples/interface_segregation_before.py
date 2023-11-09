from abc import ABC, abstractmethod


# Interface for workers who can work and eat
class WorkEatInterface(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


# Worker class implementing the full interface
class Manager(WorkEatInterface):
    def work(self):
        print("Manager is working")

    def eat(self):
        print("Manager is eating")


# Worker class implementing the interface but doesn't need to eat
class Developer(WorkEatInterface):
    def work(self):
        print("Developer is working")

    # Developer class is forced to implement unnecessary method
    def eat(self):
        print("I must implement this method but only my manager can eat!")


if __name__ == '__main__':
    manager = Manager()
    developer = Developer()

    # All workers can work
    manager.work()
    developer.work()

    # Workers who can eat also eat
    if isinstance(manager, WorkEatInterface):
        manager.eat()

    # Developer class has to implement an unnecessary method
    if isinstance(developer, WorkEatInterface):
        developer.eat()
