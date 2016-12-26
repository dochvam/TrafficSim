from math import *
from graphics import *

class Street(object):
	def __init__ (self, beginning, end, speedLimit):
		self.__beginning = beginning # a Point object
		self.__end = end # another Point object
		direc = atan2(end.getY() - beginning.getY())/(end.getX() - beginning.getX())
		while direc < 0.0:
			direc += pi * 2
		self.__direc = direc

		self.__speedLimit = speedLimit

		self.__m = (end.getY() - beginning.getY())/(end.getX() - beginning.getX())
		self.__b = end.getY() - (self.__m * end.getX())

		self.carList = []

		self.line = Line(self.__beginning, self.__end)

	def getCarPos(self, car):
		theta = arctan(self.__m)

		carX = car.locOnStreet * cos(theta) + self.beginning.getX
		carY = car.locOnStreet * sin(theta) + self.beginning.getY

		return carX, carY

	def removeFirstCar(self):
		temp = self.carList[0]
		self.carList = self.carList[1:]
		return temp

	def isCarOn (self, car):
		x,y = car.getLoc()

		if (x < self.__end.getX()):
			if (x < self.__beginning.getX()):
				return false
		if (x > self.__end.getX()):
			if (x > self.__beginning.getX()):
				return false		

		return (y - ((self.__m * x) + b)) < 0.1