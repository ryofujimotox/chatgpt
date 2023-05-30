from ai_chatbot import AIChatbot
from lib.get_env import env


class TestCreateQuiz:
    def test__正常系_正しい計算ができているか(self):
        if env("TEST_CHAT") == "0":
            return

        apikey = env("OPENAI_API_KEY")
        Chat = AIChatbot(api_key=apikey)
        response = Chat.talk("1+1=")
        assert response == "2"
