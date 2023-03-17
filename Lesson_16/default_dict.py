from loguru import logger
from collections import defaultdict

'''Example 1: Dictionary'''
def my_dict():
    dict = {1: 'Math', 2: 'Physical', 3: 'History'}
    logger.debug(dict)
    logger.debug(dict[1])
    logger.debug(dict[2])
    logger.debug(dict[3])
    logger.debug(dict[4])

def error_message():
    return "Key doesn't present"

def my_defaut_dict():
    ddict = defaultdict(error_message)
    ddict[1] = 'Math'
    ddict[2] = 'Physical'
    ddict[3] = 'History'

    logger.debug(ddict)
    logger.debug(ddict[1])
    logger.debug(ddict[2])
    logger.debug(ddict[3])
    logger.debug(ddict[4])

my_defaut_dict()