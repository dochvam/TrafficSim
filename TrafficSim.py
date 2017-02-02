from graphics import *
from Car import *
from Street import *

def step(carArray, streetArray):
	for street in streetArray:
		street.sortList()
	for car in carArray:
		car.move()

win = GraphWin('test',500,500,False)

streets = []
streets.append(Street(Point(50, 100), Point(450, 200), 10, win))

cars = []
# cars.append(Car(locOnStreet,speed,win,street,color))
cars.append(Car(60,10,win,streets[0],"red"))
cars.append(Car(1,5,win,streets[0],"blue"))
cars.append(Car(30,1,win,streets[0],"yellow"))

##print(streets[0].printCarList())
##streets[0].sortList()
##print(streets[0].printCarList())
##


while (cars[0].speed > 0):
	step(cars, streets)
	win.update()
	time.sleep(0.1)

win.getMouse()
win.close()
