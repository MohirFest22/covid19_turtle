from turtle import *

tk = Screen()
tk.title("shakl")
tk.bgcolor("black")
tk.setup(700,800)
a,b=0,0
color("limegreen")
for i in range(200):
	hideturtle()
	speed(140)
	fd(a)
	rt(b)
	a+=3
	b+=1


tk.mainloop()
