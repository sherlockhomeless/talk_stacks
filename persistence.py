import logging

FILE: str


def add_stack_to_db(stack_frame):
    logging.debug('save %s to %s' % stack_frame, FILE)
    pass

