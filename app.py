from flask import Flask, jsonify 
from calculate_distance import calculate_distance

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	return jsonify({'message' : 'Hello'} )

if __name__ == '__main__': 
	app.run(debug=True)


