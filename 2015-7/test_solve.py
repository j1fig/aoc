import pytest

import solve


@pytest.mark.parametrize('data,instruction', [
    ('123 -> x',        solve.Instruction(op='store',   args=(123,),        wire='x')),
    ('456 -> y',        solve.Instruction(op='store',   args=(456,),        wire='y')),
    ('x AND y -> d',    solve.Instruction(op='and',     args=('x', 'y'),    wire='d')),
    ('x OR y -> e',     solve.Instruction(op='or',      args=('x', 'y'),    wire='e')),
    ('x LSHIFT 2 -> f', solve.Instruction(op='lshift',  args=('x', 2),      wire='f')),
    ('y RSHIFT 2 -> g', solve.Instruction(op='rshift',  args=('y', 2),      wire='g')),
    ('NOT x -> h',      solve.Instruction(op='not',     args=('x',),        wire='h')),
    ('NOT y -> i',      solve.Instruction(op='not',     args=('y',),        wire='i')),
])
def test_parse_instruction(data, instruction):
    assert solve._parse_instruction(data) == instruction
