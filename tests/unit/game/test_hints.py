from Game.hints import Hints
from lib.get_env import env


class TestCreateHints:
    def test__正常系_用意できているか(self):
        if env("TEST_HINTS") == "0":
            return

        apikey = env("OPENAI_API_KEY")
        Chat = Hints(apikey, "東京タワー")

        assert len(Chat.get_hints()) == Chat.count
