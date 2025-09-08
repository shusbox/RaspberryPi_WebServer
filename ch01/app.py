from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello flask world!'

@app.route('/hi')
def hi():
    return 'hi'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
