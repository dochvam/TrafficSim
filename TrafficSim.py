from graphics import *
from Car import *
from Street import *

win = GraphWin('test',500,500,False)

street1 = Street(Point(50, 100), Point(450, 200), 30, win)


car2 = Car(60,5,win,street1,"red")
car1 = Car(1,30,win,street1,"blue")

print(car1)

while (car1.speed > 0):
	car1.move()
	car2.move()
	win.update()
	time.sleep(0.2)

win.getMouse()
win.close()