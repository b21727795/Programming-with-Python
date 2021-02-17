import sys

def create_board(board_size):
    
    count = 0 # 0 to  board_size**2 counter
    unmarked_board = list() #Our initial,empty matrix
    
    for x in range(board_size):
        
        row = list() #this empty list represents every row in a matrix
        
        for y in range(board_size):
            row.append(count)
            count+=1            
        
        unmarked_board.append(row) #we add every filled row to our list,to build matrix
    
    return unmarked_board #return created matrix with dynamic size

def find_number_of_digits(number):
    
    """
    it takes number as input, then finds number_of_digits.
    """
    number_of_digits = 0
    
    while (number > 0):
        
        number_of_digits+=1
        number //= 10
    
    return number_of_digits

def print_board(board,board_size):
    
    format_width = find_number_of_digits(board_size * board_size) #Simply we find number of digits
    
    for i in range(board_size):
        for j in range(board_size):
            
            print(" {:>{width}}".format(board[i][j], width=format_width),end='') #While printing, we printed right based corresponding to number of digits aka width
        print('\n',end = '')

def control_of_select(board,board_size,select,Player):
    
    if (select < 0 or select >= board_size**2):
        print('Please enter a valid number ')
        return
    
    if (Player):
        if (board[select // board_size][select % board_size] == select):
            
            board[select // board_size][select % board_size] = 'X'
            is_game_end(board,board_size)
        
        elif (board[select // board_size][select % board_size] == 'X'):
            print('You have made this choice before ')
        
        elif (board[select // board_size][select % board_size] == 'O'):
            print('The other player select this cell before ')
      
    
    else:
        if (board[select // board_size][select % board_size] == select):
            
            board[select // board_size][select % board_size] = 'O'
            is_game_end(board,board_size)
        
        elif (board[select // board_size][select % board_size] == 'O'):
            print('You have made this choice before')
        
        elif (board[select // board_size][select % board_size] == 'X'):
            print('The other player select this cell before')
        
def search_row(board,board_size): #it searches horizontal unbroken match
    for row in board:
        if (row == ['X' for x in range(board_size)] or row == ['O' for y in range(board_size)] ):
            return True
    return False

def search_column(board,board_size): #it searches vertical unbroken match
    for i in range(board_size):
        compare_list = list()
        for j in range(board_size):
            compare_list.append(board[j][i])
        if (compare_list == ['X' for x in range(board_size)] or compare_list == ['O' for y in range(board_size)]):
            return True
    return False

def search_diagonal(board,board_size):  #it searches firstly left diagonal unbroken match,then right diagonal unbroken match
    compare_list = list()
    
    for i in range(board_size):
        compare_list.append(board[i][i])
    if (compare_list == ['X' for x in range(board_size)] or compare_list == ['O' for y in range(board_size)]): #left diagonal control
        return True
    
    
    compare_list = list()
    
    for i,j in zip(range(board_size),range(board_size - 1 , -1,-1)):
        compare_list.append(board[i][j])
    if (compare_list == ['X' for x in range(board_size)] or compare_list == ['O' for y in range(board_size)]): #right diagonal control
        return True
    
    return False

def search_draw(board,board_size): #It searches all board to find unselected position for draw situation
    count = 0
    for i in range(board_size):
        for j in range(board_size):
            if(board[i][j] == count):
                return False
            count+=1
    return True


def is_game_end(board,board_size): #Is game end with any Winner
    
    
    row_control = search_row(board,board_size)
    column_control = search_column(board,board_size)
    diagonal_control = search_diagonal(board,board_size)

    if (row_control == True or column_control == True or diagonal_control == True):
        return True
    
    return False

                
    

def main(): #Game flow
    
    board_size = int(input('What is the size of Game GoPy ? :')) 
    
    if(board_size < 2):
        print('board size should be bigger than 1')
        sys.exit()

    board = create_board(board_size)
    print_board(board,board_size)

    Player = True # True is Player1 aka 'X' ,False is Player2 aka 'O'
    
    while(True): #Game Loop
        
        if (Player): #Player 1's turn
            
            select = int(input('Player 1 turn --> '))
            win = control_of_select(board,board_size,select,Player)
            
            if (win):
                print('Winner: X')
                break

            Player = False
            
        else: #Player 2's turn
            
            select = int(input('Player 2 turn --> '))
            control_of_select(board,board_size,select,Player)
            
            if (win):
                print('Winner: X')
                break
            
            Player = True
        
        print_board(board,board_size)
        
        draw = search_draw(board,board_size)
        if (draw):
            print("Draw!!!")
            break

if  __name__ == '__main__':
    main()