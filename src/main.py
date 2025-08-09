from src.utils.input_validator import input_validator
from src.game_logic.number_generator import computer_choice
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import Scorer


def main():
    number_to_guess= computer_choice(1,100)
    score = Scorer()
    while True:
        user_input = input_validator( 1, 100)
        if number_to_guess == user_input:
            print (f"YOU WON CONGRATS!! your final score is {score.get_score()}")

            break
        else:
            provide_hint(user_input, number_to_guess)
            score.decriment_score()



if __name__ == "__main__":
    main()


    while True:
        continue_game=input("Do you want to play again? (Enter any key to continue or 'q' to quit): ")
        if continue_game.lower() == 'q':
            break
        
        else:
            main()
       