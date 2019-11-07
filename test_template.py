import pytest

import solve


@pytest.mark.parametrize('data,result', [
    ('x', 'x'),
])
def test(data, result):
    assert data == result
