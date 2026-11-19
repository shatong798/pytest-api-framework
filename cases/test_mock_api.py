import json
import requests
import pytest
import allure
from config.settings import get_config
from pathlib import Path

# 项目根目录（cases 的上一级）
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "mock_area_cases.json"   # ← 用 / 拼路径

# 读取测试数据文件
with open(DATA_PATH, encoding="utf-8") as f:
    AREA_CASES = json.load(f)

class TestMockAPI:
    # 定义你本地服务的地址
    base_url = get_config()["base_url"]

    @allure.title("数据驱动：新增区域")
    @pytest.mark.parametrize(
        "case",
        AREA_CASES,
        ids=[c["desc"] for c in AREA_CASES],  # 用例名直接用 desc，报告里好认
    )
    def test_add_and_verify_area(self, mock_server,case):
        # 1. 用当前这组数据发请求
        res = requests.post(f"{self.base_url}/area/addarea", json=case["payload"], timeout=5)

        # 2. 断言状态码 / success 是否符合该组数据的期望
        assert res.status_code == case["expect_code"]
        assert res.json()["success"] == case["expect_success"]

        # 3. 正向用例才去列表里验证"真的加进去了"
        if case["expect_success"]:
            res_list = requests.get(f"{self.base_url}/area/listarea", timeout=5)
            data_list = res_list.json()["data"]
            assert any(item["areaName"] == case["payload"]["areaName"] for item in data_list)