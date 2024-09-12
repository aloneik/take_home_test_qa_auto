from typing import List, Tuple

from field import generate_pangaea_field, print_field
from utils import bfs_shortest_path, is_valid_point


def parse_coordinates(user_input: str) -> Tuple[int, int]:
    x, y = map(lambda x: int(x), user_input.split(","))
    return (x, y)


def get_land_percentage() -> int:
    user_input = input("Enter land part of the field (0-100%): ")
    try:
        percentage = int(user_input)
        return percentage
    except ValueError:
        print(
            f"Error: Invalid land percantage format: '{user_input}'. Expected the following format: a number from 0 to 100"
        )
        raise


def get_field_size() -> Tuple[int, int]:
    user_input: str = input("Enter field size (M,N): ")
    try:
        rows, cols = parse_coordinates(user_input)
        return rows, cols
    except ValueError:
        print(
            f"Error: Invalid field size format: '{user_input}'. Expected the following format: 'x,y'. Eg. 5,3"
        )
        raise


def get_start_point() -> Tuple[int, int]:
    user_input: str = input("Enter start point (x,y): ")
    try:
        start_x, start_y = parse_coordinates(user_input)
        return start_x, start_y
    except ValueError:
        print(
            f"Error: Invalid start point format: '{user_input}'. Expected the following format: 'x,y'. Eg. 0,0"
        )
        raise


def get_end_point() -> Tuple[int, int]:
    user_input: str = input("Enter end point (x,y): ")
    try:
        end_x, end_y = parse_coordinates(user_input)
        return end_x, end_y
    except ValueError:
        print(
            f"Error: Invalid end point format: '{user_input}'. Expected the following format: 'x,y'. Eg. 0,0"
        )
        raise


if __name__ == "__main__":
    rows, cols = get_field_size()
    if rows < 0 or cols < 0:
        print(f"Error: The width and height of the field must be greater than zero")

    land_percentage = get_land_percentage()
    if land_percentage < 0 or land_percentage > 100:
        print(f"Error: Land percentage exceeds the expected range: 0-100")
        exit()

    field: List[List[bool]] = generate_pangaea_field(rows, cols, land_percentage)
    print_field(field)

    start_x, start_y = get_start_point()
    if not is_valid_point(field, start_x, start_y):
        print(f"Error: Start point is outside of the field")
        exit()

    end_x, end_y = get_end_point()
    if not is_valid_point(field, end_x, end_y):
        print(f"Error: End point is outside of the field")
        exit()

    path = bfs_shortest_path(field, (start_x, start_y), (end_x, end_y))

    if path:
        print("Shortest path: ", end="")
        print(" => ".join(map(lambda x: str(x), path)))
    else:
        print(f"Unable to find a way from ({start_x}, {start_y}) to ({end_x}, {end_y})")
