import openai


class ChatGPT:
    chat = []
    model = "gpt-3.5-turbo"

    # APIキー設定
    def setupKey(self, apikey):
        openai.api_key = apikey

    # 最初の設定
    def setupSystem(self, systemContent):
        self.chat.append({"role": "system", "content": systemContent})

    # 送信メッセージをchat配列に追加する
    def appendText(self, message):
        self.chat.append({"role": "user", "content": message})

    # 過去のやり取りをchat配列に追加する
    def appendAssistant(self, message):
        self.chat.append({"role": "assistant", "content": message})

    # chat配列を送信して、返信を待機する
    def talk(self, message):
        self.appendText(message)

        response = openai.ChatCompletion.create(model=self.model, messages=self.chat)
        msg = response["choices"][0]["message"]["content"].lstrip()

        self.appendAssistant(msg)
        return msg

    # セットアップ
    def __init__(self, apikey, systemContent):
        self.setupKey(apikey)
        self.setupSystem(systemContent)
