from flask import Flask, render_template, jsonify, request, make_response

app = Flask(__name__)

@app.route('/button')
def button():
	return render_template('button.html')

@app.route('/basic')
def basic():
	return render_template('basic.html')

@app.route('/api/button', methods=['POST'])
def api_button():
	try:
		data = request.json
		is_enabled = data['enabled']
	except KeyError:
		return make_response(jsonify({"status": "bad request"}), 400)

	if is_enabled:
		return jsonify({"status": "success", "state": "enabled"})
	else:
		return jsonify({"status": "success", "state": "disabled"})

# Default endpoints

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/health-check')
def health_check():
	return "ok"

if __name__ == '__main__':
	app.run(host='0.0.0.0')