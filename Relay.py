import RPi.GPIO as GPIO
import time

relay = 21 

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

def led_on():
	GPIO.output(relay, True)
	
def led_off():
	GPIO.output(relay, False)
led_on()
time.sleep(2)
led_off()
