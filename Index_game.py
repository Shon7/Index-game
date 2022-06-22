print('WELCOME TO THE MINI INDEX GAMING')
game_list = [0,1,2]
def display_game(g):
    print("Here is the current list : ",g) 

def position_choice():
    choice = ''
    acceptable_list = ['0','1','2']
    while choice not in acceptable_list:
        choice = input("Enter the index position : ")
        if choice not in acceptable_list:
            print('Sorry! not in acceptable list')
    return int(choice)

def replacement_choice(gamelist,position):
    user_placement = input('Type a string for the index position :')
    gamelist[position] = user_placement
    return(game_list) 

def gameon_choice():
    choice = ''
    acceptable_list = ['y','n']
    while choice not in acceptable_list:
        choice = input("Keep playing? Y or N : ").lower()
        if choice not in acceptable_list:
            print('Sorry! Please enter Y or N')
    if choice == 'y' :
        return True
    else:
        return False

game_on = True
game_list = [0,1,2]
while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()

