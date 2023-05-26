import openai


class AIChatbot:
    chat_history = []  # チャット設定を記録するリスト
    ai_model = "gpt-3.5-turbo"  # デフォルトのAIモデルは 'gpt-3.5-turbo'

    def __init__(self, api_key, system_content=None, ai_model=None):
        # 初期設定メソッド。APIキーの設定、初期メッセージの追加、AIモデルの選択を行う
        self.__set_api_key(api_key)

        if system_content:
            self.set_system(system_content)

        if ai_model:
            self.ai_model = ai_model

    def set_system(self, system_content):
        # AIアシスタントの設定などをチャット設定に追加するメソッド
        self.__add_system_content(system_content)

    def talk(self, user_message):
        # ユーザーメッセージをチャット設定に追加し、AIからのレスポンスを取得するメソッド
        self.__add_user_message(user_message)  # ユーザーメッセージを追加

        ai_response = openai.ChatCompletion.create(
            model=self.ai_model, messages=self.chat_history
        )
        ai_message = ai_response["choices"][0]["message"]["content"].lstrip()
        token_count = ai_response["usage"]["total_tokens"]

        self.__add_ai_message(ai_message)  # AIアシスタントのメッセージを追加
        return ai_message

    def __set_api_key(self, api_key):
        # OpenAIのAPIキーを設定するメソッド
        openai.api_key = api_key

    def __add_system_content(self, system_content):
        # AIアシスタントの設定などをチャット設定に追加するメソッド
        self.chat_history.append({"role": "system", "content": system_content})

    def __add_user_message(self, user_message):
        # ユーザーメッセージをチャット設定に追加するメソッド
        self.chat_history.append({"role": "user", "content": user_message})

    def __add_ai_message(self, ai_message):
        # AIアシスタントのメッセージをチャット設定に追加するメソッド
        self.chat_history.append({"role": "assistant", "content": ai_message})
