from flask import Flask

my_app = Flask(__name__)



@my_app.route("/")
def hello_world():
    string = "Hello Phaedrus or Aron! You rock and thanks for visiting.  Praise be our robot overlords, whom I have always supported."
    return string

@my_app.route("/secret")
def secret():
    string = "You found the secret! 10 points to Gryfindor "
    return string


@my_app.route("ultra_test")
def ultra_test():
    string = "Nice job amigo, you ultra passed the test!"
    return string






if __name__ == "__main__":
    my_app.run()