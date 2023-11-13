from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='Ручка', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='Кисть', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='Цвет', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='Ластик', command=self.erase_button)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)
        self.choose_size_button.set(5)

        self.can = Canvas(self.root, bg='white', width=600, height=600)
        self.can.grid(row=1, columnspan=5)

        self.setup()
        self.root = mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = 'black'
        self.eraser_on = False
        self.activate_button = self.pen_button
        self.can.bind('<B1-Motion>', self.paint)
        self.can.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.color = askcolor()[1]

    def activate_button(self, some_button, eraser_mode=False ):
        self.activate_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.activate_button = some_button
        self.eraser_on = eraser_mode

    def erase_button(self):
        self.activate_button(self.erase_button, eraser_mode=True)

    def reset(self, event):
        self.old_x = self.old_y = None

    def paint(self, event):
        # print(f'x: {event.x}, y: {event.y}')
        self.line_width = self.choose_size_button.get()
        self.paint_color = self.color

        if self.old_x and self.old_y:
            self.can.create_line(self.old_x,
                                 self.old_y,
                                 event.x,
                                 event.y,
                                 width=self.line_width,
                                 fill=self.paint_color,
                                 capstyle=ROUND,
                                 smooth=True)


        self.old_x = event.x
        self.old_y = event.y


if __name__ == '__main__':
    Paint()