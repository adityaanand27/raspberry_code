import RPi.GPIO as GPIO
import distance as d
import Camera as C
import time
import threading
import  concurrent.futures 
import Relay as r
import firebase as fi
global x, y
y = {
	'Counter' : 0,
	'z' : True,
	'w' : False
}
x = False
w = False
TRIG1 = 18
ECHO1= 17
TRIG2 = 23
ECHO2 = 22
d.setup(TRIG1, ECHO1)
d.setup(TRIG2, ECHO2)


def sensor_1():
	
	while True:
		value = d.Distance(TRIG1, ECHO1)
		while value:
			y['z'] = False
			value = d.Distance(TRIG1, ECHO1)
			if(not value):
				y['z'] = True
				if y['z']:
					x = True
					y['Counter'] += 1
					fi.data_send(y['Counter'])
					print(y['Counter'])
					try:
						r.led_on()
						C.Record()
					except:
						print()
					
					 
			

def sensor_2():
	while True:
		value = d.Distance(TRIG2, ECHO2)
		while value:
			y['w'] = False
			value = d.Distance(TRIG2, ECHO2)
			if(not value):
				y['w'] = True
				if y['w'] and y['Counter'] > 0:
					y['Counter'] -= 1
					fi.data_send(y['Counter'])
					print(y['Counter'])
					if y['Counter'] == 0:
						x=False
						try:
							C.stop_Recording()
							r.led_off()
							print('Hello')
						except:
							C.stop_Recording()
							r.led_off()
							print('Exception occured')
				
		
		
t1 = threading.Thread(target = sensor_1)

t2 = threading.Thread(target = sensor_2)

t1.start()
t2.start()

	





