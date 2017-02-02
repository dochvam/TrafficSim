from math import *
from graphics import *

class Car(object):
	def __init__(self, locOnStreet, speed, win, street, color="black"):
		self.dim = 10
		self.locOnStreet = locOnStreet
		self.speed = speed  # units per timestep
		self.__win = win
		self.street = street
		self.direc = street.direc  # given in radians with direc=0 pointing East
		self.visibility = self.dim*6
		self.color = color

		self.street.carList.append(self)
		self.listLoc = len(self.street.carList) - 1

		self.__x, self.__y = street.getCarPos(self)

		self.block = Rectangle(Point((self.__x - self.dim), (self.__y - self.dim)),Point((self.__x + self.dim),(self.__y + self.dim)))

		self.block.setFill(self.color)
		self.block.draw(win)

	def __gt__ (self, other):
		return other.__lt__(self)

	def __lt__ (self, other):
		return self.locOnStreet > other.locOnStreet

	def __str__(self):
		return "Speed: {0} \n Direction: {1} \n Location: ({2}, {3})".format(self.speed, self.direc, self.__x, self.__y)

	def move(self):
		if self.listLoc != 0:
			dist_from_next_car = self.street.carList[self.listLoc-1].locOnStreet - self.locOnStreet

			diff_in_speed = self.street.carList[self.listLoc-1].speed - self.speed

			if dist_from_next_car < self.visibility and diff_in_speed < 0:
				self.accel(-1*(diff_in_speed//1 + 2))
			elif self.isMoving():
                                self.accel(2)




		if self.locOnStreet >= (self.street.length - self.visibility):
			self.accel( -((self.speed // 2) + 1) )
			print("decel")

		self.__x += (self.speed * cos(self.direc))
		self.__y += (self.speed * sin(self.direc))
		self.locOnStreet += self.speed
		#print(self.speed, self.street.speedLimit)
		self.redraw()

	def accel(self, accel_amt):
                #print(self.street.speedLimit)
                if self.speed>self.street.speedLimit:
                        print("ooooooh dat boi gon getta ticket")
                x = self.speed + accel_amt
                if x > self.street.speedLimit:
                        self.speed = self.street.speedLimit
                else:
                        self.speed = x
	def turn(self, rad):
		#pos turns counterclockwise
		self.direc += rad

	def delete(self):
		self.__end = True
	def is_ended(self):
		return self.__end
	def getLoc(self):
		return self.__x+self.dim,self.__y+self.dim
	def isMoving(self):
		if self.speed == 0:
			return False
		else:
			return True
	def redraw(self):
		self.block.undraw()
		self.block = Rectangle(Point((self.__x - self.dim), (self.__y - self.dim)),Point((self.__x + self.dim),(self.__y + self.dim)))
		self.block.setFill(self.color)
		self.block.draw(self.__win)
	def undraw(self):
		self.block.undraw
