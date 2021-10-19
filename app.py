import datetime
import logging

from stack import StackFrame
import persistence


from flask import Flask, redirect, request, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/pop')
def pop_from_stack():
    logging.info(f' received call with arguments {request.args}')
    top_stack: StackFrame = persistence.pop_stack_from_db()
    if top_stack == None:
        return "stack is empty"
    return f"popped {top_stack} from stack"

@app.route('/push/<user>/<topic>/<description>')
def push_to_stack(user: str, topic: str, description: str) -> str:
    """
    Pushed a new StackFrame for user onto the corresponding stack
    :param user:
    :return:
    """
    logging.info(f' received call with arguments {request.args}')

    date = datetime.datetime.now()
    new_stack = StackFrame(topic, description, user, date)
    persistence.add_stack_to_db(new_stack)
    return f"pushed {new_stack} to stack for {user}"


@app.route('/stack', methods=["POST", "GET"])
def stack():
    if request.method == 'POST':
          name = request.form['nm']
          topic = request.form['tp']
          description = request.form['ds']
          return redirect(url_for('push_to_stack', user = name, topic = topic, description = description))
    elif request.method == 'GET':
          return pop_from_stack()
    else:
        logging.error("HTTP method not available")

if __name__ == '__main__':
    app.debug = True
    app.run()
