from flask import Flask, request
import json

app = Flask(__name__)
 
@app.route('/', methods = ['GET','POST'])
def post():
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'JSON posted'
 

if __name__ == '__main__':
	app.run(host='192.168.2.7',debug=True)