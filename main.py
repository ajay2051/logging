import logging
import employee
from typing import Optional

# DEBUG: Detailed Information, typically of interest only when diagnosting problems.
# INFO: Confirmation that things
# are working as expected. WARNING: An Indication that something unexpected happen, or indicative of some problems in
# the near future ( e.g  'disk space low'). The software is still working as expected.
# ERROR: Due to a more serious
# problem, the software has not been able to perform some functions.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# Default log is set to WARNING. 


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(' %(asctime)s :: %(levelname)s :: %(message)s')

file_handler = logging.FileHandler('main.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# logging.basicConfig(filename='test.log', filemode='w' level=logging.DEBUG, format=' %(asctime)s :: %(levelname)s ::
# %(message)s')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried Divide By Zero')
    else:
        return result


num_1 = 20
num_2 = 0

result_add = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, result_add))

result_subtract = subtract(num_1, num_2)
logger.debug('Subtract: {} - {} = {}'.format(num_1, num_2, result_subtract))

result_multiply = multiply(num_1, num_2)
logger.debug('Multiply: {} * {} = {}'.format(num_1, num_2, result_multiply))

result_divide = divide(num_1, num_2)
logger.debug('Divide: {} / {} = {}'.format(num_1, num_2, result_divide))
