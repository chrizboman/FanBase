from os import stat
from flask import Flask, render_template, request, jsonify, send_from_directory
import json, os
import RPi.GPIO as GPIO

app = Flask(__name__)
#app.config["DEBUG"] = True
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

status = None

@app.route('/', methods=['GET'])
def index():
	status = request.args.get('status')
	return render_template('index.html', status=status)
	
	#return jsonify({"message": "Led successfully turned on" + str(status)})

@app.route('/fan/', methods=['GET'])
def toggle():
	status = request.args.get('status')

	if status == 'off':
		print("could do off code") 
		GPIO.output(18, GPIO.HIGH) #this is the first output pin on rpi

	elif status == 'on':
		print("and now some on code")
		GPIO.output(18, GPIO.LOW)

	return jsonify({"message": "Led successfully turned on" + str(status)})



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
