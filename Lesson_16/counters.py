from collections import Counter
from loguru import logger

str_example = 'python default_dict.py'
count = Counter(str_example)
# logger.debug(count)
for key, val in count.items():
    logger.debug(f'{key}: {val}')