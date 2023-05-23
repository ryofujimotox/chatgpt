from ai_chatbot import AIChatbot


class Quiz(AIChatbot):
    # system初期化
    def __init__(self, api_key, ai_model=None):
        system_content = """
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

        super().__init__(
            api_key=api_key, system_content=system_content, ai_model=ai_model
        )

    # 問題の初期化
    def start(self):
        self.chat_history = []
        return self.talk("出題してください。")
