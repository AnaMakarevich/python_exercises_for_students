import pytest

class_names = ['Manager', 'TeamLead', 'Developer']
skip_tests = {class_name: False for class_name in class_names}

for class_name in class_names:
    try:
        exec(f"from oop.exercises.inheritance_exercise import {class_name}")
    except ImportError:
        skip_tests[class_name] = True


@pytest.mark.skipif(skip_tests['Manager'], reason="Manager class is not implemented")
class TestManager:
    def test_manager_inheritance(self):
        manager = Manager("Alice Manager", 80000.0, 10)  # type: ignore
        assert manager.__class__.__bases__[0].__name__ == "Employee"

    def test_manager_attributes(self):
        manager = Manager("Alice Manager", 80000.0, 10)  # type: ignore
        assert manager.name == "Alice Manager"
        assert manager.salary == 80000.0
        assert manager.team_size == 10

    def test_manager_methods(self):
        class_methods = dir(Manager)  # type: ignore
        assert "manage_team" in class_methods, "manage_team method is missing"
        assert "display_info" in class_methods, "display_info method is missing"
        assert "lead_team" not in class_methods, "lead_team method is not supposed to be in Manager class"


@pytest.mark.skipif(skip_tests['TeamLead'], reason="TeamLead class is not implemented")
class TestTeamLead:
    def test_team_lead_inheritance(self):
        team_lead = TeamLead("Charlie Lead", 100000.0, 15, ["Project A", "Project B"])  # type: ignore
        assert team_lead.__class__.__bases__[0].__name__ == "Manager"

    def test_team_lead_attributes(self):
        team_lead = TeamLead("Charlie Lead", 100000.0, 15, ["Project A", "Project B"])  # type: ignore
        assert team_lead.name == "Charlie Lead"
        assert team_lead.salary == 100000.0
        assert team_lead.team_size == 15
        assert team_lead.projects == ["Project A", "Project B"]

    def test_team_lead_methods(self):
        class_methods = dir(TeamLead)  # type: ignore
        assert "manage_team" in class_methods, "manage_team method is missing"
        assert "display_info" in class_methods, "display_info method is missing"
        assert "plan_projects" in class_methods, "plan_projects method is missing"


@pytest.mark.skipif(skip_tests['Developer'], reason="Developer class is not implemented")
class TestDeveloper:
    def test_developer_inheritance(self):
        developer = Developer("Bob Worker", 50000.0, ["Task 1", "Task 2"])  # type: ignore
        assert developer.__class__.__bases__[0].__name__ == "Employee"

    def test_developer_attributes(self):
        developer = Developer("Bob Worker", 50000.0, ["Task 1", "Task 2"]) # type: ignore
        assert developer.name == "Bob Worker"
        assert developer.salary == 50000.0
        assert developer.tasks == ["Task 1", "Task 2"]

    def test_developer_methods(self):
        class_methods = dir(Developer)  # type: ignore
        assert "perform_tasks" in class_methods, "perform_tasks method is missing"
        assert "display_info" in class_methods, "display_info method is missing"
        assert "manage_team" not in class_methods, "manage_team method is not supposed to be in Developer class"
