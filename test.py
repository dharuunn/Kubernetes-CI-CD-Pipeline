from app import calculate_bill
def test_calculate_bill():
    assert calculate_bill(10.0, 3) == 30.0
    assert calculate_bill(0, 5) == 0.0
    