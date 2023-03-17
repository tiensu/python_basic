import random
from loguru import logger

attempts_list = []

def show_score():
    if not attempts_list:
        logger.info('You do not play any time. Play the to get scrore!')
    else:
        logger.info(f'Best score is {min(attempts_list)} attempts')

def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    logger.info('****** WELCOME TO FUN GAME ******')
    player_name = input('What is your name?: ')
    wanna_play = input(f'Hi {player_name}, would you like to play the game? (Enter yes/no): ')
    
    while wanna_play.lower() == 'yes':
        guess_num = int(input('Pick up any number between 1 and 10: '))
        if guess_num > 10 or guess_num < 0:
            logger.info('Invalid number. Try again!')
            continue
        attempts += 1

        if guess_num == rand_num:
            logger.info('Congrastiation! You are correct!')
            attempts_list.append(attempts)
            wanna_play = input('Would you like to play again? (yes/no): ')
            if wanna_play == 'yes':
                rand_num = random.randint(1, 10)
                attempts = 0
            else:
                show_score()
        elif guess_num < rand_num:
            logger.info('It is lower.')
        else:
            logger.info('It is higher.')

if __name__ == '__main__':
    start_game()

        