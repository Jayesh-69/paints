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
button_y_pos_1 = HEIGHT-TOOLBAR_HEIGHT/2-30-10-5
button_y_pos_2 = HEIGHT-TOOLBAR_HEIGHT/2-15-10-5
button_y_pos_3 = HEIGHT-TOOLBAR_HEIGHT/2-10-5
button_y_pos_4 = HEIGHT-TOOLBAR_HEIGHT/2+15-10-5
buttons = [
    Button(10, button_y_pos_1, 15, 15, MAROON),
    Button(25, button_y_pos_1, 15, 15, DARK_RED),
    Button(40, button_y_pos_1, 15, 15, BROWN),
    Button(55, button_y_pos_1, 15, 15, FIREBRICK),
    Button(70, button_y_pos_1, 15, 15, CRIMSON),
    Button(85, button_y_pos_1, 15, 15, RED),
    Button(100, button_y_pos_1, 15, 15, TOMATO),
    Button(115, button_y_pos_1, 15, 15, CORAL),
    Button(130, button_y_pos_1, 15, 15, INDIAN_RED),
    Button(145, button_y_pos_1, 15, 15, LIGHT_CORAL),
    Button(160, button_y_pos_1, 15, 15, DARK_SALMON),
    Button(175, button_y_pos_1, 15, 15, SALMON),
    Button(190, button_y_pos_1, 15, 15, LIGHT_SALMON),
    Button(205, button_y_pos_1, 15, 15, ORANGE_RED),
    Button(220, button_y_pos_1, 15, 15, DARK_ORANGE),
    Button(235, button_y_pos_1, 15, 15, ORANGE),
    Button(250, button_y_pos_1, 15, 15, GOLD),
    Button(265, button_y_pos_1, 15, 15, DARK_GOLDEN_ROD),
    Button(280, button_y_pos_1, 15, 15, GOLDEN_ROD),
    Button(295, button_y_pos_1, 15, 15, PALE_GOLDEN_ROD),
    Button(310, button_y_pos_1, 15, 15, DARK_KHAKI),
    Button(325, button_y_pos_1, 15, 15, KHAKI),
    Button(340, button_y_pos_1, 15, 15, OLIVE),
    Button(355, button_y_pos_1, 15, 15, YELLOW),
    Button(370, button_y_pos_1, 15, 15, YELLOW_GREEN),
    Button(385, button_y_pos_1, 15, 15, DARK_OLIVE_GREEN),
    Button(400, button_y_pos_1, 15, 15, OLIVE_DRAB),
    Button(415, button_y_pos_1, 15, 15, LAWN_GREEN),
    Button(430, button_y_pos_1, 15, 15, CHARTREUSE),
    Button(445, button_y_pos_1, 15, 15, GREEN_YELLOW),
    Button(460, button_y_pos_1, 15, 15, DARK_GREEN),
    Button(475, button_y_pos_1, 15, 15, GREEN),
    Button(490, button_y_pos_1, 15, 15, FOREST_GREEN),
    Button(505, button_y_pos_1, 15, 15, LIME),

    Button(10, button_y_pos_2, 15, 15, LIME_GREEN),
    Button(25, button_y_pos_2, 15, 15, LIGHT_GREEN),
    Button(40, button_y_pos_2, 15, 15, PALE_GREEN),
    Button(55, button_y_pos_2, 15, 15, DARK_SEA_GREEN),
    Button(70, button_y_pos_2, 15, 15, MEDIUM_SPRING_GREEN),
    Button(85, button_y_pos_2, 15, 15, SPRING_GREEN),
    Button(100, button_y_pos_2, 15, 15, SEA_GREEN),
    Button(115, button_y_pos_2, 15, 15, MEDIUM_AQUA_MARINE),
    Button(130, button_y_pos_2, 15, 15, MEDIUM_SEA_GREEN),
    Button(145, button_y_pos_2, 15, 15, LIGHT_SEA_GREEN),
    Button(160, button_y_pos_2, 15, 15, DARK_SLATE_GRAY),
    Button(175, button_y_pos_2, 15, 15, TEAL),
    Button(190, button_y_pos_2, 15, 15, DARK_CYAN),
    Button(205, button_y_pos_2, 15, 15, AQUA),
    Button(220, button_y_pos_2, 15, 15, CYAN),
    Button(235, button_y_pos_2, 15, 15, LIGHT_CYAN),
    Button(250, button_y_pos_2, 15, 15, DARK_TURQUOISE),
    Button(265, button_y_pos_2, 15, 15, TURQUOISE),
    Button(280, button_y_pos_2, 15, 15, MEDIUM_TURQUOISE),
    Button(295, button_y_pos_2, 15, 15, PALE_TURQUOISE),
    Button(310, button_y_pos_2, 15, 15, AQUA_MARINE),
    Button(325, button_y_pos_2, 15, 15, POWDER_BLUE),
    Button(340, button_y_pos_2, 15, 15, CADET_BLUE),
    Button(355, button_y_pos_2, 15, 15, STEEL_BLUE),
    Button(370, button_y_pos_2, 15, 15, CORN_FLOWER_BLUE),
    Button(385, button_y_pos_2, 15, 15, DEEP_SKY_BLUE),
    Button(400, button_y_pos_2, 15, 15, DODGER_BLUE),
    Button(415, button_y_pos_2, 15, 15, LIGHT_BLUE),
    Button(430, button_y_pos_2, 15, 15, SKY_BLUE),
    Button(445, button_y_pos_2, 15, 15, LIGHT_SKY_BLUE),
    Button(460, button_y_pos_2, 15, 15, MIDNIGHT_BLUE),
    Button(475, button_y_pos_2, 15, 15, NAVY),
    Button(490, button_y_pos_2, 15, 15, DARK_BLUE),
    Button(505, button_y_pos_2, 15, 15, MEDIUM_BLUE),

    Button(10, button_y_pos_3, 15, 15, BLUE),
    Button(25, button_y_pos_3, 15, 15, ROYAL_BLUE),
    Button(40, button_y_pos_3, 15, 15, BLUE_VIOLET),
    Button(55, button_y_pos_3, 15, 15, INDIGO),
    Button(70, button_y_pos_3, 15, 15, DARK_SLATE_BLUE),
    Button(85, button_y_pos_3, 15, 15, SLATE_BLUE),
    Button(100, button_y_pos_3, 15, 15, MEDIUM_SLATE_BLUE),
    Button(115, button_y_pos_3, 15, 15, MEDIUM_PURPLE),
    Button(130, button_y_pos_3, 15, 15, DARK_MAGENTA),
    Button(145, button_y_pos_3, 15, 15, DARK_VIOLET),
    Button(160, button_y_pos_3, 15, 15, DARK_ORCHID),
    Button(175, button_y_pos_3, 15, 15, MEDIUM_ORCHID),
    Button(190, button_y_pos_3, 15, 15, PURPLE),
    Button(205, button_y_pos_3, 15, 15, THISTLE),
    Button(220, button_y_pos_3, 15, 15, PLUM),
    Button(235, button_y_pos_3, 15, 15, VIOLET),
    Button(250, button_y_pos_3, 15, 15, MAGENTA),
    Button(265, button_y_pos_3, 15, 15, ORCHID),
    Button(280, button_y_pos_3, 15, 15, MEDIUM_VIOLET_RED),
    Button(295, button_y_pos_3, 15, 15, PALE_VIOLET_RED),
    Button(310, button_y_pos_3, 15, 15, DEEP_PINK),
    Button(325, button_y_pos_3, 15, 15, HOT_PINK),
    Button(340, button_y_pos_3, 15, 15, LIGHT_PINK),
    Button(355, button_y_pos_3, 15, 15, PINK),
    Button(370, button_y_pos_3, 15, 15, ANTIQUE_WHITE),
    Button(385, button_y_pos_3, 15, 15, BEIGE),
    Button(400, button_y_pos_3, 15, 15, BISQUE),
    Button(415, button_y_pos_3, 15, 15, BLANCHED_ALMOND),
    Button(430, button_y_pos_3, 15, 15, WHEAT),
    Button(445, button_y_pos_3, 15, 15, CORN_SILK),
    Button(460, button_y_pos_3, 15, 15, LEMON_CHIFFON),
    Button(475, button_y_pos_3, 15, 15, LIGHT_GOLDEN_ROD_YELLOW),
    Button(490, button_y_pos_3, 15, 15, LIGHT_YELLOW),
    Button(505, button_y_pos_3, 15, 15, SADDLE_BROWN),

    Button(10, button_y_pos_4, 15, 15, SIENNA),
    Button(25, button_y_pos_4, 15, 15, CHOCOLATE),
    Button(40, button_y_pos_4, 15, 15, PERU),
    Button(55, button_y_pos_4, 15, 15, SANDY_BROWN),
    Button(70, button_y_pos_4, 15, 15, BURLY_WOOD),
    Button(85, button_y_pos_4, 15, 15, TAN),
    Button(100, button_y_pos_4, 15, 15, ROSY_BROWN),
    Button(115, button_y_pos_4, 15, 15, MOCCASIN),
    Button(130, button_y_pos_4, 15, 15, NAVAJO_WHITE),
    Button(145, button_y_pos_4, 15, 15, PEACH_PUFF),
    Button(160, button_y_pos_4, 15, 15, MISTY_ROSE),
    Button(175, button_y_pos_4, 15, 15, LAVENDER_BLUSH),
    Button(190, button_y_pos_4, 15, 15, LINEN),
    Button(205, button_y_pos_4, 15, 15, OLD_LACE),
    Button(220, button_y_pos_4, 15, 15, PAPAYA_WHIP),
    Button(235, button_y_pos_4, 15, 15, SEA_SHELL),
    Button(250, button_y_pos_4, 15, 15, MINT_CREAM),
    Button(265, button_y_pos_4, 15, 15, SLATE_GRAY),
    Button(280, button_y_pos_4, 15, 15, LIGHT_SLATE_GRAY),
    Button(295, button_y_pos_4, 15, 15, LIGHT_STEEL_BLUE),
    Button(310, button_y_pos_4, 15, 15, LAVENDER),
    Button(325, button_y_pos_4, 15, 15, FLORAL_WHITE),
    Button(340, button_y_pos_4, 15, 15, ALICE_BLUE),
    Button(355, button_y_pos_4, 15, 15, HONEYDEW),
    Button(370, button_y_pos_4, 15, 15, IVORY),
    Button(385, button_y_pos_4, 15, 15, AZURE),
    Button(400, button_y_pos_4, 15, 15, BLACK),
    Button(415, button_y_pos_4, 15, 15, DIM_GRA),
    Button(430, button_y_pos_4, 15, 15, GRAY),
    Button(445, button_y_pos_4, 15, 15, DARK_GRAY),
    Button(460, button_y_pos_4, 15, 15, SILVER),
    Button(475, button_y_pos_4, 15, 15, LIGHT_GRA),
    Button(490, button_y_pos_4, 15, 15, GAINSBORO),
    Button(505, button_y_pos_4, 15, 15, WHITE),

    Button(310, button_y_pos_4+25, 35, 35, WHITE, "Erase", BLACK),
    Button(360, button_y_pos_4+25, 35, 35, WHITE, "Clear", BLACK),
    Button(410, button_y_pos_4+25, 35, 35, WHITE, "Save", BLACK)

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

                    if button.text == "Save":
                        temp = pygame.Rect(0, 0, WIDTH, HEIGHT-TOOLBAR_HEIGHT)
                        pygame.image.save(WIN.subsurface(temp), "temp.jpg")

    draw(WIN, grid, buttons)

pygame.quit()
