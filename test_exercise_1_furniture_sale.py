import pytest
from decimal import Decimal
from datetime import date
from Dummy_1 import calculate_discount

_test_date_valids = [
    pytest.param(date(2022, 11, 28), Decimal("0.01"), Decimal("0.05"), id="1"),
    pytest.param(date(2022, 12, 23), Decimal("0.01"), Decimal("0.05"), id="2"),
    pytest.param(date(2022, 11, 25), Decimal("0.01"), Decimal("0.00"), id="3"),
    pytest.param(date(2022, 12, 27), Decimal("0.01"), Decimal("0.00"), id="4"),
    pytest.param(date(2022, 11, 26), Decimal("0.01"), Decimal("0.15 "), id="5"),
    pytest.param(date(2022, 12, 24), Decimal("0.01"), Decimal("0.15"), id="6"),
    pytest.param(date(2022, 11, 28), Decimal("99.99"), Decimal("0.05"), id="7"),
    pytest.param(date(2022,12,23), Decimal("99.99"), Decimal("0.05"), id="8"),
    pytest.param(date(2022,11,25), Decimal("99.99"), Decimal("0.00"), id="9"),
    pytest.param(date(2022,12,27), Decimal("99.99"), Decimal("0.00"), id="10"),
    pytest.param(date(2022,11,26), Decimal("99.99"), Decimal("0.15"), id="11"),
    pytest.param(date(2022,12,24), Decimal("99.99"), Decimal("0.15"), id="12"),
    pytest.param(date(2022,11,28), Decimal("100"), Decimal("0.10"), id="13"),
    pytest.param(date(2022, 12,23), Decimal("100"), Decimal("0.10"), id="14"),
    pytest.param(date(2022,11,25), Decimal("100"), Decimal("0.00"), id="15"),
    pytest.param(date(2022,12,27), Decimal("100"), Decimal("0.00"), id="16"),
    pytest.param(date(2022,11,26), Decimal("100"), Decimal("0.19"), id="17"),
    pytest.param(date(2022,12,24), Decimal("100"), Decimal("0.19"), id="18"),
    pytest.param(date(2022,11,28), Decimal("499.99"), Decimal("0.10"), id="19"),
    pytest.param(date(2022,12,23), Decimal("499.99"), Decimal("0.10"), id="20"),
    pytest.param(date(2022, 11,25), Decimal("499.99"), Decimal("0.00"), id="21"),
    pytest.param(date(2022,12,27), Decimal("499.99"), Decimal("0.00"), id="22"),
    pytest.param(date(2022,11,26), Decimal("499.99"), Decimal("0.19"), id="23"),
    pytest.param(date(2022,12,24), Decimal("499.99"), Decimal("0.19"), id="24"),
    pytest.param(date(2022,11,28), Decimal("500"), Decimal("0.20"), id="25"),
    pytest.param(date(2022,12,23), Decimal("500"), Decimal("0.20"), id="26"),
    pytest.param(date(2022,11,25), Decimal("500"), Decimal("0.00"), id="27"),
    pytest.param(date(2022,12,27), Decimal("500"), Decimal("0.00"), id="28"),
    pytest.param(date(2022,11,26), Decimal("500"), Decimal("0.28"), id="29"),
    pytest.param(date(2022,12,24), Decimal("500"), Decimal("0.28"), id="30")
]
@pytest.mark.parametrize("day, total, expected", _test_date_valids)
def test_sale(day: date, total: Decimal, expected: Decimal):
    # Act
    actual = calculate_discount(day, total)
    # Assert
    assert actual == expected


_test_data_invalid_input = [
    pytest.param(date(2022,11,27), Decimal("3"), id="31"),
    pytest.param(date(2022,12,26), Decimal("3"), id="32"),
    pytest.param("B", Decimal("3"), id="33"),
    pytest.param(date(2022,11,30), Decimal("0"), id="34"),
    pytest.param(date(2022,11,30), "C", id="35")]
@pytest.mark.parametrize("day,total", _test_data_invalid_input)
def test_invalid_input(day: date, total: Decimal):
    with pytest.raises(ValueError):
        calculate_discount(day, total)