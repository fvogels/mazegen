from mazegen.maze import Maze
from mazegen.rendering import render_maze
import argparse
import random
import sys


def main():
    parser = argparse.ArgumentParser(description="Generates mazes")
    parser.add_argument('-W', '--width', type=int)
    parser.add_argument('-H', '--height', type=int)
    parser.add_argument('-s', '--seed', type=int, default=None)
    parser.add_argument('-c', '--size', type=int, default=32)
    parser.add_argument('-o', '--output', type=str, default='stdout')
    args = parser.parse_args()
    width = args.width
    height = args.height
    rnd = random.Random(args.seed) if args.seed else random.Random()
    maze = Maze.generate(width, height, rnd)
    if args.output == 'stdout':
        print(maze)
    else:
        render_maze(maze, cell_size=args.size).save(args.output)