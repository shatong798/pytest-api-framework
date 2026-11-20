from api import calc
from utils.logger import get_logger

logger = get_logger(__name__)


class TestCaleEx:

    def test_01_add(self, pre_op1):
        result = calc.add(1,2)
        logger.info(f"结果是：{result}")
        assert result == 3

    def test_02_sub(self, pre_op1):
        result = calc.sub(1,2)
        logger.info(f"结果是：{result}")
        assert result == -1

    def test_03_mul(self, pre_op1):
        result = calc.mul(1,2)
        logger.info(f"结果是：{result}")
        assert result == 2

    def test_04_div(self, pre_op1):
        result = calc.div(1,2)
        logger.info(f"结果是：{result}")
        assert result == 0.5

