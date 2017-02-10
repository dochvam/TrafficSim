from graphics import *
from Car import *
from Street import *
from StopLight import *

def step(carArray, streetArray, stopArray):
	for street in streetArray:
		street.sortList()
		street.moveCars()
##	for car in carArray:
##		car.move()
	for stoplight in stopArray:
		stoplight.step()

win = GraphWin('test',500,500,False)

streets = []
streets.append(Street(Point(50, 250), Point(450, 250), 10, win))
streets.append(Street(Point(250, 50), Point(250, 450), 10, win))

stoplights = []
stoplights.append(StopLight(streets[0], streets[1], 10, 10, win))


#is this even necessary? cars are stored in the street carList
cars = []#[Car(60,5,win,streets[0],"red"), Car(10,-5,win,streets[1],"blue")]
streets[0].addCar(Car(60,5,win,streets[0],"red"))
streets[1].addCar(Car(10,-5,win,streets[1],"blue"))

for i in range(100):
	step(cars, streets, stoplights)
	win.update()
	time.sleep(0.5)

win.getMouse()
win.close()
