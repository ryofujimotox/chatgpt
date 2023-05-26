import pytest
from Game.quiz import Quiz
from lib.get_env import get as env


class TestCreateQuiz:
    def test__正常系_用意できているか(self):
        if env("TEST_QUIZ") == "0":
            return

        apikey = env("OPENAI_API_KEY")
        Chat = Quiz(apikey)
        response = Chat.start()
        assert response == "setup"
