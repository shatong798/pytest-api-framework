import pytest
import requests

# 添加fixture装饰器，控制测试用例的前置和后置执行范围
@pytest.fixture(scope="class")
def pre_op1():
    # “前后置函数”
    print("新:打开计算机")
    yield
    print("新.关闭计算器")


@pytest.fixture(scope="session")
def api_client():
    print("\n--- 全局：建立 Session 连接 ---")
    session = requests.Session()
    yield session  # 把 session 交出去给测试用例用
    print("\n--- 全局：关闭 Session 连接 ---")
    session.close()