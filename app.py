from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)
#app.config["DEBUG"] = True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
status = 'astatus'

@app.route('/', methods=['GET'])
def index():
	status = request.args.get('status')
	return render_template('index.html', status=status)
	
	#return jsonify({"message": "Led successfully turned on" + str(status)})

@app.route('/fan', methods=['GET'])
def toggle():
	status = request.args.get('status')
	return jsonify({"message": "Led successfully turned on" + str(status)})


