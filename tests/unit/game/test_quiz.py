import pytest
from Game.quiz import Quiz
from lib.get_env import get as env


class TestCreateQuiz:
    # 接続後正しい計算ができているか
    def test__接続後正しい計算ができているか(self):
        apikey = env("OPENAI_API_KEY")
        
        Chat = Quiz(apikey)
        response = Chat.start()
        return
    
        assert response == "2"
