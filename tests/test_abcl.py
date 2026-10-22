from abstract_base_class_learning.abcl import Square


def test_square_functionality() -> None:
    sq = Square(10, 20)
    assert 200 == sq.area()
