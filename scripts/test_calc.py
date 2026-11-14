from api import calc


class TestCalc:
        def test_01_add(self):
            result = calc.add(1, 2)
            assert result == 3

