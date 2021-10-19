import datetime
import logging
from stack import StackFrame
from typing import List, Dict

FILE: str = "/dev/null"
db: Dict[str, List[StackFrame]] = {}
EMPTY_STACK: StackFrame = StackFrame("no stacks left", "", "", datetime.datetime.now())


def add_stack_to_db(stack_frame: StackFrame):
    try:
        db[stack_frame.user].append(stack_frame)
    except KeyError:
        db[stack_frame.user] = [stack_frame]
    logging.debug(f'save {stack_frame} to {FILE}')
    pass


def pop_stack_from_db(user: str) -> str:
    try:
        stack_frame = db[user].pop()
    except (IndexError, KeyError):
        stack_frame = EMPTY_STACK

    logging.debug(f'popped {stack_frame}')
    return stack_frame.serialize()
