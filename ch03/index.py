from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import db_model

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)

GREEN = 8
RED = 10
YELLOW = 12

GPIO.setup(GREEN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(YELLOW, GPIO.OUT, initial=GPIO.LOW)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/greenOn")
def led_green():
    try:
        GPIO.output(GREEN, GPIO.HIGH)
        return render_template("index.html")
    except:
        return "fail"

@app.route("/redOn")
def led_red():
    try:
        GPIO.output(RED, GPIO.HIGH)
        return render_template("index.html")
    except:
        return "fail"


@app.route("/yellowOn")
def led_yellow():
    try:
        GPIO.output(YELLOW, GPIO.HIGH)
        return render_template("index.html")
    except:
        return "fail"

@app.route("/greenOff")
def led_greenOff():
    try:
        GPIO.output(GREEN, GPIO.LOW)
        return render_template("index.html")
    except:
        return "fail"

@app.route("/redOff")
def led_redOff():
    try:
        GPIO.output(RED, GPIO.LOW)
        return render_template("index.html")
    except:
        return "fail"

@app.route("/yellowOff")
def led_yellowOff():
    try:
        GPIO.output(YELLOW, GPIO.LOW)
        return render_template("index.html")
    except:
        return "fail"

@app.route("/on")
def led_on():
    try:
        GPIO.output(GREEN, GPIO.HIGH)
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(YELLOW, GPIO.HIGH)
        return render_template("index.html")
    except:
        return "fail"

@app.route("/off")
def led_off():
    try:
        GPIO.output(GREEN, GPIO.LOW)
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.LOW)
        return render_template("index.html")
    except:
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
