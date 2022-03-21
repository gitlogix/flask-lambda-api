
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World to me!"

@app.route('/health')
def health_check():
    return "API health is fine!"
if __name__ == '__main__':
 app.run()