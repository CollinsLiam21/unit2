#Liam Collins
#1/31/18
#coloredSquare.py

from ggame import*

red = Color(0xff0000,1)
line = LineStyle(3,red)
rectangle = RectangleAsset(100,100,line,red)

Sprite(rectangle)
myApp = App()
myApp.run()

blue = Color(0x0000ff,1)
line = LineStyle(3,blue)
rectangle = RectangleAsset(100,100,line,blue)

Sprite(rectangle)
myApp = App()
myApp.run()

green = Color(0x00ff00,1)
line = LineStyle(3,green)
rectangle = RectangleAsset(100,100,line,green)

Sprite(rectangle)
myApp = App()
myApp.run()

yellow = Color(0xffff00,1)
line = LineStyle(3,yellow)
rectangle = RectangleAsset(100,100,line,yellow)

Sprite(rectangle)
myApp = App()
myApp.run()
