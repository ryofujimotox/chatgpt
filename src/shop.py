from typing import Optional, List
from chatgpt.src.ai_chatbot import AIChatbot
import json


class Shop(AIChatbot):
    def get_system_content(self, shop_name, menu):
        return f"""
- Act as a Waiter at the {shop_name}
- 客にメニュー番号は伝えないでください

Always output values in the following format
{{
  "ordered_numbers":[Ordered menu numbers],
  "waiter_speak": output your statement as a Waiter in Japanese
}}
Keys must be included.
Delete information other than JSON.
If there is no corresponding information, set to null.

menu:
{menu}
"""

    def __init__(
        self, api_key: str, shop_name: str, menu: str, ai_model: Optional[str] = None
    ) -> None:
        super().__init__(
            api_key=api_key,
            ai_model=ai_model,
            system_content=self.get_system_content(shop_name, menu),
        )

    def talk(self, message) -> Optional[List[str]]:
        response = super().talk(message)

        #
        data = self._parse_response(response)
        if not data["waiter_speak"]:
            return None

        return data

    def _parse_response(self, response: str) -> List[str]:
        data_dict = json.loads(response)

        # 結果を表示
        return {
            "waiter_speak": data_dict["waiter_speak"],
            "ordered_numbers": data_dict["ordered_numbers"],
        }
