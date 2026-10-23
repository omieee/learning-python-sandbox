from composition.composition_learning import Car


def test_print_car_details() -> None:
    car = Car("Honda", "City", 250)
    assert car.display().startswith("I own a")
