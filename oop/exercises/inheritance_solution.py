class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"{self.name} - ${self.salary}")

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.salary})"


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage_team(self):
        print(f"Manager {self.name} is managing the team")


class TeamLead(Manager):
    def __init__(self, name: str, salary: float, team_size: int, projects: list):
        super().__init__(name, salary, team_size)
        self.team_size = team_size
        self.projects = projects

    def plan_projects(self):
        print(f"Team lead {self.name} is planning projects")


class Developer(Employee):
    def __init__(self, name: str, salary: float, tasks: list):
        super().__init__(name, salary)
        self.tasks = tasks

    def perform_tasks(self):
        print(f"Developer {self.name} is performing tasks")


if __name__ == "__main__":
    print(dir(Manager))
