from chatgpt.src.yes_or_no import YesOrNo
import pytest


@pytest.mark.check_env("TEST_YesOrNo")
class TestCreateYesOrNo:
    def test__正常系_用意できているか(self, api_key):
        Chat = YesOrNo(api_key, "東京タワー")

        assert Chat.talk("赤い?")["score"] >= 50
        assert Chat.talk("青い?")["score"] <= 10
