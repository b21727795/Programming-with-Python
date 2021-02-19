import sys

def create_maze(file_path):
    
    maze_matrix = list()
    maze_file = open(file_path,'r')
    
    for line in maze_file:
        
        row = list()
        for letter in line.strip():
            if (letter == 'W'):
                row.append([letter,False,False])
            elif (letter == 'P' or letter == 'F' or letter == 'S' or letter == 'H'):
                row.append([letter,True,False])
        maze_matrix.append(row)
    
    maze_file.close()
    return maze_matrix

def find_location(letter,maze_matrix): #Maze size can be dynamic,square,rectangle etc.
    
    i = 0
    for row in maze_matrix:
        j = 0
        for element in row:
            if (element[0] == letter):
                return [i,j]
            j+=1
        i+=1     
    return -1,-1

def print_maze(maze,solution,start,finish):
    row = len(maze)
    column = len(maze[0])
    
    solution_matrix = [['0' for j in range(column)] for i in range(row)] 
    
    for pair in solution:
        solution_matrix[pair[0]][pair[1]] = '1'
    
    
    solution_matrix[start[0]][start[1]] = 'S'
    solution_matrix[finish[0]][finish[1]] = 'F'

    for row in solution_matrix:
        print(', '.join(row))


def path(maze,location,path_list,finish): 
    
    row,column = location[0],location[1] #row,column coordinates
    pair = maze[row][column] #pair[0] = letter , pair[1] = valid_letter,pair[2] = visited before
    
    
    if(pair[1] == True):
        maze[row][column][2] = True #mark as visited
        path_list.append([row,column]) #found path
    
    #We found Final letter aka Final point,so turn back to base case
    if (maze[finish[0]][finish[1]][2] == True):
        return
    
    
  
    
    #Recursive Part
    #Statement Control respectively : Can I go to there in manner of mathematically, Have I visited before, Is a Wall or Open Road , Is Final point found
    if (row > 0 and maze[row - 1][column][2] == False and maze[row -1][column][1] == True and maze[finish[0]][finish[1]][2] == False): #Look Up
        path(maze, [row - 1, column], path_list,finish)
    
    if (column > 0 and maze[row][column -1][2] == False and maze[row][column - 1][1] == True and maze[finish[0]][finish[1]][2] == False):#Look left
        path(maze,[row, column - 1],path_list,finish)
    
    if (row < len(maze) - 1 and maze[row + 1][column][2] == False and maze[row + 1][column][1] == True and maze[finish[0]][finish[1]][2] == False):#Look down
        path(maze,[row + 1, column],path_list,finish)
    
    if (column < len(maze[0]) - 1 and maze[row][column + 1][2] == False and maze[row][column + 1][1] == True and maze[finish[0]][finish[1]][2] == False):#Look right
        path(maze,[row, column + 1],path_list,finish)
    
    #If there is dead end and if we could not find Final point yet,remove this dead end road until junction point
    if (maze[finish[0]][finish[1]][2] == False and maze[row][column][2] == True):
        path_list.pop()

def path_with_health(maze,location,path_list,finish,health,CONST_HEALTH,isDead):
    
    
    if(health < 0 and maze[finish[0]][finish[1]][2] == False):
        print('There is no path for health condition')
        isDead = True
        return
    
    row,column = location[0],location[1] #row,column coordinates
    pair = maze[row][column] #pair[0] = letter , pair[1] = valid_letter,pair[2] = visited before
    
    
    if (pair[1] == True):
        maze[row][column][2] = True #mark as visited
        path_list.append([row,column]) #found path
    
    


    #We found Final letter aka Final point,so turn back to base case
    if (maze[finish[0]][finish[1]][2] == True and isDead == False):
        return
    
    #Recursive Part
    #Statement Control respectively : Can I go to there in manner of mathematically, Have I visited before, Is a Wall or Open Road , Is Final point found
    if (pair[0] == 'H' and isDead == False):
        if (row > 0 and maze[row - 1][column][2] == False and maze[row -1][column][1] == True and maze[finish[0]][finish[1]][2] == False): #Look Up
            path_with_health(maze, [row - 1, column], path_list,finish,CONST_HEALTH -1,CONST_HEALTH,isDead)
        
        if (column > 0 and maze[row][column -1][2] == False and maze[row][column - 1][1] == True and maze[finish[0]][finish[1]][2] == False):#Look left
            path_with_health(maze,[row, column - 1],path_list,finish,CONST_HEALTH -1,CONST_HEALTH,isDead)
        
        if (row < len(maze) - 1 and maze[row + 1][column][2] == False and maze[row + 1][column][1] == True and maze[finish[0]][finish[1]][2] == False):#Look down
            path_with_health(maze,[row + 1, column],path_list,finish,CONST_HEALTH -1,CONST_HEALTH,isDead)
        
        if (column < len(maze[0]) - 1 and maze[row][column + 1][2] == False and maze[row][column + 1][1] == True and maze[finish[0]][finish[1]][2] == False):#Look right
            path_with_health(maze,[row, column + 1],path_list,finish,CONST_HEALTH -1,CONST_HEALTH,isDead)
    elif(isDead == False):
        if (row > 0 and maze[row - 1][column][2] == False and maze[row -1][column][1] == True and maze[finish[0]][finish[1]][2] == False): #Look Up
            path_with_health(maze, [row - 1, column], path_list,finish,health -1,CONST_HEALTH,isDead)
        
        if (column > 0 and maze[row][column -1][2] == False and maze[row][column - 1][1] == True and maze[finish[0]][finish[1]][2] == False):#Look left
            path_with_health(maze,[row, column - 1],path_list,finish,health -1,CONST_HEALTH,isDead)
        
        if (row < len(maze) - 1 and maze[row + 1][column][2] == False and maze[row + 1][column][1] == True and maze[finish[0]][finish[1]][2] == False):#Look down
            path_with_health(maze,[row + 1, column],path_list,finish,health -1,CONST_HEALTH,isDead)
        
        if (column < len(maze[0]) - 1 and maze[row][column + 1][2] == False and maze[row][column + 1][1] == True and maze[finish[0]][finish[1]][2] == False):#Look right
            path_with_health(maze,[row, column + 1],path_list,finish,health -1,CONST_HEALTH,isDead)    
    
    #If there is dead end and if we could not find Final point yet,remove this dead end road until junction point
    if (maze[finish[0]][finish[1]][2] == False and maze[row][column][2] == True and isDead == False):
        path_list.pop()

def main(maze_file,maze_health_file,health):
    
    print('***************** Normal Maze *************************************************')
    maze = create_maze(maze_file)
    maze_start = find_location('S',maze)
    maze_finish = find_location('F',maze)
    maze_solution = list()

    path(maze,maze_start,maze_solution,maze_finish)
    print_maze(maze,maze_solution,maze_start,maze_finish)

    print('**************** Maze with Health Condition *********************************')
    maze_with_health = create_maze(maze_health_file)
    maze_with_health_start = find_location('S',maze_with_health)
    maze_with_health_finish = find_location('F',maze_with_health)
    maze_solution = list()

    path_with_health(maze_with_health, maze_with_health_start, maze_solution, maze_with_health_finish, health, health,False)
    print_maze(maze_with_health,maze_solution,maze_with_health_start,maze_with_health_finish)

if __name__ == '__main__':
    
    maze_file = sys.argv[1]
    maze_health_file = sys.argv[2]
    health = int(sys.argv[3])
    
    
    main(maze_file,maze_health_file,health)
