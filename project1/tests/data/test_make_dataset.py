import pytest

from src.data.make_dataset import categories_to_ids


@pytest.mark.parametrize(
    "column, categories",
    [
        ("buying_price", {"vhigh": 4, "high": 3, "med": 2, "low": 1}),
        ("maint_price", {"vhigh": 4, "high": 3, "med": 2, "low": 1}),
        ("luggage_boot_size", {"big": 3, "med": 2, "small": 1}),
        ("safety_estimate", {"high": 3, "med": 2, "low": 1}),
    ],
)
def test_categories_to_ids(column, categories):
    assert categories_to_ids(column, categories) == categories
