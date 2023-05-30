from typing import Optional, List
from chatgpt.src.ai_chatbot import AIChatbot
import re


class Hints(AIChatbot):
    """AI Chatbotを使用して、特定の答えに関連する難しいヒントを生成するクラス。

    Attributes:
        count (int): 提供するヒントの数。
        answer (Optional[str]): 答え。初期値はNone。
    """

    count: int = 5
    answer: Optional[str] = None
    hints: List[str] = []

    def __init__(
        self, api_key: str, answer: str, ai_model: Optional[str] = None
    ) -> None:
        """初期化メソッド。

        Parameters:
            api_key (str): AI ChatbotのAPIキー。
            answer (str): 答え。
            ai_model (Optional[str]): 使用するAIモデル。指定がなければNone。
        """
        super().__init__(
            api_key=api_key,
            ai_model=ai_model,
            system_content=self._generate_game_rule(),
        )
        self.restart(answer)

    def _generate_game_rule(self) -> str:
        """ゲームルールを生成する。

        Returns:
            str: ゲームルールの文字列。
        """
        return f"""Provide {self.count} clues related to your answer.
Start with poetic, abstract clues and gradually move to more direct, concrete clues.
Each clue should be no more than 20 words.
全て日本語で書いてください。

Format:
1. a
2. b
3. c"""

    def restart(self, answer: str) -> List[str]:
        """問題を初期化する。

        Parameters:
            answer (str): 答え。

        Returns:
            List[str]: 生成されたヒントのリスト。
        """
        self.answer = answer
        self.initialize_system(self._generate_game_rule())

        return self.generate()

    def generate(self) -> List[str]:
        response = super().talk("Answer: " + self.answer)

        #
        hints = self._parse_response_into_clues(response)
        if not len(hints) == self.count:
            return self.restart(self.answer)

        self.hints = hints
        return self.hints

    def get_hints(self) -> List[str]:
        return self.hints

    def _parse_response_into_clues(self, response: str) -> List[str]:
        """応答を解析して、ヒントのリストを生成する。

        Parameters:
            response (str): 応答の文字列。

        Returns:
            List[str]: ヒントのリスト。
        """
        # 改行で分割してリストにする
        list_of_sentences = response.split("\n")

        # 空の要素を取り除き、先頭の数字とピリオドを取り除く
        clues = [
            re.sub(r"^\d+\.", "", sentence).strip()
            for sentence in list_of_sentences
            if sentence.strip()
        ]

        return clues
