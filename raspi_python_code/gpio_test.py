import RPi.GPIO as GPIO
import time,threading

GPIO.setmode(GPIO.BCM)
PORT=4

GPIO.setup(PORT,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def printPort():
	value=GPIO.input(PORT)
	print ("reading port "+str(PORT)+": " + str(value))
	threading.Timer(5, printPort).start()

printPort()
