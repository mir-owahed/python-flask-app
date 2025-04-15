from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '1st code on Python Flask!'


@app.route('/hello')
def hello():
    return 'Hello World!'
    
    
@app.route('/ping')
def ping():
    return 'PONG!'
    
    
app.run(host='0.0.0.0', port=8181)
