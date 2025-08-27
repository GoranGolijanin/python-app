from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details', methods=['GET'])
def details():
	return jsonify(
		{ 
			# "time": datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d"),
			"time": datetime.datetime.now().strftime("%Y-%m-%d"),
			"hostname": socket.gethostname(),
			"message": "You are doing great!"
		}), 200

@app.route('/api/v1/health', methods=['GET'])
def health():
	return jsonify({ "status": "up" }), 200

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)