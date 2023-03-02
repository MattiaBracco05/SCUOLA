from typing import *
import utilities

BACKGROUND = 48
FOREGROUND = 38

# FORMATTAZIONE COLORE
RGB24 = 2

# GRAFICA
BOLD = 1
R_BOLD = 22

ITALIC = 3
R_ITALIC = 23

UNDERLINE = 4
R_UNDERLINE = 24

BLINK = 5
R_BLINK = 25

REVERSE = 7
R_REVERSE = 27

HIDDEN = 8
R_HIDDEN = 28

STRIKETHROUGH = 9
R_STRIKETHROUGH = 29

mode_list = [BOLD, R_BOLD, ITALIC, R_ITALIC, HIDDEN, R_HIDDEN, STRIKETHROUGH, R_STRIKETHROUGH, REVERSE, R_REVERSE,
             UNDERLINE, R_UNDERLINE, BLINK, R_BLINK]

RESET = "\x1b[0m"
#-----------------------------------------------------------------------------------------------------------------------------------
class RGB():
	def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
		self.__red: int = None
		self.__blue: int = None
		self.__green: int = None

		self.red = red
		self.blue = blue
		self.green = green

	@property
	def red(self) -> int:
		return self.__red

	@property
	def green(self) -> int:
		return self.__green

	@property
	def blue(self) -> int:
		return self.__blue

	@blue.setter
	def blue(self, value):
		self.__rangeControl(value)

		self.__blue = value

	@green.setter
	def green(self, value):
		self.__rangeControl(value)

		self.__green = value

	@red.setter
	def red(self, value: int):
		self.__rangeControl(value)

		self.__red = value

	def __rangeControl(self, value: int):
		if not 0 <= value <= 255:
			raise ValueError("The range of the value of RGB is 0-255")

		if not isinstance(value, int):
			raise TypeError("Value must be an instance of class int")
#-----------------------------------------------------------------------------------------------------------------------------------
class xterm_text_decorator():
	def __init__(self, rgb: RGB, ground: int, mode: Set[int] = None):
		self.__rgb: RGB = None
		self.__mode: Set[int] = None
		self.__ground: int = None

		self.rgb = rgb
		self.mode = mode
		self.ground = ground

	@property
	def rgb(self) -> RGB:
		return self.__rgb

	@property
	def ground(self) -> int:
		return self.__ground

	@property
	def mode(self) -> Set[int]:
		return self.__mode

	@rgb.setter
	def rgb(self, value: RGB):
		if not isinstance(value, RGB):
			raise TypeError("Except instance of RGB")

		self.__rgb = value

	@ground.setter
	def ground(self, value: int):
		if not isinstance(value, int):
			raise TypeError("Except int value")

		if value != BACKGROUND and value != FOREGROUND:
			raise ValueError("Value not recognized, use BACKGROUND or FOREGROUND constant")

		self.__ground = value

	@mode.setter
	def mode(self, value: Set[int]):
		if value is None:
			self.__mode = set()
			return

		if not utilities.isCollectionOf(value, int):
			raise ValueError("Attribute mode must be a set of instance of int")

		if len(list(filter(lambda x: x not in mode_list, value))) > 0:
			raise ValueError("Some value is not recognized")

		self.__mode = value

	def __add__(self, value: int):
		if value not in mode_list:
			raise ValueError("Value is not recognized")

		self.__mode.add(value)
		return self

	def __sub__(self, value: int):
		if value not in mode_list:
			raise ValueError("Value is not recognized")

		if value not in self.mode:
			raise ValueError("Value not found in mode set")

		self.__mode.remove(value)
		return self

	def __str__(self):
		strmode = [str(x) for x in self.mode]
		strmode.insert(0, "")
		s = ";".join(strmode)
		return f"\x1b[{self.ground};{RGB24};{self.rgb.red};{self.rgb.green};{self.rgb.blue}{s}m"
