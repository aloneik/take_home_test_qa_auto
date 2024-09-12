import pytest

from shortest_path.utils import bfs_shortest_path


@pytest.mark.parametrize(
    "field,start,end,expected_path",
    [
        ([[True]], (0, 0), (0, 0), []),
        ([[False]], (0, 0), (0, 0), [(0, 0)]),
        (
            [[False, False, False], [False, True, False], [False, True, False]],
            (2, 2),
            (0, 0),
            [(2, 2), (1, 2), (0, 2), (0, 1), (0, 0)],
        ),
        (
            [
                [False, False, False],
                [False, True, False],
                [False, True, False],
                [False, False, False],
                [False, False, False],
            ],
            (2, 0),
            (2, 2),
            [(2, 0), (3, 0), (3, 1), (3, 2), (2, 2)],
        ),
        (
            [
                [False, False, False, False],
                [False, True, True, False],
                [False, False, True, True],
                [False, True, True, False],
                [False, False, False, False],
            ],
            (3, 3),
            (2, 1),
            [(3, 3), (4, 3), (4, 2), (4, 1), (4, 0), (3, 0), (2, 0), (2, 1)],
        ),
        (
            [
                [False, False, True],
                [False, False, True],
                [False, False, True],
                [False, False, True],
            ],
            (0, 0),
            (3, 0),
            [(0, 0), (1, 0), (2, 0), (3, 0)],
        ),
        (
            [
                [True, True, True, True],
                [False, False, False, False],
                [False, False, False, False],
            ],
            (1, 0),
            (1, 3),
            [(1, 0), (1, 1), (1, 2), (1, 3)],
        ),
    ],
)
def test_get_shortest_path(field, start, end, expected_path):
    path = bfs_shortest_path(field, start, end)

    assert path == expected_path


@pytest.mark.parametrize(
    "field,start,end,expected_path",
    [
        (
            [[True, False, False], [False, True, False], [False, False, True]],
            (1, 0),
            (0, 1),
            [],
        ),
        (
            [
                [False, True, False],
                [False, True, False],
                [False, True, False],
            ],
            (1, 0),
            (1, 2),
            [],
        ),
        (
            [
                [False, False, False],
                [True, True, True],
                [False, False, False],
            ],
            (2, 1),
            (0, 1),
            [],
        ),
    ],
)
def test_no_path(field, start, end, expected_path):
    path = bfs_shortest_path(field, start, end)

    assert path == expected_path
