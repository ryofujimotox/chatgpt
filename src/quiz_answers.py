from typing import Optional, List
from chatgpt.src.ai_chatbot import AIChatbot
import json


class QuizAnswers(AIChatbot):
    def get_system_content(self, topic_title):
        return f"""
- We're going to play a guessing game. 
- You'll have to generate ‘Answer’ and I'll think of an ‘Answer'.
- Generate a list of 10 ‘Answers'.
- The difficulty level should be easy.
- The 'Answers' must be written in Japanese Kanji.
Format: { "answers": ["Answer1", "Answer2", "..."] }
----
{topic_title}
"""

    def __init__(
        self, api_key: str, topic_title: str, ai_model: Optional[str] = None
    ) -> None:
        super().__init__(
            api_key=api_key,
            ai_model=ai_model,
            system_content=self.get_system_content(topic_title),
        )

    def talk(self, message) -> Optional[List[str]]:
        response = super().talk(message)

        #
        data = self._parse_response(response)
        return data

    def _parse_response(self, response: str) -> Optional[List[str]]:
        data_dict = json.loads(response)

        result = data_dict["answers"]
        if len(result) != 10:
            return None

        return result
