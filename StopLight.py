from math import *
from graphics import *


class StopLight (object):
	

	def __init__ (self, street1, street2, time1, time2, win):
		self.street1 = street1
		self.street2 = street2
		self.x, self.y, self.locOnStreet1, self.locOnStreet2 = self.street1.getIntersect(self.street2)
		self.graphic = []
		self.win = win
		#how long is a yellow light?
		self.yellowConstant = 3

		self.graphic.append(Circle(Point(self.x-4, self.y), 3))
		self.graphic.append(Circle(Point(self.x+4, self.y), 3))
		self.graphic.append(Circle(Point(self.x, self.y-4), 3))
		self.graphic.append(Circle(Point(self.x, self.y+4), 3))

		# timeN = how long streetN's red light is
		self.time1 = int(time1)
		self.time2 = int(time2)
		# Ratio = (length of red for street1)/(length of red for street2)
		self.ratio = time1/time2
		# length = how long it takes to complete a full cycle
		self.length = time1 + time2
		# t = how far into the cycle we are
		self.t = 0

		self.state1 = "red"
		self.state2 = "green"
		self.updateColor()


	def step (self):
		self.t += 1
		if self.t < self.time1 - self.yellowConstant:
			self.state1 = "red"
			self.state2 = "green"
		elif self.t < self.time1:
			self.state1 = "red"
			self.state2 = "yellow"
		elif self.t == self.time1:
			self.state1 = "red"
			self.state2 = "red"
		elif self.t < self.length - self.yellowConstant:
			self.state1 = "green"
			self.state2 = "red"
		elif self.t < self.length:
			self.state1 = "yellow"
			self.state2 = "red"
		else:
			self.state1 = "red"
			self.state2 = "red"
			self.t = -1

		self.updateColor()

	def updateColor (self):
		self.graphic[0].setFill(self.state1)
		self.graphic[1].setFill(self.state1)
		self.graphic[2].setFill(self.state2)
		self.graphic[3].setFill(self.state2)

		for i in self.graphic:
			i.undraw()
			i.draw(self.win)




