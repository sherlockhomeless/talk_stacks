import logging

FILE: str = "/dev/null"


def add_stack_to_db(stack_frame):
    logging.debug(f'save {stack_frame} to {FILE}')
    pass

