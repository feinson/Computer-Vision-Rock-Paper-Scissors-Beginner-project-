import random
list_of_moves = ["Rock", "Paper", "Scissors"]

def get_computer_choice():

    return random.choice(list_of_moves)

def show_please_enter():
    print("Please enter either 1, 2 or 3.")

def get_user_choice():

    while True:
        print("To select a move press:\n")

        for count, move in enumerate(list_of_moves):
            print(f"{count+1} => {move}")

        user_input = input("Please enter your choice.\n")

        try:
            user_choice = int(user_input)

            if user_choice in [1,2,3]:
                break
            
            else:
                show_please_enter()

        except:
            show_please_enter()
        
        return user_choice

print(get_computer_choice())
print(get_user_choice())