# flask 웹 서버
from flask import Flask

app = Flask(__name__) # main이 들어있따

@app.route('/hello') #https://localhost:5000/Home/Index
def index():
    return 'hello, Flask'

if __name__=='__main__':
    app.run(host='localhost')