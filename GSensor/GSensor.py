import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

class GSensor:
	"""
	Reference: https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi?view=all
	"""
	def __init__(self):
		# create the spi bus
		self.spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
		# create the cs (chip select)
		self.cs = digitalio.DigitalInOut(board.D22)
		# create the mcp object
		self.mcp = MCP.MCP3008(self.spi, self.cs)
		# create an analog input channel on pin 0
		self.chan0 = AnalogIn(self.mcp, MCP.P0)
		# print('Raw ADC Value: ', self.chan0.value)
		# print('ADC Voltage: ' + str(self.chan0.voltage) + 'V')
		self.last_read = 0
		self.tolerance = 250

	def remap_range(self, value, left_min, left_max, right_min, right_max):
		# this remaps a value from original (left) range to new (right) range
		# Figure out how 'wide' each range is
		left_span = left_max - left_min
		right_span = right_max - right_min

		# Convert the left range into a 0-1 range (int)
		valueScaled = int(value - left_min) / int(left_span)

		# Convert the 0-1 range into a value in the right range.
		return int(right_min + (valueScaled * right_span))

	def getData(self):
		"""
		Get current value
		"""
		# we'll assume that the pot didn't move
		trim_pot_changed = False
		# read the analog pin
		trim_pot = self.chan0.value
		# how much has it changed since the last read?
		pot_adjust = abs(trim_pot - self.last_read)

		if pot_adjust > self.tolerance:
			trim_pot_changed = True

		if trim_pot_changed:
			# convert 16bit adc0 (0-65535) trim pot read into 0-100 volume level
			set_volume = self.remap_range(trim_pot, 0, 65535, 0, 100)
			# set OS volume playback volume
			# print('Value = {volume}%' .format(volume = set_volume))
			set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' \
			.format(volume = set_volume)
			os.system(set_vol_cmd)
			# save the potentiometer reading for the next loop
			self.last_read = trim_pot
			return set_volume
		else : return self.remap_range(self.last_read, 0, 65535, 0, 100)

	def stable_or_sway(self):
		trim_pot_changed = False
		trim_pot = self.chan0.value
		pot_adjust = abs(trim_pot - self.last_read)
		if pot_adjust > self.tolerance : trim_pot_changed = True
		if trim_pot_changed:
			set_volume = self.remap_range(trim_pot, 0, 65535, 0, 100)
			set_vol_cmd = 'sudo amixer cset numid=1 -- {volume}% > /dev/null' \
			.format(volume = set_volume)
			os.system(set_vol_cmd)
			self.last_read = trim_pot
			if set_volume > 50 : return "It's swaying！"
			else : return "It's stable～"
		elif self.remap_range(self.last_read, 0, 65535, 0, 100) > 50 : return "It's swaying！"
		else : return "It's stable～"
