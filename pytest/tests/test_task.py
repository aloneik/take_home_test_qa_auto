import pytest
import pytest_check as check


@pytest.mark.parametrize(
    "limit",
    [10**7, 1.5 * (10**7), 5 * (10**7), 10**8, 5 * (10**8), 10**9, 1.5 * (10**9)],
)
def test_no_popularity_less_than_given(programming_language_popularity, limit):
    for row in programming_language_popularity:
        popularity = row.popularity
        check.greater_equal(popularity, limit, f"{row} (Expected more than {limit})")
