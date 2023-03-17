import random
from loguru import logger

def check_player_status():
    user_play = input('Would you like to play more? (yes/no)')
    if user_play.lower() == 'yes':
        return True
    elif user_play.lower() == 'no':
        return False
    else:
        logger.info('Please input valid value!')


def play_game():
    play = True
    player_name = input('What is your name? ')
    logger.info(f'******* Welcome {player_name} to the funny game *********')
    while play:
        user_choise = input('Please select a weapon: [R]OCK, [P]APER, or [S]CISSOR: ')
        if user_choise.upper() not in ['R', 'P', 'S']:
            logger.info('Please select valid weapon!')
        else:
            comp_choise = random.choice(['R', 'P', 'S'])
            logger.info(f'Computer chooses: {comp_choise}')
            if user_choise == comp_choise:
                logger.info('TIE')
            elif user_choise.upper() == 'R' and comp_choise == 'P':
                logger.info('Paper beats Rock, I win!')
            elif user_choise.upper() == 'R' and comp_choise == 'S':
                logger.info('Rock beats Scissor. You win!')
            elif user_choise.upper() == 'P' and comp_choise == 'R':
                logger.info('Paper beats Rock. You win!')
            elif user_choise.upper() == 'P' and comp_choise == 'S':
                logger.info('Scissor beats Paper. I win!')
            elif user_choise.upper() == 'S' and comp_choise == 'R':
                logger.info('Rock beats Scissor. I win!')
            else:
                logger.info('Scissor beats Paper. You win!')
            
            play = check_player_status()
            logger.info('******* GAME OVER **********')
        

if __name__ == '__main__':
    play_game()
