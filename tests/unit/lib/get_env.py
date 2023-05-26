from dotenv import load_dotenv
import os

load_dotenv()


def get(key):
    value = os.getenv(key)
    return value
