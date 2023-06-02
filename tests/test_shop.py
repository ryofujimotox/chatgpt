from chatgpt.src.shop import Shop
from chatgpt.tests.lib.get_env import env


class TestCreateShop:
    shopname = """BBQ restaurant 'GOLD BUTCHER'"""
    menu = """番号,名前,価格,おすすめかどうか
1,上ロース,10000,false
2,牛タン,5000,true
3,超柔らかい肉X,20000,true
4,コーラ,100,false
5,オレンジジュース,200,false"""

    def test__正常系_用意できているか(self):
        apikey = env("OPENAI_API_KEY")

        #
        Chat = Shop(apikey, self.shopname, self.menu)
        talked = Chat.talk("おすすめは？")
        if talked is None:
            assert talked == "取得できなかった"
            return

        assert ("牛タン" in talked["waiter_speak"]) or ("柔らかい肉" in talked["waiter_speak"])

    def test__正常系_用意できているか2(self):
        apikey = env("OPENAI_API_KEY")

        #
        Chat = Shop(apikey, self.shopname, self.menu)
        talked = Chat.talk("コーラ1つと、牛タン2つ、上ロース1つください")
        if talked is None:
            assert talked == "取得できなかった"
            return
        assert talked["waiter_speak"]

        order = talked["ordered_numbers"]
        assert order.count(2) == 2
        assert order.count(4) == 1
        assert order.count(1) == 1
        assert len(order) == 4
