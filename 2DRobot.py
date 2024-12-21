from graphics import *  # import the graphics module to display robot grid
import random

'''
Calculates and returns the total columns in the whole grid
'''
def getNumberOfColumns():
    return len(grid[0]) #grid[0] is the top row (first list in the grid)

'''
Calculates and returns the total rows in the whole grid
'''
def getNumberOfRows():
    return len(grid)  # the number of items in the grid is the number of rows

'''
Returns the string of the robot's direction, "L", "R", "U", or "D"
'''
def getDirection():  # No changes to this function
    return facing  # returns direction


'''
Returns the robot's current location, as an ordered pair: row, column
'''
def getRobotLocation():
    for r in range(getNumberOfRows()):   # for each row
        for c in range(getNumberOfColumns()):   # for each column
            if grid[r][c] == 1: # if the coordinates (within the list) are equal to 1 (what the robot is)
                return r, c  # returns the coordinates


'''
Change the variable facing to rotate the robot 90 degrees clockwise
No return needed.
'''
def rotateRight():
    global facing
    if facing == "R":   #if it faces right, turn right (face down)
        facing = "D"
    elif facing == "D": #if it is facing down, a right turn would face left
        facing = "L"
    elif facing == "L": #if it starts at facing left, a right turn would face up
        facing = "U"
    elif facing == "U": #if it faces up, the right turn would face right
        facing = "R"

'''
Change the variable facing to rotate the robot 90 degrees counterclockwise
No return needed.
'''
def rotateLeft():  #all the same as rotateRight() but reverse
    global facing
    if facing == "R": #starting right, left turn means facing up
        facing = "U"
    elif facing == "D": #starting down, left turn means facing right
        facing = "R"
    elif facing == "L": #start left, left turn means facing down
        facing = "D"
    elif facing == "U": #start while facing up, left turns means facing left
        facing = "L"

'''
Returns True or False depending on whether the robot has an open space in front,
or if it is against a wall/obstacle.
'''
def canMove(direction):
    if direction == "R" and getRobotLocation()[1] != len(grid[0])-1:  # checks if the direction robot is facing is
        # right AND if x coordinate is NOT equal to the furthest x coordinate possible (if it's hugging the wall)
        return True
    elif direction == "L" and getRobotLocation()[1] != 0: # same as above, just checks if x coordinate is 0 and
        # hugging wall
        return True
    elif direction == "U" and getRobotLocation()[0] != 0: #same as above, checks if y is 0 (at the top and facing up)
        return True
    elif direction == "D" and getRobotLocation()[0] != len(grid)-1: #same as "U" but checks if y is at the bottom
                                                # this has to ^^^ be -1 because the length and the actual value are
                                                # offset (value starts at 0, length starts at 1)
        return True # returns whether the robot can move
    else:
        return False # only runs if above 4 are all unsatisfied.

'''
Checks to see if the robot can move in the direction it is facing.
Changes the grid based on the robot's movement in that direction.
Prints "unable to move" if the way is blocked.
'''
def moveForward():
    if canMove(facing): # can the robot move forward? (Boolean)
        row, col = getRobotLocation() # where is the robot in the grid? (Integers)
        if facing == "R":
            grid[row][col] = 0  #first changes the value in the grid of where the robot currently is to 0
            col += 1
            grid[row][col] = 1  # then changes the new position to 1 after adding col by 1 - all following are same as
            # this, vertical changes alter row instead of col
        elif facing == "L":
            grid[row][col] = 0
            col -= 1
            grid[row][col] = 1
        elif facing == "U":
            grid[row][col] = 0
            row -= 1
            grid[row][col] = 1
        elif facing == "D":
            grid[row][col] = 0
            row += 1
            grid[row][col] = 1
    else:
        print("Cannot move forward!")
    # update the grid accordingly



