from Calc import Calc


class TestCalcAdd:
    def test_calc_positive(self):
        add = Calc(1, 1)
        assert add.calc_add() == 2

    def test_calc_minus(self):
        add = Calc(-1, -1)
        assert add.calc_add() == -2

    def test_calc_zero(self):
        add = Calc(0, 0)
        assert add.calc_add() == 0


class TestCalcDiv:
    def test_calc_positive(self):
        div = Calc(1, 1)
        assert div.calc_div() == 1

    def test_calc_minus(self):
        div = Calc(-1, -1)
        assert div.calc_div() == -1
