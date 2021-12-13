from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Pixel Art")


def init_grid(rows, cols, color):  # function to init grid on starting
    grid = []

    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):  # function to draw grid pixel on window
    for i, row in enumerate(grid):
        for j, pixel in enumerate(row):
            pygame.draw.rect(
                win, pixel, (j*PIXEL_SIZE, i*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS+1):
            pygame.draw.line(win, BLACK, (0, i*PIXEL_SIZE),
                             (WIDTH, i*PIXEL_SIZE))

        for i in range(COLS+1):
            pygame.draw.line(win, BLACK, (i*PIXEL_SIZE, 0),
                             (i*PIXEL_SIZE, HEIGHT-TOOLBAR_HEIGHT))


# function to get the row and col when mouse is clicked
def get_row_col_from_pos(pos):
    x, y = pos
    row = y//PIXEL_SIZE
    col = x//PIXEL_SIZE

    if row >= ROWS:
        raise IndexError
    return row, col


def draw(win, grid, buttons):  # function to draw
    win.fill(BG_COLOR)
    draw_grid(win, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK
button_y_pos = HEIGHT-TOOLBAR_HEIGHT/2-15
buttons = [
    Button(10, button_y_pos, 30, 30, BLACK),
    Button(50, button_y_pos, 30, 30, RED),
    Button(90, button_y_pos, 30, 30, GREEN),
    Button(130, button_y_pos, 30, 30, BLUE),
    Button(170, button_y_pos, 30, 30, WHITE, "Erase", BLACK),
    Button(210, button_y_pos, 30, 30, WHITE, "Clear", BLACK)
]

# main event loop
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color

                    if button.text == "Clear":
                        grid = init_grid(ROWS, COLS, BG_COLOR)
                        drawing_color = BLACK

    draw(WIN, grid, buttons)

pygame.quit()
