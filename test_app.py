from app import calculate_bill
def test_calculate_bill_no_discount():
    assert calculate_bill(10.0, 3, 0) == 30.0
def test_calculate_bill_with_discount():
    assert calculate_bill(100.0, 1, 10) == 90.0
    assert calculate_bill(20.0, 5, 25) == 75.0
