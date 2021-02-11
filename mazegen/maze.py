import random


class Maze:
    @staticmethod
    def generate(width, height, rnd=random):
        free = False
        wall = True
        grid = [ [ wall for _ in range(width) ] for _ in range(height) ]

        def is_inside(x, y):
            return 0 <= x < width and 0 <= y < height

        def around(x, y):
            for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                p = (x + dx, y + dy)
                if is_inside(*p):
                    yield p

        x = rnd.randrange(width)
        y = rnd.randrange(height)
        grid[y][x] = free
        queue = [(x, y)]

        while queue:
            x, y = queue.pop()
            free_count = 0
            for (x2, y2) in around(x, y):
                if grid[y2][x2] == free:
                    free_count += 1
            if free_count < 2:
                grid[y][x] = free
                neighbors = list(around(x, y))
                rnd.shuffle(neighbors)
                for neighbor in neighbors:
                    queue.append(neighbor)

        return Maze(grid)

    def __init__(self, grid):
        self.__grid = grid

    @property
    def width(self):
        return len(self.__grid[0])

    @property
    def height(self):
        return len(self.__grid)

    def is_free(self, position):
        x, y = position
        return not self.__grid[y][x]

    def is_wall(self, position):
        x, y = position
        return self.__grid[y][x]

    @property
    def walls(self):
        return ((x, y) for y in range(self.width) for x in range(self.height) if self.is_wall((x, y)))

    def __str__(self):
        return "\n".join("".join("x" if elt else "." for elt in row) for row in self.__grid)
