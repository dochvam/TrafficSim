from graphics import *
from Car import *
from Street import *
from StopLight import *

def step(carArray, streetArray, stopArray):
	for street in streetArray:
		street.sortList()
	for car in carArray:
		car.move()
	for stoplight in stopArray:
		stoplight.step()

win = GraphWin('test',500,500,False)

streets = []
streets.append(Street(Point(50, 250), Point(450, 250), 10, win))
streets.append(Street(Point(250, 50), Point(250, 450), 10, win))

stoplights = []
stoplights.append(StopLight(streets[0], streets[1], 10, 10, win))

cars = []



for i in range(100):
	step(cars, streets, stoplights)
	win.update()
	time.sleep(0.5)

win.getMouse()
win.close()
