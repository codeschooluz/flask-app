from flask import Flask

app = Flask(__name__)

@app.route('/')
def github():
    return 'Hello, Github!'


if __name__ == '__main__':
    app.run()