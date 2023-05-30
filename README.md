# Use AIChatbot

## Install

`1 local install` or `2 git install`

1 local install

put

```
your_project
|--main.py
|
|--chatgpt
|  |--.....
```

debug install

```
pip install -e /your_project/chatgpt
```


2 git install


```
pip install git+https://github.com/ryofujimotox/chatgpt
```


## How it Work

1 put `main.py`

``` python
from ai_chatbot import AIChatbot


def main():
    apikey = "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"

    Chat = AIChatbot(api_key=apikey)
    response = Chat.talk("1+1=")
    assert response == "2"

if __name__ == "__main__":
    main()
```

2 run

```
python main.py
```

3 confirm outout

```
hero: HELLO I'm HERO
hero: You are welcome
badman: We lost.
```



## Customize










