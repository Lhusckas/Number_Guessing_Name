import random
import os
import time
import art

clear = lambda: os.system('cls')
number_of_victories = 0

# The game() function is where the main game's located
def game(victory_ammount):
    '''The main game function.'''
    
    def update_victory_ammount(victories): victories += 1; return victories
    
    print(art.logo)
    print('''
Welcome to the Number Guessing Game! Feel free to play whenever you want.
You need to guess what is the chosen number between 1 to 100. Good luck!
''')

    chosen_number = random.randint(1, 100)
    
    difficulty = input("Choose the game's difficulty. Easy - 10 lives, or Hard - 5 lives: ").lower()
    
    if difficulty == "easy":
        player_lives = 10
    elif difficulty == "hard":
        player_lives = 5
    else:
        print("You need to type 'easy' or 'hard'. Reloading the game...")
        time.sleep(1)
        clear()
        game(victory_ammount = update_victory_ammount())
        
    guessing = True
    
    # The loop below will keep running until the player make a right guess or loses all the lives
    while guessing:
        player_guess = int(input("Guess a number: "))
        
        if player_guess == chosen_number:
            print("You've won! Congratulations!")
            victory_ammount += 1
            guessing = False
        elif player_guess != chosen_number:
            player_lives -= 1
            if player_lives > 0:
                if player_guess > chosen_number:
                    print("Your guess was higher than the chosen number.")
                elif player_guess < chosen_number:
                    print("Your guess was lower than the chosen number.")
                print(f"You have {player_lives} lives remaining.")
            elif player_lives <= 0:
                print(f"\nYou lost all your lives.")
                print(art.game_over)
                guessing = False
    
    play_again = input("Do you want to play again? (Y/N): ").lower()
    
    if play_again == "y":
        clear()
        game(victory_ammount = update_victory_ammount(victories = victory_ammount))
    else:
        print(f"You have a total of {victory_ammount} victories.")
        print(art.game_end)
        print("Clearing the console...")
        time.sleep(5)
        clear()
    
game(victory_ammount = number_of_victories)