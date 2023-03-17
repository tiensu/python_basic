from loguru import logger

''' Method 1: Implement QUEUE using list '''
def create_queue_list():
    # init a queue
    queue = []

    # adding elements to the queue
    queue.append('a')
    queue.append('b')
    queue.append('c')

    logger.info('Init queue:')
    logger.info(queue)

    # remove elements from the queue
    logger.info('Elements dequeued from the queue:')
    for _ in range(0, len(queue)):
        logger.info(queue.pop(0))

    logger.info('Queue after removing elements:')
    logger.info(queue)


'''Method 2: Implement QUEUE using collections.deque'''
from collections import deque

def create_queue_coll():
    # init a queue
    queue = deque()

    # add elements to the queue
    queue.append('x')
    queue.append('y')
    queue.append('z')
    logger.info('Init queue:')
    logger.info(queue)

    # remove elements from the queue
    logger.info('Elements dequeued from the queue:')
    for _ in range(len(queue)):
        logger.info(queue.popleft())

    logger.info('Queue after removing all elements:')
    logger.info(queue)

# create_queue_coll()

'''Method 3: Implement QUEUE using queue.Queue'''
from queue import Queue

def create_queue_buildin():
    # init queue
    queue = Queue(maxsize=5)
    logger.info(f'Maxsize of queue: {queue.qsize()}')
    
    # add some elements into queue
    list_e = ['Ha Noi', 'Ha Nam', 'Thai Binh', 'Hung Yen', 'Bac Ninh', 'Hai Duong']
    for e in list_e:
        if(not queue.full()):
            queue.put(e)

    # check queue whether full or not
    logger.info(f'Queue full: {queue.full()}')
    logger.info(f'Maxsize of queue: {queue.qsize()}')

    # remove some elements from queue
    logger.info('Element dequeued from the queue:')
    for _ in range(queue.qsize()):
        logger.info(queue.get())

    # check queue whether empty or not
    logger.info(f'Queue empty: {queue.empty()}')

create_queue_buildin()