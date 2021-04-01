def matrix(p_name, get_pos, get_game,matrix_list):
    '''function to allocate game position and game string'''

    # allocate the game to the position
    matrix_list[get_pos] = get_game

    # state the status of the game
    status = False
    # display the list
    print(str(matrix_list[:3])+'\n'+str(matrix_list[3:6])+'\n'+str(matrix_list[6:9]))

    # check if the game correspond diagonally,
    # horizontally and vertically
    if (matrix_list[0]==matrix_list[1]==matrix_list[2]):
        status = True
    elif (matrix_list[3]==matrix_list[4]==matrix_list[5]):
        status= True
    elif (matrix_list[6]==matrix_list[7]==matrix_list[8]):
        status= True
    elif (matrix_list[0]==matrix_list[3]==matrix_list[6]):
        status= True
    elif (matrix_list[1]==matrix_list[4]==matrix_list[7]):
        status= True
    elif (matrix_list[2]==matrix_list[4]==matrix_list[6]):
        status= True
    elif (matrix_list[2]==matrix_list[5]==matrix_list[8]):
        status= True
    elif (matrix_list[0]==matrix_list[4]==matrix_list[8]):
        status= True
    else:
        print("keep on playing\n")
    return status

# list to store player name
player_name = []

# get the name of the first player
p1 = str(input("Enter player 1 name: "))

# append player one name to the player_name list
player_name.append(p1)

# get the name of the second player
p2 = str(input("Enter player 2 name: "))

# append player one name to the player_name list
player_name.append(p2)

# string to show game message
game_message = ""

# the list container
matrix_list = [[0],[1],[2],[3],[4],[5],[6],[7],[8]]

print("\nHere are the position of the matrix")
# first display the matrix box
print(str(matrix_list[:3])+'\n'
        +str(matrix_list[3:6])+'\n'
        +str(matrix_list[6:9])+'\n')

# loop through how many times the game will play
active = True
while active:
    for i in range(0,4):
        # print the first player name
        print(player_name[0], "turn to play")

        # get the position on the matrix list
        # for which the player wants to play
        get_pos = int(input("Enter the position to play: "))

        # allocate the position to the position list
        get_game = str(input("Enter your game: "))
        if(matrix(player_name[0], get_pos, get_game, matrix_list)):
            game_message = "Game over! "+player_name[0]+" won\n"
            print(game_message)
            break 

        # print the second player name
        print(player_name[1], "turn to play")

        # get the position on the matrix list
        # for which the player wants to play
        get_pos = int(input("Enter the position to play: "))

        # allocate the position to the position list
        get_game = str(input("Enter your game: "))
        if(matrix(player_name[0], get_pos, get_game, matrix_list)):
            game_message = "Game over! "+player_name[1]+" won\n"
            print(game_message)
            break

    else:
        print("Game over! No more moves")

    # Does player wants to play again
    reply = input("Do you want to play again (y/n): ")
    if reply == 'y':
        active = True
        # reset the game
        matrix_list = [[0],[1],[2],[3],[4],[5],[6],[7],[8]]
        print("\nHere are the position of the matrix")
        # first display the matrix box
        print(str(matrix_list[:3])+'\n'
                +str(matrix_list[3:6])+'\n'
                +str(matrix_list[6:9])+'\n')
    else:
        active = False