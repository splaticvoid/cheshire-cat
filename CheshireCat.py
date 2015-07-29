#!/usr/bin/python


'''CheshireCat.py 
Parent script for executing lighting effects on TAYDCC. 


'''



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
ledArguments = __import__('LEDArguments.py')
	
'''initialize the LED driver class'''	
ledDrive = __import__('LEDDrive.py')


'''initialize the serial reader'''
uiReceiver = __import__('UIReceiver.py')
	

'''initialize the playback modes class'''
modes = __import__('CheshireCatModes.py')


