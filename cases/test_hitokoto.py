import allure
from api.hitokoto import HitokotoAPI


class TestHitokoto:

    # 这个方法名必须以 test_ 开头
    @allure.title("测试一言接口：获取随机句子")
    def test_get_random_quote(self, api_client):
        hitokoto_api = HitokotoAPI(api_client)

        # 用 with 语法给发请求这一步加个标签
        with allure.step("1. 发送 GET 请求到一言接口"):
            response = hitokoto_api.get_random_quote()

        with allure.step("2. 断言 HTTP 状态码为 200"):
             # 断言 HTTP 状态码
            assert response.status_code == 200

        with allure.step("3. 解析 JSON 并断言核心字段"):
            data = response.json()
            # 断言业务逻辑
            assert "hitokoto" in data
            assert "from" in data

        allure.attach(data['hitokoto'], name="获取到的句子", attachment_type=allure.attachment_type.TEXT)
        # 可以打印，也可以不打印（pytest 默认捕获 print）
        print(f"获取到的句子：{data['hitokoto']}")


