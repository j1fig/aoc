import pytest

import solve


@pytest.mark.parametrize('sequence,result', [
    ('xyxy', True),
    ('aabcdefgaa', True),
    ('aaa', False),
])
def test_has_non_overlapping_repeating_pairs(sequence, result):
    assert solve._has_non_overlapping_repeating_pairs(sequence) == result


@pytest.mark.parametrize('sequence,result', [
    ('aaa', True),
    ('xyx', True),
    ('abcdefeghi', True),
    ('uurcxstgmygtbstg', False),
])
def test_has_interspersed_repeated_letters(sequence, result):
    assert solve._has_interspersed_repeated_letters(sequence) == result
