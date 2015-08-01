#!/usr/bin/python

import Adafruit_PWM_Servo_Driver
import time
from random import randrange

'''LEDDrive.py 
Primary class for generating lighting effects by sending signals to the correct I2C addresses.
Currently only the PCA9685 is supported

Properties:

maxlevel:  			Maximum brightness of the lights - minimum value is 0; maximum value is 4095
stripePeriod: 		Period (seconds) at which colors will move between stripes - inversely related to frequency
					Minimum is 0.1s; Maximum is infinite (fixed mode)
smoothness:			Coarseness of color change as each stripe changes color - minimum is 0; maximum is 255	

TODO:  Create blink
TODO:  Create fade
TODO:  Create switch
TODO:  Create RGB mapping
TODO:  Create attribute setup
'''

class LEDDrive	(object):
    def __init__(self, pwm = None, maxlevel = 2048, stripePeriod = 2):
        self.stripes = []
		self.boards = []
		self.pwmAddresses = { 0x40: True, 0x41: True, 0x42: True, 0x43: True }
		self.maxlevel = maxlevel;
		
		'''Each I2C address supports 16 channels'''
		
		for (j in range(len(pwmAddresses))):
			for (i in range(5)):
				'''self.stripes.append({ 'RED': 0, 'GREEN': 1, 'BLUE': 2})'''
				self.stripes.append({ 'RED': 3*i, 'GREEN': 3*i+1, 'BLUE': 3*i+2})
				
		'''setup pwm blocks'''
        if pwm is None:
            self.pwm = self.setup_pwm()
        else:
            self.pwm = pwm
			
	'''level - sets the maximum brightness of the stripes'''
	@property
	def maxlevel(self):
		return self.__maxlevel
		
	@maxlevel.setter
	def maxlevel(self, val):
		if val < 0:
			self.__maxlevel = 0
			
		if val > 4095:
			self.__maxlevel = 4095
			
    @staticmethod
    def setup_pwm(freq=200):
		pwmInstances = []
		'''TODO: May need to order the list'''
		for (address, valid) in pwmAddresses.items()
			if pwmAddresses[address] == True:
				print "PWM initialized for ", address
				pwmInstance = Adafruit_PWM_Servo_Driver.PWM(address)
				pwmInstance.setPWMFreq(freq)
				pwmInstances.append(pwmInstance)
				
        return pwmInstances

    @staticmethod
    def convert_eight_to_twelve_bit(eight_bit):
        """The PWM chip has 10 bit resolution, so we need to 
            convert regular 8 bit rgb codes
        >>> RGB_Driver.convert_eight_to_ten_bit(0)
        0
        >>> RGB_Driver.convert_eight_to_ten_bit(255)
        4080
        >>> RGB_Driver.convert_eight_to_ten_bit(128)
        2048
        """
        return eight_bit<<4

	'''set the RGB value for a specific block of channels'''
    def set_rgb(self, red_value, green_value, blue_value):
        """The rgb values must be between 0 and 4095"""
        '''print "R: %d, G: %d, B: %d" % (red_value, green_value, blue_value)'''
        self.pwm.setPWM(self.red_pin, 0, red_value)
        self.pwm.setPWM(self.green_pin, 0, green_value)
        self.pwm.setPWM(self.blue_pin, 0, blue_value)

    '''set the RGB value for a specific stripe'''
	'''TODO: Figure out which approach is faster'''
    def set_stripe(self, stripe_num, red_value, green_value, blue_value):
		board, position = divmod(stripe_num, 5)
        self.pwm[board].setPWM(3*position, 0, red_value)
        self.pwm[board].setPWM(3*position+1, 0, green_value)
        self.pwm[board].setPWM(3*position+2, 0, blue_value)		
        '''self.pwm[board].setPWM(self.stripes[position]['RED'], 0, red_value)
        self.pwm[board].setPWM(self.stripes[position]['GREEN'], 0, green_value)
        self.pwm[board].setPWM(self.stripes[position]['BLUE'], 0, blue_value)
        self.pwm.setPWM(self.stripes[stripe_num]['RED'], 0, red_value)
        self.pwm.setPWM(self.stripes[stripe_num]['GREEN'], 0, green_value)
        self.pwm.setPWM(self.stripes[stripe_num]['BLUE'], 0, blue_value)'''
        return
	
	'''Fade gradually shifts colors from an initial element of rgbList to a subsequent element.'''
	def fade(self, chanType, rgbList, startChan, stopChan, step):
		return
	
	'''Blink gradually shifts colors from an initial element of rgbList, to an "off" state, and then to a subsequent element.'''
	def blink(self, chanType, rgbList, startChan, stopChan, step):
		return

	'''Switch immediately changes colors from an initial element of rgbList to a subsequent element.'''
	def switch(self, chanType, rgbList, startChan, stopChan, step):
		return
		
	'''Constructs a mapping between two RGB colors. A map type indicates how the RGB color wheel should be traversed.'''	
	def buildRGBmap():
		return
	
	'''Reads attributes (frequency, max brightness, smoothness) passed by the caller and sets the property values accordingly'''
	def readAttributes():
		return
	
   
 
