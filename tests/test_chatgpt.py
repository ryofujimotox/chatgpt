from chatgpt.src.ai_chatbot import AIChatbot
import pytest


@pytest.mark.check_env("TEST_CHAT")
class TestCreateQuiz:
    def test__正常系_正しい計算ができているか(self, api_key):
        Chat = AIChatbot(api_key=api_key)
        response = Chat.talk("1+1=")
        assert response == "2"
