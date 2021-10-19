import logging

FILE: str = "/dev/null"
db = []

def add_stack_to_db(stack_frame):
    db.append(stack_frame)
    logging.debug(f'save {stack_frame} to {FILE}')
    pass

def pop_stack_from_db():
    if len(db) == 0:
        return None
    else:
        stack_frame = db.pop();
        logging.debug(f'popped {stack_frame}')
        return stack_frame
