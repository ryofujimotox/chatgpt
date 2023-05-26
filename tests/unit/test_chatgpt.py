import pytest
from ai_chatbot import AIChatbot
from lib.get_env import get as env


class TestCreateQuiz:
    # 接続後正しい計算ができているか
    def test__接続後正しい計算ができているか(self):
        if env("TEST_CHAT") == "0":
            return
        
        apikey = env("OPENAI_API_KEY")
        Chat = AIChatbot(api_key=apikey)
        response = Chat.talk("1+1=")
        assert response == "2"
