from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

pins = (14,15,18)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pins, GPIO.OUT)  # GPIO초기화
GPIO.output(pins, GPIO.LOW)

@app.route('/')
def main():
    state = request.args.get("state")
    return render_template("control_off.html", state=state)

@app.route('/on')
def on():
    GPIO.output(pins, True)
    GPIO.output(pins, GPIO.HIGH)
    state = request.args.get("state")
    return render_template('control_on.html', state='magenta')

@app.route('/off')
def off():
    GPIO.output(pins, GPIO.LOW)
    state = request.args.get("state")
    return render_template('control_off.html', state='off')

@app.route('/red')
def red():
    # GPIO.output(pins,True)
    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.LOW)
    return render_template('control_on.html', state='red')

@app.route('/green')
def green():
    # GPIO.output(pins,True)
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.LOW)
    return render_template('control_on.html', state='green')

@app.route('/blue')
def blue():
# GPIO.output(pins,True)
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.HIGH)
    return render_template('control_on.html', state='blue')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)