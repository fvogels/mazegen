from PIL import Image, ImageDraw


def render_maze(maze, cell_size=32):
    size = (maze.width * cell_size, maze.height * cell_size)
    image = Image.new('RGB', size, color='white')
    draw = ImageDraw.Draw(image)
    for y in range(maze.height):
        for x in range(maze.width):
            if maze.is_wall((x, y)):
                x1 = x * cell_size
                y1 = y * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                draw.rectangle([(x1, y1), (x2, y2)], fill='black')
    return image