from advanced_topics.magic_methods.fraction import Fraction


class TestFraction:
    def test_fraction_str(self):
        f = Fraction(1, 2)
        assert str(f) == "1/2"

    def test_fraction_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        assert f1 + f2 == Fraction(3, 4)

    def test_fraction_sub(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        assert f1 - f2 == Fraction(1, 4)

    def test_fraction_mul(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        assert f1 * f2 == Fraction(1, 8)

    def test_fraction_div(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        assert f1 / f2 == Fraction(2, 1)

    def test_fraction_eq(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 4)
        assert f1 == Fraction(2, 4)
        assert f1 != f2
        assert f1 == f1

    def test_fraction_simplify(self):
        f1 = Fraction(2, 4)
        assert f1 == Fraction(1, 2)
