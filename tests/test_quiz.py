from chatgpt.src.quiz import Quiz
import pytest


@pytest.mark.check_env("TEST_QUIZ")
class TestCreateQuiz:
    def test__正常系_用意できているか(self, api_key):
        Chat = Quiz(api_key)
        assert Chat.start()
