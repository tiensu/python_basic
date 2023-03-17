from loguru import logger
'''Method 1: Implement stack using list'''

def create_stack_list():
    # init stack
    stack = []

    # add some elements into stack
    stack.append('a')
    stack.append('b')
    stack.append('c')

    logger.info('Init stack:')
    logger.info(stack)

    # remove elements from the stack
    logger.info('Elements popped from the stack:')
    for _ in range(len(stack)):
        logger.info(stack.pop())

    logger.info('Stack after all elements are popped:')
    logger.info(stack)

# create_stack_list()

'''Method 2: Implement QUEUE using collections.deque'''
from collections import deque
def create_stack_coll():
    # init a queue
    stack = deque()

    # add elements to the stack
    stack.append('x')
    stack.append('y')
    stack.append('z')
    logger.info('Init stack:')
    logger.info(stack)

    # remove elements from the stack
    logger.info('Elements dequeued from the stack:')
    for _ in range(len(stack)):
        logger.info(stack.pop())

    logger.info('stack after removing all elements:')
    logger.info(stack)

# create_queue_coll()

'''Method 3: Implement STACK using queue.Queue'''
from queue import LifoQueue

def create_stack_buildin():
    # init stack
    stack = LifoQueue(maxsize=5)
    logger.info(f'Stack size: {stack.qsize()}')

    # put some elements into stack
    list_e = ['Dog', 'Cat', 'Bird', 'Horse', 'Cow', 'Ship']
    for e in list_e:
        if not stack.full():
            stack.put(e)

    
    logger.info(f'Stack full: {stack.full()}')
    logger.info(f'Stack size: {stack.qsize()}')

    # removing elements from stack
    logger.info('Elements popped from the stack:')
    for _ in range(0, stack.qsize()):
        logger.info(stack.get())

    logger.info(f'Stack empty: {stack.empty()}')

create_stack_buildin()