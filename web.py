from flask import Flask
application = Flask(__name__)

@application.route('/hello')
def hello():
    return "Hello World from Python Flask!"

if __name__ == "__main__":
    application.run()

#app.run(host='0.0.0.0', port=5000)
