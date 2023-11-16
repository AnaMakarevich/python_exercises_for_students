import pytest

from advanced_topics.exercises.exercises.exercise_6 import Configuration
from advanced_topics.exercises.tests.utils import skip_if_not_implemented


@pytest.mark.skipif(condition=True, reason="Method not implemented")
class TestConfiguration:
    @skip_if_not_implemented
    def test_basic_usage(self):
        config1 = Configuration()
        config2 = Configuration()
        assert config1 is config2

    @skip_if_not_implemented
    def test_setting_and_getting(self):
        config1 = Configuration()
        config2 = Configuration()
        config1.set_setting("language", "English")
        config2.set_setting("theme", "Light")
        assert config1.get_setting("language") == "English"
        assert config1.get_setting("theme") == "Light"

    @skip_if_not_implemented
    def test_updating_settings(self):
        config1 = Configuration()
        config2 = Configuration()
        config1.set_setting("theme", "Dark")
        assert config2.get_setting("theme") == "Dark"

    @skip_if_not_implemented
    def test_adding_new_setting(self):
        config1 = Configuration()
        config2 = Configuration()
        config2.set_setting("font_size", 14)
        assert config1.get_setting("font_size") == 14
