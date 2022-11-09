import random
list_of_moves = ["Rock", "Paper", "Scissors"]

def get_computer_choice():

    return random.choice(list_of_moves)


def show_please_enter():

    print("Please enter either 1, 2 or 3.\n")


def get_user_choice():

    while True:
        print("To select a move press:\n")

        for count, move in enumerate(list_of_moves):
            print(f"{count+1} => {move}")

        user_input = input("Please enter your choice.\n")

        try:
            
            user_input = int(user_input)
            
            if user_input in [1,2,3]:
                break
            
            else:
                show_please_enter()

        except:
            show_please_enter()
        

    return list_of_moves[user_input-1]


def get_winner(computer_choice, user_choice):

    hierarchy = ["Rock", "Scissors", "Paper", "Rock"]

    if computer_choice == user_choice:
        print("It is a tie!")
        return

    elif hierarchy.index(computer_choice) + 1 == hierarchy.index(user_choice,1):
        
        print("You lost")
        return computer_choice
        
    else:
        print("You won!")
        return user_choice

# a=get_computer_choice()

# b=get_user_choice()
# print(a,b)

# get_winner(a,b)