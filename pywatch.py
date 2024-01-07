from tkinter import Tk, Label, Button, Frame
from math import trunc
from datetime import datetime, timedelta

root = Tk()
root.wait_visibility(root)
root.title("pywatch")
root.attributes("-topmost", True)
root.config(bg="white")

label = Label(root, text="", font=("Fira Mono", 20))
label.pack()


def close():
    root.destroy()


running = False
time_start = None
ready = True


def render(elapsed):
    label["text"] = f"{trunc(elapsed / 3600):02d}:{trunc(elapsed % 3600 / 60):02d}:{elapsed % 3600 % 60:05.2f}"


def start():
    global time_start, running
    time_start = datetime.now()
    running = True

    def update():
        render((datetime.now() - time_start).total_seconds())
        if running:
            label.after(10, update)

    update()


def stop():
    global running
    running = False


frame = Frame(root)

start = Button(frame, text="Start", command=start)
stop = Button(frame, text="Stop", command=stop)
close = Button(frame, text="Close", command=close)
frame.pack(anchor='center', pady=5)
start.pack(side="left")
stop.pack(side="left")
close.pack(side="left")
render(0)

label.pack()
root.mainloop()
