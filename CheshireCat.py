#!/usr/bin/python

'''CheshireCat.py 
Parent script for executing lighting effects on TAYDCC. 


'''
import argparse
sys.path.append(os.path.abspath("/cheshire-cat-master/LEDDriver"))
from CheshireCatModes import CheshireCatMode
from CheshireCatModes import CheshireCatActions
import LEDDriver 
import UIReceiver 




def setup():

	return


	
def loop():
	'''read the serial data - note, this should not happen very often relative to the frequency of light-switching operations'''
	
	
	'''have the attributes changed?'''
	
	'''if so, modify the attributes of LEDDriver'''

	'''has the mode changed?'''
	
	'''if so, switch modes to execute'''
	
	'''execute sequence for a predefined number of iterations'''
	
	'''re-check the serial input after the number of iterations is maxed out'''
	
	return
	
'''Read serial arguments from the receiver'''
def importArguments():
	parser = argparse.ArgumentParser(description='Script implementation for driving the TAYDCC LED system.')
	parser.add_argument('-f', help='Selects rate at which colors shift from one stripe to the next.  Default is 0.5 seconds.', dest='frequency', action='store', default=0.5, type=float)
	parser.add_argument('-b', help='Selects maximum brightness of LEDs.  Max is 4095.', dest='max_brightness', action='store', default=2048, type=int)
	parser.add_argument('-c', help='Selects coarseness of color changes.  Max is 255.', dest='smoothness', action='store', default=128, type=int)
	parser.add_argument('-m', help='Selects a preset mode.  Overrides -s, -r', dest='mode', action='store', default=0, type=int)
	parser.add_argument('-r', help='Sets a random color scheme', dest='random', action='store_true', default=False)
	parser.add_argument('-x', help='Fixes the chosen color scheme (no playback)', dest='fixed', action='store_true', default=False)
	parser.add_argument('-s', help='Specifies a list of stripe colors', dest='stripes', action='append', default=[])
	results = parser.parse_args()

	print 'frequency: ', results.frequency
	print 'max brightness: ', results.max_brightness
	print 'smoothness: ', results.smoothness
	print 'mode: ', results.mode
	print 'random: ', results.random
	print 'fixed: ', results.fixed
	print 'stripes: ', results.stripes
	return results

'''ledArguments = __import__('LEDArguments.py')'''


	
'''initialize the LED driver class'''	
'''ledDrive = __import__('LEDDrive.py')'''


'''initialize the serial reader'''
'''uiReceiver = __import__('UIReceiver.py')'''
	

'''initialize the playback modes class'''
'''modes = __import__('CheshireCatModes.py')'''

args = importArguments()
setup()
loop()

