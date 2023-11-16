from advanced_topics.exercises.solutions.exercise_9 import slow_function, fast_function


class TestTimeDecorator:
    def test_slow_function(self, capsys):
        slow_function()
        captured = capsys.readouterr()
        assert "slow_function took" in captured.out

    def test_fast_function(self, capsys):
        fast_function()
        captured = capsys.readouterr()
        assert "fast_function took" in captured.out
