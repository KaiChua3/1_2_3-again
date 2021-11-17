#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def falling_apple():
  apple.penup()
  apple.goto(0,-200)
  trtl.clear()
def draw_an_A():
  trtl.penup()
  trtl.goto(0,0)
  trtl.color("white")
  trtl.write("A", font=("Arial", 74, "bold"))
  trtl.hideturtle()

wn.listen()
trtl.mainloop()
#-----function calls-----
draw_apple(apple)
draw_an_A()
wn.bgpic("background.gif")
wn.onkeypress(falling_apple,"a")
wn.listen()
wn.mainloop()
