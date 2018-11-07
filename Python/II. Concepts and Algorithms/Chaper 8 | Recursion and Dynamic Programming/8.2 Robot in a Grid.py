"""
8.2 Robot in a grid.

Imagine a robot sitting on the upper left corner of grid with r rows and c
columns.The robot can only move in two directions, right and down, but certain
cells are "off limits" such that the robot cannot step on them. Design an
algorithm to find a path for the robot from the top left to the bottom right.
"""
from collections import namedtuple

Point = namedtuple('Point', 'row col')


def robot_in_a_grid(maze):
    """Method to find a path for the robot."""
    if not maze:
        return None
    path = []
    failed_points = {}
    if get_path(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
        return path
    return None


def get_path(maze, row, col, path, failed_points):
    """Method to find a path for the robot."""
    # If out of bounds or  not available, return.
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    p = Point(row, col)

    # If we've already visited this cell, return.
    if p in failed_points:
        return False

    is_at_origin = (row == 0) and (col == 0)

    # If there's a path from start to my current location, add my location.
    if is_at_origin or get_path(maze, row, col - 1, path, failed_points)
        or get_path(maze, row - 1, col, path, failed_points):
       path.add(p)
       return True

    failed_points.add(p)  # Cache result.
    return False
