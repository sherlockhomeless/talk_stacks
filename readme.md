# Talk Stacks

Talk stacks is a REST-principle based interface that lets you keep track of interesing topics to talk about with friends.

## Use case

You know the situation, where you have a super interesting idea that you want to discuss with a friend immediately, but you are in the library, in a noisy train or a too drunk to speak intelligibly. Usually, the idea just vanishes into obscure parts of your unconsciousness mind to never be see again. Imagine, having a stack with your friends to which you can push your ideas to. As soon as you have your idea, you go to your shared stack and add the idea to it. If you see each other the next time, you can pop those ideas to have authentic, meaningful and life changing conversations. Social connections are an important part of our life and we should honor them accordingly.

## Implementation

The talk stack is interacted with via means of a REST endpoints. This idea obviously has imense potential to be further developed, but we focus on a MVP approach.

The talk-stack backend is realized using flask. All the endpoints are defined in `main.py`.

## Installation

1. Clone repository
2. Enter repository
3. `pipenv shell`
4. `pipenv sync`
4. `flask run`
5. profit

## TODO

- [ ] Think about how to write unit-tests for flask (very valuable skill for $$$$)
- [ ] Implement */push_stack/<user>*: Adding a new talk-stack to the stack of <user>. This entails parsing the POST, creating an instance of StackFrame and make it persistant
- [ ] Implement */pop_stack/<user>*: Pop from the stack from the given user; ideally use templating to return a non-super-shitty-looking response
- [ ] Refactor

## Further information

Posts can be easily tested with curl: `curl --verbose -i -d POST  http://127.0.0.1:5000/stack/bigp\?topic\=cool`

The goal is to run talk-stack with a webserver, that offers a simply html-page to interact with the backend.

[Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/#)
[Testing REST with curl](https://www.codepedia.org/ama/how-to-test-a-rest-api-from-command-line-with-curl/)
