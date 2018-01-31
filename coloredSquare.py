#Liam Collins
#1/31/18
#coloredSquare.py

from ggame import*
from random import randint
num = randint(1,4)

if num == 1:
    red = Color(0xff0000,1)
    green = Color(0x00ff00,1)
    line = LineStyle(10,green)
    rectangle = RectangleAsset(400,400,line,red)

    Sprite(rectangle)
    myApp = App()
    myApp.run()

elif num == 2: 
    blue = Color(0x0000ff,1)
    yellow = Color(0xffff00,1)
    red = Color(0xff0000,1)
    line = LineStyle(25,yellow)
    line2 = LineStyle(10,red)
    rectangle = RectangleAsset(200,100,line,blue)

    Sprite(rectangle)
    myApp = App()
    myApp.run()

elif num == 3:
    green = Color(0x00ff00,1)
    blue = Color(0x0000ff,1)
    line = LineStyle(3,blue)
    rectangle = RectangleAsset(100,300,line,green)

    Sprite(rectangle)
    myApp = App()
    myApp.run()

else:
    yellow = Color(0xffff00,1)
    red = Color(0xff0000,1)
    line = LineStyle(15,red)
    rectangle = RectangleAsset(250,250,line,yellow)
    
    Sprite(rectangle)
    myApp = App()
    myApp.run()
