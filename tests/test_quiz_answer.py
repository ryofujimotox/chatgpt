from chatgpt.src.quiz_answers import QuizAnswers
import pytest


@pytest.mark.check_env("TEST_QuizAnswer")
class TestCreateQuizAnswer:
    def test__正常系_用意できているか(self, api_key):
        #
        Chat = QuizAnswers(api_key, "観光地")
        print(Chat)
        exit
