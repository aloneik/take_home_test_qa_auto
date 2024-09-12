from typing import List, Tuple
from collections import deque


def is_valid_point(field: List[List[bool]], x: int, y: int) -> bool:
    rows = len(field)
    cols = len(field[0])
    return 0 <= x < rows and 0 <= y < cols


def bfs_shortest_path(
    field: List[List[bool]], source: Tuple[int, int], destination: Tuple[int, int]
) -> List[Tuple[int, int]]:
    start_x, start_y = source
    end_x, end_y = destination

    # There is no way from/to a land cell
    if field[start_x][start_y] or field[end_x][end_y]:
        return []

    directions = (-1, 0, 1, 0, -1)

    # Initialize a queue for BFS with the source with the path
    deq = deque([(start_x, start_y, [source])])

    visited = set()
    visited.add(source)

    while deq:
        x, y, path = deq.popleft()

        if (x, y) == destination:
            return path

        for i in range(0, 4):
            dx = directions[i]
            dy = directions[i + 1]

            adjacent_x = x + dx
            adjacent_y = y + dy
            adjacent_cell = (adjacent_x, adjacent_y)

            if not is_valid_point(field, adjacent_x, adjacent_y):
                continue

            if adjacent_cell not in visited and not field[adjacent_x][adjacent_y]:
                deq.append((adjacent_x, adjacent_y, path + [adjacent_cell]))
                visited.add(adjacent_cell)

    return []
