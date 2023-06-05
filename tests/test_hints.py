from chatgpt.src.hints import Hints
import pytest


@pytest.mark.check_env("TEST_HINTS")
class TestCreateHints:
    def test__正常系_用意できているか(self, api_key):
        Chat = Hints(api_key, "東京タワー")

        assert len(Chat.get_hints()) == Chat.count
