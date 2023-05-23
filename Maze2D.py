import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(600, 600)

# Set up the turtle
t = turtle.Turtle()
t.shape('square')
t.color('white')
t.penup()

# Define the maze
maze1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 2, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

maze2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 3, 3, 4, 1, 2, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 3, 4, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 3, 3, 3, 3, 3, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

maze3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 2, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

maze4 = [
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 3, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 3, 3, 4, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 3, 3, 3, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 3, 3, 3, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 3, 3, 3, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 3, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 1, 2, 1, 1, 4, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
2
maze5 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 3, 3, 3, 1, 3, 1],
    [1, 0, 1, 0, 0, 1, 0, 3, 3, 3, 3, 1, 3, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 3, 3, 4, 1, 3, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 2, 1, 0, 0, 0, 1, 4, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 3, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 3, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def level_start():
    global maze
    global maze1
    global maze2
    global maze3
    global maze4
    global maze5
    
    A=random.randint(1, 5)
    
    if A==1:
        maze=maze1
        print('maze 1 loaded')
        
    elif A==2:
        maze=maze2
        print('maze 2 loaded')
        
    elif A==3:
        maze=maze3
        print('maze 3 loaded')
        
    elif A==4:
        maze=maze4
        print('maze 4 loaded')
        
    elif A==5:
        maze=maze5
        print('maze 5 loaded')
        
level_start()

# Define the starting point
start_x, start_y = 1, 1
t.goto(start_x * 30, start_y * 30)

# Define the movement functions
def move_up():
    new_x = t.xcor()
    new_y = t.ycor() + 30
    if is_valid_move(new_x, new_y):
        t.goto(new_x, new_y)

def move_down():
    new_x = t.xcor()
    new_y = t.ycor() - 30
    if is_valid_move(new_x, new_y):
        t.goto(new_x, new_y)

def move_left():
    new_x = t.xcor() - 30
    new_y = t.ycor()
    if is_valid_move(new_x, new_y):
        t.goto(new_x, new_y)

def move_right():
    new_x = t.xcor() + 30
    new_y = t.ycor()
    if is_valid_move(new_x, new_y):
        t.goto(new_x, new_y)

def is_valid_move(x, y):
    global t
    
    maze_x = int(x // 30)
    maze_y = int(y // 30)
    
    if maze[maze_y][maze_x] == 3:
        t.color('red')
        return True
    
    else:
        t.color('white')
        
    
    if maze[maze_y][maze_x] == 1:
        return False
    
    elif maze[maze_y][maze_x] == 2:
        t.color('red')
        print("You Won")
        quit()
    
    elif maze[maze_y][maze_x] == 4:
        
        print("YOU DIED")
        time.sleep(10)
        quit()
        
    else:
        return True
    

# Set up the key bindings
screen.listen()
screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_down, 'Down')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')

# Start the game
screen.mainloop()
