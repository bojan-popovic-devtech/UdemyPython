import math
import tkinter


def parabola(canvas_, size):
    for x in range(size):
        y = x * x / size
        plot(canvas_, x, -y)
        plot(canvas_, -x, -y)


def circle(canvas_, radius, g, h, colour="red"):
    canvas_.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # for x in range(g, g + radius):
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(canvas_, x, y)
    #     plot(canvas_, x, 2 * h - y)
    #     plot(canvas_, 2 * g - x, y)
    #     plot(canvas_, 2 * g - x, 2 * h - y)


def draw_axes(canvas_):
    canvas_.update()
    x_origin = canvas_.winfo_width() / 2
    y_origin = canvas_.winfo_height() / 2
    canvas_.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas_.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas_.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvas_, x_, y_):
    canvas_.create_line(x_, y_, x_+1, y_+1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, "blue")
mainWindow.mainloop()
