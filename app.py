
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "API health is fine!"

@app.route('/api-health')
@app.route('/health')
def health_check():
    return "API health is fine!"
if __name__ == '__main__':
 app.run()
