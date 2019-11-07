import pytest

import solve


@pytest.mark.parametrize('grid,instruction,result', [
    (
        [[-1, -1],
         [-1, -1]],
        solve.Instruction('on', 0, 0, 1, 1),
        [[1, 1],
         [1, 1]],
    ),
    (
        [[1, -1],
         [-1, 1]],
        solve.Instruction('toggle', 0, 0, 1, 1),
        [[-1, 1],
         [1, -1]],
    ),
    (
        [[1, -1],
         [-1, 1]],
        solve.Instruction('off', 0, 0, 1, 1),
        [[-1, -1],
         [-1, -1]],
    ),
    (
        [[1, -1],
         [-1, 1]],
        solve.Instruction('off', 0, 0, 0, 1),
        [[-1, -1],
         [-1, 1]],
    ),
    (
        [[-1, -1],
         [-1, 1]],
        solve.Instruction('toggle', 0, 0, 0, 1),
        [[1, 1],
         [-1, 1]],
    ),
])
def test_execute(grid, instruction, result):
    solve._execute(grid, instruction)
    assert grid == result


@pytest.mark.parametrize('grid,instruction,result', [
    (
        [[0, 0],
         [0, 0]],
        solve.Instruction('on', 0, 0, 1, 1),
        [[1, 1],
         [1, 1]],
    ),
    (
        [[1, 2],
         [4, 0]],
        solve.Instruction('toggle', 0, 0, 1, 1),
        [[3, 4],
         [6, 2]],
    ),
    (
        [[1, 0],
         [3, 10]],
        solve.Instruction('off', 0, 0, 1, 1),
        [[0, 0],
         [2, 9]],
    ),
    (
        [[1, 0],
         [3, 10]],
        solve.Instruction('on', 0, 0, 0, 0),
        [[2, 0],
         [3, 10]],
    ),
    (
        [[1, 0],
         [3, 10]],
        solve.Instruction('toggle', 1, 0, 1, 0),
        [[1, 0],
         [5, 10]],
    ),
    (
        [[1, 1],
         [3, 10]],
        solve.Instruction('off', 1, 0, 1, 1),
        [[1, 1],
         [2, 9]],
    ),
])
def test_regulate(grid, instruction, result):
    solve._regulate(grid, instruction)
    assert grid == result
