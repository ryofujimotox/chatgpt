from chatgpt.src.quiz import Quiz
from chatgpt.tests.lib.get_env import env


class TestCreateQuiz:
    def test__正常系_用意できているか(self):
        if env("TEST_QUIZ") == "0":
            return

        apikey = env("OPENAI_API_KEY")
        Chat = Quiz(apikey)
        assert Chat.start()
