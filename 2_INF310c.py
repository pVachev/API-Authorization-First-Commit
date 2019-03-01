from flask import Flask

app = Flask(__name__) 

@app.route('/<word>')
def hello_world2(word):
    return 'INF 310c - Final Exam'