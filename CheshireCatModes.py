#!/usr/bin/python


'''CheshireCatModes.py 
Class defining a collection of playback modes.  Each playback mode corresponds to a static method. 
Class accepts an instance of LEDDrive on construction.

There are a maximum of 16 modes currently.

'''
from enum import Enum

class CheshireCatMode:
	Default,
	Disney,
	GloriousJuche,
	JoxerMode,
	EnrageMode,
	RandomStripes,
	AmericaFuckYeah,
	NyanCatMode,
	CircusMode,
	WhiteRabbitMode
	SeizureMode,
	GrandMalSeizure = range(12)
	
	
class CheshireCatActions(object):
	
	
	@staticmethod
	def SetMode(mode):
		switcher = {
			0: SetDefault,
			1: SetDisney,
			2: SetGloriousJuche,
			3: JoxerMode,
			4: EnrageMode,
			5: RandomStripes,
			6: AmericaFuckYeah,
			7: NyanCatMode,
			8: CircusMode,
			9: WhiteRabbitMode,
			10: SeizureMode,
			11: GrandMalSeizure
		}
		
		func = switcher.get(mode, lambda: "nothing")
		
		return func()
			
		
	def SetDefault():
		print "Default mode operations..."
		return
		
	def	SetDisney():
		print "Subset of basic stripe - purple and pink..."
		return
		
	def	SetGloriousJuche():
		print "Red and yellow"
		return
		
	def	JoxerMode():
		print "Cascading shades of yellow and orange"
		return
		
	def	EnrageMode():
		print "All stripes turn red"
		return
		
	def	RandomStripes():
		print "Two stripe colors are chosen randomly exactly once"
		return
		
	def	AmericaFuckYeah():
		print "Stripes become red, white, and blue"
		return
	
	def	NyanCatMode():
		print "Rainbow coloring"
		return
	
	def	CircusMode():
		print "Subset of basic stripe - red and white"
		return
	
	def	WhiteRabbitMode():
		print "All stripes turn white"
		return
	
	def	SeizureMode():
		print "Random colors cascade through each stripe"
		return
		
	def	GrandMalSeizure
		print "Maximal randomness, random interval changes, and full brightness"
		return
	
		