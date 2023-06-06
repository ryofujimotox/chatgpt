from typing import Optional, List
from chatgpt.src.ai_chatbot import AIChatbot
import json


class QuizAnswers(AIChatbot):
    def get_system_content(self, topic_title):
        return f"""
Prompt:
- We're going to play a guessing game. I'll think of an 'Answer', and you'll have to generate it.
- Generate a list of 10 'Answers' that could potentially be correct. The difficulty level should be easy.
- The 'Answers' must be written in Japanese.
- Please format your output in JSON, like this: { "answers": ["Answer1", "Answer2", "..."] }
- Ensure all keys are included in your output.
- Do not include any additional information beyond what is contained in the JSON structure.
- If you don't have any relevant answers, return null in the 'answers' key.
----
{topic_title}
"""

# Prompt:
# - Let's play a game where you try to guess the 'Answer' I'm thinking of.
# - Please prepare 10 suitable 'Answers' for the topic in bullet points.
# - Difficulty level: Easy
# - 'Answers' must be in Japanese.

# Format:
# - Always output values in the following format: {{ "answers":["Answers"] }}
# - Keys must be included.
# - Remove information other than JSON.
# - If there is no corresponding information, set to null.
# ----
# {topic_title}

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
