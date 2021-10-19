import datetime
import logging

from stack import StackFrame
import persistence


from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


def pop_from_stack(user: str) -> str:
    logging.info(f' received call with arguments {request.args}')
    top_stack: StackFrame = persistence.pop_stack_from_db(user)
    return f"popped {top_stack} from stack"


def push_to_stack(user: str, topic: str, description: str) -> str:
    """
    Pushed a new StackFrame for user onto the corresponding stack
    :param topic: topic of the new talk stack
    :param user: user to which the new talk stack is added
    :param description: description of the new topic
    :return:
    """
    logging.info(f' received call with arguments {request.args}')

    date = datetime.datetime.now()
    new_stack = StackFrame(topic, description, user, date)
    persistence.add_stack_to_db(new_stack)
    return f"pushed {new_stack} to stack for {user}"


@app.route('/stack/<user>', methods=["POST", "GET"])
def stack(user: str):
    if request.method == 'POST':
        topic = request.form['tp']
        description = request.form['ds']
        push_to_stack(user, topic, description)

    elif request.method == 'GET':
        return pop_from_stack(user)
    else:
        logging.error("HTTP method not available")


if __name__ == '__main__':
    app.debug = True
    app.run()
