from config.settings import get_config

class HitokotoAPI:
    def __init__(self, session):
        self.session = session
        self.url = get_config()["hitokoto_url"]

    def get_random_quote(self):
        # 只负责发请求，把结果 return 出去，绝不写 assert
        return self.session.get(self.url,timeout = 15)

