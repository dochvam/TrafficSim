from math import *
from graphics import *

class Street(object):
	def __init__ (self, beginning, end, speedLimit, win):
                
                #orientation of the street
		self.beginning = beginning 	# a Point object
		self.end = end 				# another Point object
		self.win = win
		self.hash = hash(self.beginning) + hash(self.end)
		self.lightList = []
		self.end = end 			# another Point object
		self.length = sqrt((beginning.getX() - end.getX())**2 + (beginning.getY() - end.getY())**2)

		self.m = 0 #lol what is this
		#self.direc is the direction that the street goes in radians
		if (end.getX() == beginning.getX()):
			self.m = 100000000
			if beginning.getY() > end.getY():

				self.direc = pi/2
			else:
				self.direc = 3*pi/2
		else:
			direc = atan((end.getY() - beginning.getY())/(end.getX() - beginning.getX()))
			while direc < 0.0:
				direc += pi * 2
			self.direc = direc

		if self.m != 100000000:
			self.m = (end.getY() - beginning.getY())/(end.getX() - beginning.getX())
		self.b = end.getY() - (self.m * end.getX())

                #cars and related
		self.carList = []
                self.speedLimit = speedLimit
                self.light = "green"

		self.itemsList = []
                #graphics
                self.win = win          
		self.line = Line(self.beginning, self.end) #eventually this should be adapted for multiple lanes? abstract class?
		self.line.setWidth(3)
		self.line.draw(self.win)

	def __eq__ (self, other):
		return self.hash == other.hash

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
		
	def addCar(self, car):
		if type(car) is Car:
			carList.add(car)
			self.sortList()

	def getIntersect(self, other):
		x = (other.b - self.b)/(self.m - other.m)
		y = (self.m * x) + self.b

		locOnStreet1 = sqrt((x-self.beginning.getX())**2 + (y-self.beginning.getY())**2)
		locOnStreet2 = sqrt((x-other.beginning.getX())**2 + (y-other.beginning.getY())**2)

		return x, y, locOnStreet1, locOnStreet2

        def addCar(self, car):
                if type(car) is Car:
                        carList.add(car)
                        self.sortList()

        def setLight(self, light):
                if type(light) is str:
                        self.light = light

        def moveCars(self):
                if self.light is "green":
                        for car in carList:
                                car.move()
                elif self.light is "yellow":
                        for car in carList:
                                car.move() #this should be fixed
                elif self.light is "red":
                        continue #this should also be fixed. I propose getting cars to stop before the "Intersection" but we need to make that first

