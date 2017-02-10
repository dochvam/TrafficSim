from math import *
from graphics import *


class StopLight (object):
	

	def __init__ (self, street1, street2, time1, time2, win):
		self.street1 = street1
		self.street2 = street2
		self.street1.lightList.append(self)
		self.street2.lightList.append(self)
		self.street1.itemsList.append(self)
		self.street2.itemsList.append(self)

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

		self.state = []

		self.state.append("red")
		self.state.append("green")
		self.updateColor()


	def step (self):
		self.t += 1
		if self.t < self.time1 - self.yellowConstant:
			self.state[0] = "red"
			self.state[1] = "green"
		elif self.t < self.time1:
			self.state[0] = "red"
			self.state[1] = "yellow"
		elif self.t == self.time1:
			self.state[0] = "red"
			self.state[1] = "red"
		elif self.t < self.length - self.yellowConstant:
			self.state[0] = "green"
			self.state[1] = "red"
		elif self.t < self.length:
			self.state[0] = "yellow"
			self.state[1] = "red"
		else:
			self.state[0] = "red"
			self.state[1] = "red"
			self.t = -1

		self.updateColor()

	def updateColor (self):
		self.graphic[0].setFill(self.state[0])
		self.graphic[1].setFill(self.state[0])
		self.graphic[2].setFill(self.state[1])
		self.graphic[3].setFill(self.state[1])

		for i in self.graphic:
			i.undraw()
			i.draw(self.win)




