from math import *
from graphics import *

class Car(object):
	def __init__(self, locOnStreet, speed, direc, win, strt):
		self.locOnStreet = locOnStreet
		self.speed = speed  # units per timestep
		self.direc = direc  # given in radians with direc=0 pointing East
		self.__win = win
		self.strt = strt

		self.__x, self.__y = strt.getCarLoc()
		self.__block=Rectangle(Point((x-0.5),(y-0.5)),Point((x+0.5),(y+0.5)))

	def __str__(self):
		return "Speed: {0} \n Direction: {1} \n Location: ({2}, {3})".format(self.__speed, self.__direc, self.__x, self.__y)

	def move(self):
		self.__x = self.__x + (self.__speed * cos(self.__direc))
		self.__y = self.__y + (self.__speed * sin(self.__direc))
		self.redraw()

	def accel(self, accel_amt):
		self.__speed += accel_amt

	def turn(self, rad):
		#pos turns counterclockwise
		self.__direc += rad

	def delete(self):
		self.__end = True
	def is_ended(self):
		return self.__end
	def getLoc(self):
		return self.__x,self.__y

	def redraw(self):
		self.__block.undraw()
		self.__block.draw(self.__win)
	def undraw(self):
		self.__block.undraw()
