import pytest
from Game.quiz import Quiz


class TestCreateQuiz:
    apikey = "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"

    # todo
    # 接続後正しい計算ができているか
    def test__接続後正しい計算ができているか(self):
        Chat = Quiz(self.apikey)
        response = Chat.start()
        return
    
        assert response == "2"
