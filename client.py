import socket
from config import ADDRESS, CANVAS_WIDTH, CANVAS_HEIGHT

from tkinter import Tk, Canvas


def draw_fun(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill='black')
    client.send(f'{x} {y}'.encode('ascii'))


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

root = Tk()
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.bind('<B1-Motion>', draw_fun)
canvas.pack()
root.mainloop()
