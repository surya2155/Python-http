import flask
from flask import request, jsonify
from flask import Flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# some test data for the response.
hello_world = 'hello World'

@app.route('/', methods=['GET'])
def home():
    return '''<h1>This is the home page</h1>
<p>Add /hello for the desired response.</p>'''

# A route to return the desired response.
@app.route('/hello', methods=['GET'])
def api_all():
    return jsonify(hello_world)

if __name__ == '__main__':
    app.run()
