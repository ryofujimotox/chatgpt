from typing import Optional
from chatgpt.src.ai_chatbot import AIChatbot


class Quiz(AIChatbot):
    game_rule = """
## ゲームのルール

1. 出題者は「答え」を用意して、途中で変えることはできません。
2. この時、「答え」は決して公開しないでください。
3. 「答え」は日本人全員が知っているものです。
4. 参加者は出題者にさまざまな質問をします。出題者は「はい」「いいえ」「関係ありません」の3択で答えます。
5. 「いいえ」は答えの方向性は合っているが明確にNOと言える場合、「関係ありません」はその質問が答えから大きく遠ざかっている場合に使います。
6. 参加者が「答え」を見つけるか、参加者がギブアップするとゲームは終了します。その後、「答え」を公開します。

## 答えの例

- バナナ
- 車
- マクドナルド

## ゲームの開始
あなたが新しい問題を作成し、出題者として振る舞ってください。私は参加者としてあなたに質問します。それでは、ゲームを始めましょう！
"""

    def __init__(self, api_key: str, ai_model: Optional[str] = None) -> None:
        """
        QuizGameクラスの初期化メソッド。

        :param api_key: AI ChatbotのAPIキー
        :param ai_model: AIモデル名（任意）
        """
        super().__init__(
            api_key=api_key, ai_model=ai_model, system_content=self.game_rule
        )

    def start(self) -> bool:
        """
        ゲームをスタートするメソッド。ゲームの初期化を行い、セットアップメッセージを送信します。

        :return: セットアップが完了したかどうかを示す真偽値
        """
        # 問題の初期化
        self.initialize_system(self.game_rule)

        response = self.talk("用意ができたら、「setup」とだけ返事してください。")
        return "setup" in response
