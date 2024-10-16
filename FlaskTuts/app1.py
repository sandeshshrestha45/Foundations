from flask import Flask

#WSGI application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Hello! Flask.."

@app.route('/message')
def message():
    return "This is a Flask app"



if __name__=='__main__':
    app.run(debug=True)