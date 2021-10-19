import datetime
import logging

from stack import StackFrame
import persistence


from flask import Flask, redirect, request
app = Flask(__name__)


@app.route('/push_stack/<user>')
def edit_stack(user):

    return "cool"


@app.route('/pop_stack/<user', methods=["POST"])
def push():
    logging.info(f' received call with arguments {request.args}')
    new_stack: StackFrame = parse_push_request(request)
    persistence.add_stack_to_db(new_stack)

def parse_push_request(r: request) -> StackFrame:
    """
    Parses a request that should contain all information to construct a StackFrame
    :param r:
    :return:
    """
    user = r.args.get('user')
    topic = r.args.get('topic')
    description = r.args.get('description')
    date = datetime.datetime.now()
    return StackFrame(user, topic, description, date)





if __name__ == '__main__':
    app.debug = True
    app.run()
