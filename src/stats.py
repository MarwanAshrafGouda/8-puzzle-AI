class StatsFile(object):
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'w') as my_file:
            my_file.write("")

    # passed to algorithms.search to print current configuration.
    def write_config(self, msg):
        with open(self.file_name, 'a') as my_file:
            my_file.write(msg + "\n")

    # used to print the total stats at the end of the file.
    def write_stat(self, msg):
        with open(self.file_name, 'a') as my_file:
            my_file.write(msg + "\n")
