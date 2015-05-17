import defaults

from json import loads, dumps

from flask import Flask
app = Flask(__name__)


class Idea(object):
    def __init__(self):
        self.text = ""
        self.timestamp = None

    def __len__(self):
        return len(self.text)


class Box(object):
    def __init__(self, box_limit=32000):
        self.ideas = []
        self.box_limit = box_limit

    def add_idea(self, idea):
        self.ideas.append(idea)

    def ideas_by_timestamp(self):
        return sorted(self.ideas, key:lambda x: x.timestamp)

    def ratio_used(self):
        return float(len(self)) / self.box_limit

    def __len__(self):
        return sum(len(idea) for idea in self.ideas.values())




@app.route("/get_o0o")
def get_o0o():
    try:
        with open('projects', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return dumps(defaults.DEFAULT_TEMPLATE)



if __name__ == "__main__":
    app.run()
