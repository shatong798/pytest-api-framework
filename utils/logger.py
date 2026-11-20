import logging
from pathlib import Path

# 日志目录：项目根目录下的 logs/
LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)


def get_logger(name: str = "api-test") -> logging.Logger:
    """获取一个配置好的 logger，重复调用不会重复添加 handler"""
    logger = logging.getLogger(name)

    # 已经配置过就直接返回，避免日志重复打印
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # 统一格式：时间 [级别] [模块名] 消息
    fmt = logging.Formatter(
        "%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 输出 1：控制台（INFO 及以上）
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(fmt)

    # 输出 2：文件 logs/test.log（DEBUG 及以上，更全）
    file_handler = logging.FileHandler(LOG_DIR / "test.log", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)

    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger