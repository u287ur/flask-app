from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask on Docker Environment (v2.0)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)