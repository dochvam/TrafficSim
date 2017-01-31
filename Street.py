from math import *
from graphics import *

class Street(object):
	def __init__ (self, beginning, end, speedLimit, win):
		self.beginning = beginning 	# a Point object
		self.end = end 				# another Point object
		self.win = win
		self.length = sqrt((beginning.getX() - end.getX())**2 + (beginning.getY() - end.getY())**2)
		
		direc = atan((end.getY() - beginning.getY())/(end.getX() - beginning.getX()))
		while direc < 0.0:
			direc += pi * 2
		self.direc = direc

		self.speedLimit = speedLimit

		self.m = (end.getY() - beginning.getY())/(end.getX() - beginning.getX())
		self.b = end.getY() - (self.m * end.getX())

		self.carList = []

		self.line = Line(self.beginning, self.end)
		self.line.setWidth(3)
		self.line.draw(self.win)

	def getCarPos(self, car):
		theta = self.direc

		carX = car.locOnStreet * cos(theta) + self.beginning.getX()
		carY = car.locOnStreet * sin(theta) + self.beginning.getY()

		return carX, carY

	def removeFirstCar(self):
		temp = self.carList[0]
		self.carList = self.carList[1:]
		return temp

	def isCarOn (self, car):
		x,y = car.getLoc()

		if (x < self.end.getX()):
			if (x < self.beginning.getX()):
				return false
		if (x > self.end.getX()):
			if (x > self.beginning.getX()):
				return false		

		return (y - ((self.m * x) + b)) < 0.1

	def sortList(self):
		self.carList = sorted(self.carList)

	def printCarList(self):
		rtn = ""
		for car in self.carList:
			rtn += str(car.locOnStreet) + " "
		return rtn