'''
Displays the current grid in the graphics window,
including blank squares and the robot itself
'''
def displayRobotGrid():
    for r in range(getNumberOfRows()):  # r represents rows
        for c in range(getNumberOfColumns()):  # c represents columns
            s = Rectangle(Point(20*c, 20*r), Point(20*c+20, 20*r+20))
            #these three lines draw the grid using the nested for loops
            s.setFill('white')
            s.draw(win)
    r, c = getRobotLocation()
    #the above assigns usable and accessible variables to the coordinates, instead of getting both at once
    # we can pick and choose now
    if getDirection() == "R":    # the coordinates used are from the in-class coordinates from the slideshow
        robot = Polygon(Point(20*c, 20*r), Point(20*c, 20*r+20), Point(20*c+20, 20*r+10))
        robot.setFill("black")
    if getDirection() == "L":
        robot = Polygon(Point(20*c+20, 20*r), Point(20*c+20, 20*r+20), Point(20*c, 20*r+10))
        robot.setFill("black")
    if getDirection() == "D":
        robot = Polygon(Point(20*c, 20*r), Point(20*c+20, 20*r), Point(20*c+10, 20*r+20))
        robot.setFill("black")
    if getDirection() == "U":
        robot = Polygon(Point(20*c, 20*r+20), Point(20*c+20, 20*r+20), Point(20*c+10, 20*r))
        robot.setFill("black")
    #fill in other directions for other triangles
    robot.draw(win)


'''
Initializes the graphics and the list representing the grid
'''
def setup():   #No changes to this function
    global win, grid, facing, s, goalSquareRow, goalSquareCol#these variables can be accessed throughout program

    #grid is a list of lists. Each list corresponds to a row of squares.
    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    robotSpawnRow = random.randint(0, len(grid)-1)  #finds random row value
    robotSpawnCol = random.randint(0, len(grid[0])-1)   #finds random col value
    grid[int(robotSpawnRow)][robotSpawnCol] = 1   #could be done in 1 line, but clearer this way
    facing = "D" #R or L or U or D
    #figure out reasonable height and width of the graphics window
    gridHeight = 0
    if len(grid) * 20 < 350:
        gridHeight = 350
    else:
        gridHeight = len(grid)*20

    gridWidth = 0
    if len(grid[0]) * 20 < 350:
        gridWidth = 350
    else:
        gridWidth = len(grid[0])*20

    #set up initial window
    win = GraphWin("Robot", gridWidth, gridHeight, autoflush=False)
    win.setBackground("green")
    directionText = Text(Point(win.getWidth()/2, win.getHeight()/5*4),
        "Press right arrow or 'r' to turn right 90 degrees\n" +
        "Press left arrow or 'l' to turn left 90 degrees\n" +
        "Press up arrow or 'u' to move forward 1 space\n" +
        "Press 'x' to stop\n" +
        "Get to the yellow square!")
    directionText.setFill("white")
    directionText.draw(win)



'''
The driver of the program. Takes user input through keys
and manipulates the robot appropriately.
'''
def main(): #No changes to this function
    setup()
    goalSquareRow = random.randint(0, getNumberOfRows() - 1)  #gets random row
    goalSquareCol = random.randint(0, getNumberOfColumns() - 1) #random column
    over = False
    while not over:
        displayRobotGrid()
        goalSquare = Rectangle(Point(20 * goalSquareCol, 20 * goalSquareRow),
                               # these two lines define a certain square to be a goal square
                      Point(20 * goalSquareCol + 20, 20 * goalSquareRow + 20))
        goalSquare.setFill('yellow') #colors goal square
        goalSquare.draw(win) #draws goal square
        if getRobotLocation() == (goalSquareRow, goalSquareCol): #checks is robot is at goal square
            goalSquare.setFill('green') #changes coal square color
            directionText2 = Text(Point(win.getWidth() / 2, win.getHeight() / 2), #copied from above (given in skeleton)
                                  "You win!")
            directionText2.setFill("white")
            directionText2.draw(win)
        key = win.getKey() #waits for user key press
        if key == 'x': #if user presses 'x' key, closes window
            over = True
            win.close()
        elif key == 'd' or key == "Right":
            rotateRight()
        elif key == 'a' or key == "Left":
            rotateLeft()
        elif key == 'w' or key == "Up":
            moveForward()


if __name__ == "__main__":
    main()
