from dotenv import load_dotenv
import os
from typing import Optional


def load() -> None:
    """
    .envファイルから環境変数を読み込む関数。

    Returns:
        None
    """
    load_dotenv()


load()


def env(key: str) -> Optional[str]:
    """
    指定したキーの環境変数の値を取得する関数。

    Parameters:
        key (str): 環境変数のキー

    Returns:
        Optional[str]: 環境変数の値（存在しない場合はNone）
    """
    value = os.getenv(key)
    return value
