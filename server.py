import socket
from config import ADDRESS, CANVAS_WIDTH, CANVAS_HEIGHT

from threading import Thread
from queue import Queue, Empty

from tkinter import Tk, Canvas


def server_loop():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen()
    connection, address = server.accept()

    while True:
        message = connection.recv(1024).decode('ascii').split(' ')
        server_queue.put((int(message[0]), int(message[1])))


def draw_fun():
    try:
        coords = server_queue.get_nowait()
        x, y = coords
        canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill='black')
    except Empty:
        pass
    root.after(1, draw_fun)
    return


server_queue = Queue(0)
server_thread = Thread(target=server_loop)
server_thread.start()

root = Tk()
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()
root.after(1, draw_fun)
root.mainloop()
