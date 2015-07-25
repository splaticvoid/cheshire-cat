#!/usr/bin/python


'''TODO:  Create class for single LED channel access
TODO:  Create collection for RGB pins'''

import Adafruit_PWM_Servo_Driver
import time
from random import randrange

class TAYDCCDrive(object):
    def __init__(self, pwm = None):
        self.stripes = []
	self.stripes.append({ 'RED': 0, 'GREEN': 1, 'BLUE': 2})
	'''self.stripes.append({ 'RED': 16, 'GREEN': 17, 'BLUE': 18})'''

        if pwm is None:
            self.pwm = self.setup_pwm()
        else:
            self.pwm = pwm

    @staticmethod
    def setup_pwm(freq=200):
        pwm = Adafruit_PWM_Servo_Driver.PWM(0x40)
        "PWM initialized...."
        pwm.setPWMFreq(freq)
        return pwm

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

    def set_rgb(self, red_value, green_value, blue_value):
        """The rgb values must be between 0 and 4095"""
        '''print "R: %d, G: %d, B: %d" % (red_value, green_value, blue_value)'''
        self.pwm.setPWM(self.red_pin, 0, red_value)
        self.pwm.setPWM(self.green_pin, 0, green_value)
        self.pwm.setPWM(self.blue_pin, 0, blue_value)

    def set_stripe(self, stripe_num, red_value, green_value, blue_value):
        self.pwm.setPWM(self.stripes[stripe_num]['RED'], 0, red_value)
        self.pwm.setPWM(self.stripes[stripe_num]['GREEN'], 0, green_value)
        self.pwm.setPWM(self.stripes[stripe_num]['BLUE'], 0, blue_value)
        return

if __name__ == '__main__':
    driver = TAYDCCDrive()

    print "TAYDCC LED drive initialized..."
    print "BATTERY TEST"
    speed = 12

    startTime = time.time()
    currentTime = 0
    level = 4095

    driver.set_stripe(0,0,0,0)
    '''driver.set_stripe(1,0,0,0)'''
    time.sleep(5)
    while (currentTime < 3600):

	driver.set_stripe(0,level,0,0)
	time.sleep(1)
	driver.set_stripe(0,0,level,0)
	time.sleep(1)
	driver.set_stripe(0,0,0,level)
	time.sleep(1)
	driver.set_stripe(0,level,level,0)
        time.sleep(1)
	driver.set_stripe(0,level,0,level)
	time.sleep(1)
	driver.set_stripe(0,0,level,level)
	time.sleep(1)
	driver.set_stripe(0,level,level,level)
	time.sleep(1)
        driver.set_stripe(0,0,0,0)
	time.sleep(1)
        currentTime = time.time() - startTime
        print currentTime, " seconds elasped"
         	
   
 
