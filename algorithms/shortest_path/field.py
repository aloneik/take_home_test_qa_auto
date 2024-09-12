import math
from random import choice
from typing import List


# Returns a Pangaea (land surrounded by water) map of the given size
def generate_pangaea_field(
    rows: int, cols: int, land_percentage: int
) -> List[List[bool]]:
    field: List[List[bool]] = [[False for _ in range(cols)] for _ in range(rows)]

    total_cells = rows * cols
    land_cells: int = math.floor(total_cells * (land_percentage / 100))

    if land_cells == 0:
        return field

    start_x = rows // 2
    start_y = cols // 2
    field[start_x][start_y] = True
    land_count = 1

    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    land_positions = [(start_x, start_y)]

    while land_count < land_cells:
        x, y = choice(land_positions)

        dx, dy = choice(directions)
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < rows and 0 <= new_y < cols and not field[new_x][new_y]:
            field[new_x][new_y] = True
            land_positions.append((new_x, new_y))
            land_count += 1

    return field


def print_field(field: List[List[bool]]) -> None:
    for row in field:
        # L - land, W - water
        print("|".join(map(lambda x: "L" if x else "W", row)))
