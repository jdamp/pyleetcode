import pytest

from problems.p001_two_sum import two_sum


# test cases from leetcpde
@pytest.mark.parametrize("nums,target,expected", [([2, 7, 11, 15], 9, (0, 1)),
                                                  ([3, 2, 4], 6, (1, 2)),
                                                  ([3, 3], 6, (0, 1))])
def test_two_sum(nums, target, expected):
    assert two_sum(nums, target) == expected
