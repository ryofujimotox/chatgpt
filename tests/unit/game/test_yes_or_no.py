from Game.yes_or_no import YesOrNo
from lib.get_env import env


class TestCreateYesOrNo:
    def test__正常系_用意できているか(self):
        if env("TEST_YesOrNo") == "0":
            return

        apikey = env("OPENAI_API_KEY")
        Chat = YesOrNo(apikey, "東京タワー")
        assert Chat.talk("赤いですか") == 1
