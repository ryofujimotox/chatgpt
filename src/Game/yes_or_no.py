from typing import Optional
from ai_chatbot import AIChatbot


class YesOrNo(AIChatbot):
    game_rule = """Simulate statistical data.
Format: Number(closer to 100 for more 'yes'; closer to 0 for more 'no')-Justification(20 characters)"""

    answer: str = None

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
        self.initialize_system()

    def talk(self, user_message: str) -> bool:
        """
        ゲームをスタートするメソッド。ゲームの初期化を行い、セットアップメッセージを送信します。

        Parameters:
            user_message (str): ユーザーからのメッセージ

        :return: セットアップが完了したかどうかを示す真偽値
        """

        response = super().talk(self.answer + "は、" + user_message)
        splited = self.split(response)
        return splited

    def split(self, response: str):
        data = response.split("-")
        return data
