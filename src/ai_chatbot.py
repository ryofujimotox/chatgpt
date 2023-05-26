import openai
from typing import Optional, List, Dict


class AIChatbot:
    chat_history: List[Dict[str, str]] = []  # チャット設定を記録するリスト
    ai_model: str = "gpt-3.5-turbo"  # デフォルトのAIモデルは 'gpt-3.5-turbo'
    system_content: str = None

    def __init__(
        self,
        api_key: str,
        system_content: Optional[str] = None,
        ai_model: Optional[str] = None,
    ) -> None:
        """
        AIChatbotクラスの初期化メソッド。

        Parameters:
            api_key (str): OpenAIのAPIキー
            system_content (str, optional): 初期メッセージとして追加するシステムコンテンツ
            ai_model (str, optional): 使用するAIモデル

        Returns:
            None
        """
        self.__set_api_key(api_key)

        if system_content:
            self.system_content = system_content

        if ai_model:
            self.ai_model = ai_model

        self.initialize_system()

    def initialize_system(self) -> None:
        """
        AIアシスタントの設定などをチャット設定に追加するメソッド。

        Returns:
            None
        """

        self.chat_history: List[str] = []
        self.__add_system_content()

    def talk(self, user_message: str) -> str:
        """
        ユーザーメッセージをチャット設定に追加し、AIからのレスポンスを取得するメソッド。

        Parameters:
            user_message (str): ユーザーからのメッセージ

        Returns:
            str: AIアシスタントからのレスポンスメッセージ
        """
        self.__add_user_message(user_message)  # ユーザーメッセージを追加

        ai_response = openai.ChatCompletion.create(
            model=self.ai_model, messages=self.chat_history
        )
        ai_message = ai_response["choices"][0]["message"]["content"].lstrip()
        token_count = ai_response["usage"]["total_tokens"]

        self.__add_ai_message(ai_message)  # AIアシスタントのメッセージを追加
        return ai_message

    def __set_api_key(self, api_key: str) -> None:
        """
        OpenAIのAPIキーを設定するメソッド。

        Parameters:
            api_key (str): OpenAIのAPIキー

        Returns:
            None
        """
        openai.api_key = api_key

    def __add_system_content(self) -> None:
        """
        AIアシスタントの設定などをチャット設定に追加するメソッド。

        Returns:
            None
        """
        if not self.system_content:
            return

        self.chat_history.append({"role": "system", "content": self.system_content})

    def __add_user_message(self, user_message: str) -> None:
        """
        ユーザーメッセージをチャット設定に追加するメソッド。

        Parameters:
            user_message (str): ユーザーメッセージ

        Returns:
            None
        """
        self.chat_history.append({"role": "user", "content": user_message})

    def __add_ai_message(self, ai_message: str) -> None:
        """
        AIアシスタントのメッセージをチャット設定に追加するメソッド。

        Parameters:
            ai_message (str): AIアシスタントのメッセージ

        Returns:
            None
        """
        self.chat_history.append({"role": "assistant", "content": ai_message})
