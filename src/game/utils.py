class StatsFile(object):
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'w') as file:
            file.write("")

    # used to print the total stats at the end of the file.
    def write(self, msg):
        with open(self.file_name, 'a') as file:
            file.write(msg + "\n")


# turns the given string to a grid-like format
def string_to_grid(config: str):
    grid = ''
    for i in range(0, 3):
        for j in range(0, 3):
            grid += config[3 * i + j % 3]
        grid += '\n'
    return grid
