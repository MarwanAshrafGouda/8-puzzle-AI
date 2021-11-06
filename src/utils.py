# visualizes the given board configuration
def string_to_grid(config: str):
    grid = ''
    for i in range(0, 3):
        for j in range(0, 3):
            grid += config[3 * i + j % 3]
        grid += '\n'
    return grid
