from api import calc


class TestCaleEx:

    def test_01_add(self, pre_op1):
        result = calc.add(1,2)
        print(f"结果是：{result}")
        assert result == 3

    def test_02_sub(self, pre_op1):
        result = calc.sub(1,2)
        print(f"结果是：{result}")
        assert result == -1

    def test_03_mul(self):
        result = calc.mul(1,2)
        print(f"结果是：{result}")
        assert result == 2

    def test_04_div(self):
        result = calc.div(1,2)
        print(f"结果是：{result}")
        assert result == 1

