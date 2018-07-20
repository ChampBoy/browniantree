# Sunny Parawala paraw001

#Import Statements
import turtle, math, random

def main(): 
    turtle.setworldcoordinates(0,0,199,199)
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    n=treeSize()
    grid=[]
    grid=make_grid(grid) #In the grid list the x-coordinate supplied gives the column number and
    turtle.goto(100,100) #the y-coordinate supplied gives the row number
    turtle.dot(5,"blue")
    grid[100][100]=True
    screen=turtle.getscreen()
    screen.tracer(0)
    draw_tree(grid,n)


def treeSize(): #Function to ask user for number of particles in the tree
    user_input=int(turtle.textinput('','Enter tree size: '))
    return user_input

def make_grid(grid): #Function to create grid
    for i in range(200):
        grid.append([])
        for j in range(200):
            grid[i].append(False)
    return grid

def draw_tree(grid,n): #Function to form Brownian Tree
    cluster_r=0 
    temp_radius=0
    xcor=100
    ycor=100
    while n-1>0: # As one particle already at centre we start with n-1
        turtle.goto(100,100)
        random_angle=math.radians(random.uniform(0,360))
        xcor=int(round(100+(cluster_r+1)*math.sin(random_angle),0))
        ycor=int(round(100+(cluster_r+1)*math.cos(random_angle),0))
        turtle.goto(xcor,ycor)
        need_random_walk=0
        if xcor<200 and ycor<200 and xcor>=0 and ycor>=0: 
            if hasNeighbor(grid,ycor,xcor):
                cluster_r+=1
                turtle.dot(5,"blue") 
                turtle.update()
                grid[xcor][ycor]=True

            else:
                need_random_walk=1 #Random walk needed if particle didnt stick exactly after spawn
        else:
            need_random_walk=1 #Random walk needed if outside grid co-ordinates

        if need_random_walk==1: #Do a random walk if needed
                i=0
                found_particle=0
                while i<200 and found_particle==0:
                    j=random.randint(1,4) #Take a random walk
                    if j==1:
                        xcor+=1
                    elif j==2:
                        ycor+=1
                    elif j==3:
                        xcor=xcor-1
                    elif j==4:
                        ycor=ycor-1
                    temp_distance=math.sqrt((xcor-100)**2+(ycor-100)**2) #Distance of new particle from origin
                    if xcor<200 and ycor<200 and xcor>=0 and ycor>=0: #Stick only if inside grid
                        if hasNeighbor(grid,ycor,xcor):
                            turtle.goto(xcor,ycor)
                            turtle.dot(5,"blue") 
                            turtle.update()
                            if temp_distance>cluster_r:
                                cluster_r=temp_distance #Updating Cluster radius
                            grid[xcor][ycor]=True
                            found_particle=1
                    i=i+1 
                if found_particle==0:
                    n=n+1 # Will repeat if particle doesnt stick
        n=n-1

def hasNeighbor(grid,row,col): # Function to check whether grid location has a neighbor

    if grid[col][row]==True: #Check if particle already present at a location
        return False
    if row!=0 and row!=199 and col==0:# Left Bordering Line
        if grid[0][row+1]==True or grid[0][row-1]==True or grid[1][row]==True or grid[1][row+1]==True or grid[1][row-1]==True: 
            return True
    elif col==0 and row==0: #Left Bottom Corner
        if grid[0][1]==True or grid[1][0]==True or grid[1][1]==True:
            return True
    elif row==0 and col!=0 and col!=199: #Bottom Border Line 
        if grid[col][1]==True or grid[col-1][0]==True or grid[col+1][0]==True or grid[col-1][1]==True or grid[col+1][1]==True:
            return True
    elif row==0 and col==199: #Right Bottom Corner
        if grid[199][1]==True or grid[198][0]==True or grid[198][1]==True:
            return True
    elif  row!=0 and row!=199 and col==199: #Right Border Line
        if grid[199][row-1]==True or grid[198][row]==True or grid[199][row+1]==True or grid[198][row+1]==True or grid[198][row-1]==True:
            return True
    elif row==199 and col==199: #Right Top Corner
        if grid[198][199]==True or grid[199][198]==True or grid[198][198]==True:
            return True
    elif row==199 and col!=0 and col!=199: #Top Border Line
        if grid[col+1][199]==True or grid[col-1][199]==True or grid[col][198]==True or grid[col-1][198]==True or grid[col+1][198]==True:
            return True
    elif row==199 and col==0:# Top Left Corner
        if grid[0][198]==True or grid[1][199]==True or grid[1][198]==True:
            return True
    else: #For All Other Cases
        ezzy = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1)]
        for x in ezzy:
            a,b = x
            grid[col+a][row+b] == True
        if grid[col+1][row]==True or grid[col][row+1]==True or grid[col-1][row]==True or grid[col][row-1]==True or grid[col-1][row+1]==True or grid[col+1][row+1]==True or grid[col-1][row-1]==True or grid[col+1][row-1]==True:
            return True

    return False # If No neighboring position has a particle return false

if __name__=='__main__':
    main()

