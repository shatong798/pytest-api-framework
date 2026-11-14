import requests
import pytest
import allure


class TestMockAPI:
    # 定义你本地服务的地址
    base_url = "http://localhost:1234"

    @allure.title("测试本地 Mock 服务：新增区域并验证")
    def test_add_and_verify_area(self):
        # 1. 准备数据
        payload = {"areaName": "发财", "priority": "999"}

        # 2. 发送 POST 新增请求
        res_post = requests.post(f"{self.base_url}/area/addarea", json=payload, timeout=5)

        # 3. 断言：状态码必须是 200，且 success 为 True
        assert res_post.status_code == 200
        assert res_post.json()["success"] is True

        # 4. 发送 GET 查询请求，验证是否真的加进去了
        res_get = requests.get(f"{self.base_url}/area/listarea", timeout=5)
        assert res_get.status_code == 200

        # 把返回的数据列表提取出来
        data_list = res_get.json()["data"]

        # 5. 断言：列表中必须包含刚刚新增的“发财”
        # 使用 any() 遍历列表，只要有一个匹配就通过
        assert any(item["areaName"] == "发财" for item in data_list)

        print("\n✅ 测试通过：'发财' 区域已成功存入后端内存数据库！")