from graphics import *
from Car import *

win = GraphWin('test',250,250, autoflush=False)

car1 = Car(1,1,2,0,win)

x=0

while (x<100):
	car1.move()
	x += 1
	win.update()
	time.sleep(5)