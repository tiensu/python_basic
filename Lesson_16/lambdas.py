from loguru import logger

# Example 1: Condiction checking
# without lambda
def check_num(num):
    if isinstance(num, int):
        logger.debug(f'{num} is integer')
    else:
        logger.debug(f'{num} is not integer')

# check_num('abc')

# with lambda
format_check = lambda num: logger.debug(f'{num} is integer') if isinstance(num, int) else logger.debug(f'{num} is not integer')
# format_check('abc')

# Example 2:
new_list = [lambda arg=x: arg*10 for x in range(1, 5)]
for item in new_list:
    logger.debug(item())