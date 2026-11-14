class HitokotoAPI:
    def __init__(self, session):
        self.session = session
        self.url = "https://v1.hitokoto.cn/"

    def get_random_quote(self):
        # 只负责发请求，把结果 return 出去，绝不写 assert
        return self.session.get(self.url,timeout = 15)

