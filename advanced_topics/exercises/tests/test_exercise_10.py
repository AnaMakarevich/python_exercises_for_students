import time

from advanced_topics.exercises.solutions.exercise_10 import Timer


def test_timer_output(capsys):
    with Timer():
        time.sleep(0.5)
    captured = capsys.readouterr()
    assert "Code execution took" in captured.out
