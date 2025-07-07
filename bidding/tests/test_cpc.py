import pytest
from bidding.price_helper import adjusted_cpc

@pytest.mark.parametrize(
    "current_cpc, target_roas, expected",
    [
        (1.0, 100, 1.0),
        (2.0, 50, 1.0),
        (3.0, 0, 0.0),
        (4.0, 200, 8.0),
        (0, 100, 0),
    ]
)
def test_calculate_adjusted_cpc(current_cpc, target_roas, expected):
    assert adjusted_cpc(current_cpc, target_roas) == expected