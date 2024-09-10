import math

from itertools import chain
from random import random
from typing import List, Tuple
from collections import deque


# field_row_count: str = input("Enter field width: ")
# field_col_count: str = input("Enter field height: ")

field_row_count = "5"
field_col_count = "5"

# land_to_square_ratio = input("Enter land part of the field (0-100%): ")
land_to_square_ratio = "20"

lts_ratio = None
try:
    lts_ratio = int(land_to_square_ratio)
except ValueError:
    print(f"Error: Land part of the field value is invalid: '{land_to_square_ratio}'. Expected the following format: a number from 0 to 100")
    exit()

if lts_ratio < 0 or lts_ratio > 100:
    print(f"Error: Land part of the field value '{lts_ratio}' exceeds the expected range: 0-100")
    exit()

# generate the field
rows = int(field_col_count)
cols = int(field_row_count)
field_size = (rows, cols)

field: List[List[bool]] = [[random() < (int(land_to_square_ratio) / 100) for _ in range(cols)] for _ in range(rows)]

actual_ratio = sum(map(lambda x: 1 if x else 0, chain.from_iterable(field))) / (rows * cols) * 100
print(f"Land to square ratio: {math.floor(actual_ratio)}%")

def print_field(field: List[List[bool]]) -> None:
    for row in field:
        print("|".join(map(lambda x: "L" if x else "W", row)))

print_field(field)

def is_valid_point(point: Tuple[int, int], field_size: Tuple[int, int]):
    row = point[0]
    col = point[1]

    rows = field_size[0]
    cols = field_size[1]

    return row >= 0 and row < rows and col >= 0 and col < cols

start_point: str = input("Enter start point (x,y): ")
start_x, start_y = None, None
try:
    start_x, start_y = map(lambda x: int(x), start_point.split(','))
except ValueError:
    print(f"Error: Start point format is invalid: '{start_point}'. Expected the following point format: 'x,y'")
    exit()

if not is_valid_point((start_x, start_y), field_size):
    print(f"Error: Entered point ({start_x},{start_y}) exceeds the field size ({rows},{cols})")
    exit()


end_point: str = input("Enter end point (x,y): ")
end_x, end_y = None, None
try:
    end_x, end_y = map(lambda x: int(x), end_point.split(','))
except ValueError:
    print(f"Error: Start point format is invalid: '{end_point}'. Expected the following point format: 'x,y'")
    exit()

if not is_valid_point((end_x, end_y), field_size):
    print(f"Error: Entered point ({end_x},{end_y}) exceeds the field size ({rows},{cols})")
    exit()


# stop if one the points is Land
if field[start_x][start_y] or field[end_x][end_y]:
    print(f"There is no way from '({start_x},{start_y})' to '({end_x},{end_y})'")


# get shortest path
directions = [-1, 0, 1, 0, -1]

q = deque()
visited = [[cell for cell in row] for row in field]
distances = [[float("inf") for _ in range(cols)] for _ in range(rows)]
parents = [[-1 for _ in range(cols)] for _ in range(rows)]

q.append((start_x, start_y))
visited[start_x][start_y] = True
distances[start_x][start_y] = 0

while q:
    point = q.popleft()
    for i in range(0, 4):
        dx, dy = directions[i], directions[i + 1]
        adjacent_point = (point[0] + dx, point[1]+ dy)

        if not is_valid_point(adjacent_point, field_size):
            continue

        is_distance_infinite = distances[adjacent_point[0]][adjacent_point[1]] == float("inf")
        is_point_visited = visited[adjacent_point[0]][adjacent_point[1]]
        if is_distance_infinite and not is_point_visited:
            visited[adjacent_point[0]][adjacent_point[1]] = True
            parents[adjacent_point[0]][adjacent_point[1]] = point
            distances[adjacent_point[0]][adjacent_point[1]] = distances[point[0]][point[1]] + 1
            q.append(adjacent_point)


if distances[end_x][end_y] == float('inf'):
    print("Source and Destination are not connected")
    exit()

path = []
current_node = (end_x, end_y)
path.append(current_node)
while parents[current_node[0]][current_node[1]] != -1:
    path.append(parents[current_node[0]][current_node[1]])
    current_node = parents[current_node[0]][current_node[1]]

# Printing path from source to destination
print(" => ".join(map(lambda x: str(x), path[::-1])))
