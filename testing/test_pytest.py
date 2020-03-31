import sys
import pytest

sys.path.append("..")

from python.calc import Calc

test_data_add = [
    (1, 2, 3),  # 正数
    (1.4, 1.5, 2.9),  # 小数
    (-1, -4, -5)  # 负数
]

test_data_div = [
    (4, 2, 2),  # 整数整除
    (7, 3, 2),  # 整数不整除
    (-4, -2, 3),  # 负数整除
    (-7, -2, 3),  # 负数不整除
    (7.0, 3.5, 2),  # 小数整除
    (7.0, 2.0, 3.5)  # 小数不整除
]


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a, b, result", test_data_add)
    def test_add(self, a, b, result):
        assert self.calc.add(a, b) == result

    @pytest.mark.parametrize("a, b, result", test_data_div)
    def test_div(self, a, b, result):
        assert self.calc.div(a, b) == result

    def test_div_exception(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(3, 0)



if __name__ == '__main__':
    pytest.main(['-v'])