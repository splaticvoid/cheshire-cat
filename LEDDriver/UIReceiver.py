#!/usr/bin/python


'''UIReceiver.py 
Class for receiving and formatting GPIO input on the Raspberry Pi 2

'''
import time, serial
import numpy as np

class UIReceiver(object):
	def __init__(self):
		self.gpioValues = []
		self.defaultSerialPort = '/dev/ttyAMA0'
		self.serialRate = 115200
		self.timeout = 0.1
		self.maxBytes = 200
		return
		
	'''reads the input from the RX pin'''
	@staticmethod
	def getInput():
		serialport = serial.Serial(self.defaultSerialPort, self.serialRate, self.timeout)		
		readResult = serialport.read(maxBytes)
		print "Read result from serial port: ", readResult
		return readResult
			
	'''returns a dictionary structure containing the elements returned in the serial buffer'''
	@staticmethod
	def formatResult(message):
		ccDict = {}
		ccInput = message
		print "serial string: ", ccInput
		ccKeyValues = ccInput.strip().split(',')
		
		for(i in range(len(ccKeyValues))):
			keyValuePair = ccKeyValues.split(':'))
			print "key: ", keyValuePair[0]
			print "value: ", keyValuePair[1]
			ccDict[keyValuePair[0].strip()] = keyValuePair[1].strip()
		return ccDict	

if __name__ == '__main__':
    receiver = UIReceiver()
	
	result = UIReceiver.getInput()	
	print "serial: ", result

	dictResult = UIReceiver.formatResult(message)
	for keys,values in dictResult.items():
		print(keys)
		print(values)