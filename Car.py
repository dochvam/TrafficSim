from math import *
from graphics import *

class Car(object):
	def __init__(self, x, y, speed, direc, win):
		self.__x = x
		self.__y = y
		self.__speed = speed  # units per timestep
		self.__direc = direc  # given in radians with direc=0 pointing East
		self.__win = win
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
