import datetime
import logging

from stack import StackFrame
import persistence


from flask import Flask, redirect, request
app = Flask(__name__)


@app.route('/stack/<user>', methods=["POST", "GET"])
def stack(user):
    if request.method == 'POST':
        return push_to_stack(user)
    elif request.method == 'GET':
        return pop_from_stack()
    else:
        logging.error("HTTP method not available")


def pop_from_stack():
    logging.error("Poping from Stack not implemented")
    raise NotImplementedError


def push_to_stack(user: str) -> str:
    """
    Pushed a new StackFrame for user onto the corresponding stack
    :param user:
    :return:
    """
    logging.info(f' received call with arguments {request.args}')
    new_stack: StackFrame = parse_push_request()
    persistence.add_stack_to_db(new_stack)
    return f"pushed {new_stack} to stack for {user}"


def parse_push_request() -> StackFrame:
    """
    Parses a request that should contain all information to construct a StackFrame
    The request is encapsulated by the 'request'-variable imported from flask
    :return:
    """
    user = request.args.get('user')
    topic = request.args.get('topic')
    description = request.args.get('description')
    date = datetime.datetime.now()
    return StackFrame(topic, description, user, date)


if __name__ == '__main__':
    app.debug = True
    app.run()
