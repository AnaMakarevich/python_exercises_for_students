import time

from advanced_topics.exercises.exercises.exercise_10 import MyTimer


def test_timer_output(capsys):
    with MyTimer():
        time.sleep(0.5)
    captured = capsys.readouterr()
    assert "Code execution took" in captured.out
