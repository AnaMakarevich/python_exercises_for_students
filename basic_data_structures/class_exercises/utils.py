from pathlib import Path

import pytest


def get_test_path(file_path: Path):
    test_file_name = f"test_{file_path.name}"
    parent_dir = file_path.parent.name
    tests_dir = Path(__file__).parent.parent / "tests"
    return tests_dir / parent_dir / test_file_name

def test_my_solution(file_path: Path):
    test_file = str(get_test_path(file_path))
    pytest.main([test_file])
