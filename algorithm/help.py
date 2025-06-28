class Maze:
    def __init__(self):
        self.maze = [[1]]
        self.direction = "forward"
        self.l = 0
        self.w = 1
    def add_maze(self):
        
        if self.direction == "forward":
            self.l += 1
            self.maze.insert(1, [0 for i in range(self.w)])
        if self.direction == "backward":
            self.l += 1
            self.maze.insert(0, [0 for i in range(self.w)])
        if self.direction == "left":
            self.w += 1
            for i in self.maze:
                i.insert(1, 0)
        if self.direction == "right":
            self.w += 1
            for i in self.maze:
                i.insert(0, 0)

    def print_maze(self):
        for i in self.maze:
            print(i)


maze = Maze()

while True:
    x = input('Direction: ')
    if x == 'w':
        maze.direction = 'forward'
        maze.add_maze()
    if x == 'a':
        maze.direction = 'left'
        maze.add_maze()
    if x == 's':
        maze.direction = 'backward'
        maze.add_maze()
    if x == 'd':
        maze.direction = 'right'
        maze.add_maze()

    maze.print_maze()