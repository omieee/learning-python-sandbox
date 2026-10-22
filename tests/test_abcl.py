from abstract_base_class_learning.abcl import Square


def test_square_functionality() -> None:
    sq = Square(10)
    assert 100 == sq.area()
