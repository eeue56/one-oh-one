import defaults

from json import loads, dumps

from flask import Flask
app = Flask(__name__)


@app.route("/get_o0o")
def get_o0o():
    try:
        with open('projects', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return dumps(defaults.DEFAULT_TEMPLATE)



if __name__ == "__main__":
    app.run()
