import pytest
import requests
import threading
import time
from mock_server.app import app
from config.settings import get_config
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="session")
def mock_server():
    cfg = get_config()
    server = threading.Thread(
        target=lambda: app.run(host=cfg["mock_host"], port=cfg["mock_port"], debug=False, use_reloader=False),
        daemon=True,
    )
    server.start()
    time.sleep(2)
    yield

# 添加fixture装饰器，控制测试用例的前置和后置执行范围
@pytest.fixture(scope="class")
def pre_op1():
    # “前后置函数”
    logger.info("新:打开计算机")
    yield
    logger.info("新.关闭计算器")


@pytest.fixture(scope="session")
def api_client():
    logger.info("全局：建立 Session 连接")
    session = requests.Session()
    yield session  # 把 session 交出去给测试用例用
    logger.info("全局：关闭 Session 连接")
    session.close()