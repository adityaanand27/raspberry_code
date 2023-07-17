import time
import RPi.GPIO as GPIO
global pulse_duration1
global pulse_start1
Pass = False

def setup(TRIG,ECHO):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	
def check_dis(dist):
    if(dist <= 9):
        return True
    else:
        return False


def Distance(TRIG, ECHO):
    
    GPIO.output(TRIG,False)
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start1=time.time()
    
    while GPIO.input(ECHO)==1:
        pulse_end1=time.time()
    
    pulse_duration1=pulse_end1-pulse_start1
    
    distance=pulse_duration1*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    
    
    Pass = check_dis(distance)
    return Pass
