import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

for i in range(1000):
    m = GPIO.input(26)
    GPIO.output(25, m)
    time.sleep(0.5)