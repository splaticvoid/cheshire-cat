#!/usr/bin/python


'''Unit tests for LEDDrive.py'''

import Adafruit_PWM_Servo_Driver
import time
from random import randrange

class LEDDriveTests	(object):
    def __init__(self, pwm = None):
		ledDrive = __import__('LEDDrive.py')
		defaultTestStripe = 0
		
	@staticmethod
	def TestAllI2CChannels():
		return -1
		
	@staticmethod
	def TestRGBForAllStripes():
		driver.set_stripe(defaultTestStripe,0,0,0)
		'''driver.set_stripe(1,0,0,0)'''
		time.sleep(5)	
		driver.set_stripe(defaultTestStripe,level,0,0)
		time.sleep(1)
		driver.set_stripe(defaultTestStripe,0,level,0)
		time.sleep(1)
		driver.set_stripe(defaultTestStripe,0,0,level)
		time.sleep(1)
		driver.set_stripe(defaultTestStripe,level,level,0)
        time.sleep(1)
		driver.set_stripe(defaultTestStripe,level,0,level)
		time.sleep(1)
		driver.set_stripe(defaultTestStripe,0,level,level)
		time.sleep(1)
		driver.set_stripe(defaultTestStripe,level,level,level)
		time.sleep(1)
        driver.set_stripe(defaultTestStripe,0,0,0)
		return 0
				
	@staticmethod
	def TestSingleColorFadeThroughEveryStripe():
		return -1

	@staticmethod
	def TestAlternatingColorsSwitch():
		return -1
		
	@staticmethod
	def TestFadeOperation():
		return -1
		
	@staticmethod
	def TestBlinkOperation():
		return -1		

	@staticmethod
	def TestRGBMap():
		return -1
		
	@staticmethod
	def TestReadAttributes():
		return -1
		
	@staticmethod
	def TestPlaybackModes():
		return -1
		
	@staticmethod
	def TestUIReceiver():
		return -1
		
if __name__ == '__main__':
    tests = LEDDriveTests()

	'''setup'''
    startTime = time.time()
    currentTime = 0
	
	'''perform tests'''
	if (tests.TestRGBForEachStripe() < 0): raise AssertionError('TestRGBForEachStripe failed.')
	     	
	'''teardown'''
	currentTime = time.time() - startTime
	print currentTime, " seconds elasped"
	
 
	
