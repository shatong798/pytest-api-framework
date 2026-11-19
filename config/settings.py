import os

# 当前环境：读环境变量 ENV，没设置就默认 test
ENV = os.getenv("ENV", "test")

# 每个环境一套配置
CONFIG = {
    "test": {
        "base_url": "http://127.0.0.1:1234",
        "mock_host": "127.0.0.1",
        "mock_port": 1234,
        "hitokoto_url": "https://v1.hitokoto.cn/",
    },
    "staging": {
        "base_url": "http://staging.example.com",
        "mock_host": "127.0.0.1",
        "mock_port": 1234,
        "hitokoto_url": "https://v1.hitokoto.cn/",
    },
    "prod": {
        "base_url": "http://prod.example.com",
        "mock_host": "127.0.0.1",
        "mock_port": 1234,
        "hitokoto_url": "https://v1.hitokoto.cn/",
    },
}


def get_config():
    """根据当前环境返回对应配置"""
    return CONFIG[ENV]