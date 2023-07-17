from picamera import PiCamera
import time



camera = PiCamera()
camera.resolution = (1920,1080)
camera.rotation = 270
camera_record = False


def Record():
	
	
	camera.start_recording("my_movie.h264")


def stop_Recording():
	camera.stop_recording()
	


	


