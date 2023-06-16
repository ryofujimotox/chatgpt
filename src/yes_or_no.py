from typing import Optional
from chatgpt.src.ai_chatbot import AIChatbot
from chatgpt.src.hints import Hints


class YesOrNo(AIChatbot):
    game_rule = """Grade the accuracy of the questions on a scale of 0-100.
Format: {"score":0~100,"description":10-word in Japanese}"""

    answer: str = None

    hints: Hints = None

    def __init__(
        self, api_key: str, answer: str, ai_model: Optional[str] = None
    ) -> None:
        """
        YesOrNoクラスの初期化メソッド。

        :param api_key: AI ChatbotのAPIキー
        :param answer: 答え
        :param ai_model: AIモデル名（任意）
        """
        super().__init__(
            api_key=api_key, ai_model=ai_model, system_content=self.game_rule
        )
        self.restart(answer)

    def restart(self, answer: str):
        # 問題の初期化
        self.answer = answer

        # ヒント
        self.hints = None

        # 初期化
        self.initialize_system(self.game_rule)

    def get_hinsts(self):
        if self.hints is None:
            self.hints = Hints(self.api_key, self.answer)

        return self.hints.get()

    def talk(self, message: str) -> dict:
        """
        ゲームをスタートするメソッド。ゲームの初期化を行い、セットアップメッセージを送信します。

        Parameters:
            message (str): ユーザーからのメッセージ

        :return: セットアップが完了したかどうかを示す真偽値
        """

        response = super().talk("Question: " + self.answer + "は、" + message)
        data = self.__parse_response(response)
        return data

    def __parse_response(self, response: str) -> dict:
        """
        応答を解析してデータを返すメソッド。

        Parameters:
            response (str): 応答の文字列

        Returns:
            dict: 解析されたデータ
        """

        data = response.split(" - ")
        data = {"score": int(data[0]), "description": data[1]}
        return data
