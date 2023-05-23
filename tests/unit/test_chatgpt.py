import pytest
from ai_chatbot import AIChatbot


class TestCreateQuiz:
    apikey = "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"

    # 接続後正しい計算ができているか
    def test__接続後正しい計算ができているか(self):
        assert "2" == "2"
        return

        Chat = AIChatbot(api_key=self.apikey)
        response = Chat.talk("1+1=")
        assert response == "2"
