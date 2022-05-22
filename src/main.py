import os
import random
import tkinter as tk
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

x = 1400
cycle = 0
check = 1
idle_num = [1, 2, 3, 4]
sleep_num = [10, 11, 12, 13, 15]
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)
img_path = BASE_DIR / "static"

# Event change - and the probability to do an action
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print("idle")
        window.after(400, update, cycle, check, event_number, x)
    elif event_number == 5:
        check = 1
        print("from idle to sleep")
        window.after(100, update, cycle, check, event_number, x)
    elif event_number in walk_left:
        check = 4
        print("walking towards left")
        window.after(100, update, cycle, check, event_number, x)
    elif event_number in walk_right:
        check = 5
        print("walking towards right")
        window.after(100, update, cycle, check, event_number, x)
    elif event_number in sleep_num:
        check = 2
        print("sleep")
        window.after(1000, update, cycle, check, event_number, x)
    elif event_number == 14:
        check = 3
        print("from sleep to idle")
        window.after(100, update, cycle, check, event_number, x)


# function to loop each frame
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)

    return cycle, event_number


# update the frame by assigning a number to every action
def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)

    # idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(
            cycle, idle_to_sleep, event_number, 10, 10
        )

    # sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)

    # sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 1, 1)

    # walk toward left
    elif check == 4:
        frame = walking_positive[cycle]
        cycle, event_number = gif_work(
            cycle, walking_positive, event_number, 1, 9
        )
        x -= 10

    # walk toward right
    elif check == 5:
        frame = walking_negative[cycle]
        cycle, event_number = gif_work(
            cycle, walking_negative, event_number, 1, 9
        )
        x -= -10

    window.geometry("100x100+" + str(x) + "+1050")
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)


window = tk.Tk()

# gif to frames
idle = [
    tk.PhotoImage(
        file=os.path.join(img_path, "idle.gif"), format="gif -index %i" % (i)
    )
    for i in range(5)
]

idle_to_sleep = [
    tk.PhotoImage(
        file=os.path.join(img_path, "idle_to_sleep.gif"),
        format="gif -index %i" % (i),
    )
    for i in range(8)
]

sleep = [
    tk.PhotoImage(
        file=os.path.join(img_path, "sleep.gif"), format="gif -index %i" % (i)
    )
    for i in range(3)
]

sleep_to_idle = [
    tk.PhotoImage(
        file=os.path.join(img_path, "sleep_to_idle.gif"),
        format="gif -index %i" % (i),
    )
    for i in range(8)
]

walking_positive = [
    tk.PhotoImage(
        file=os.path.join(img_path, "walking_positive.gif"),
        format="gif -index %i" % (i),
    )
    for i in range(8)
]

walking_negative = [
    tk.PhotoImage(
        file=os.path.join(img_path, "walking_negative.gif"),
        format="gif -index %i" % (i),
    )
    for i in range(8)
]

# make gif background transparent
window.config(highlightbackground="black")
window.overrideredirect(True)
window.wm_attributes("-transparentcolor", "black")

# assign as a label
label = tk.Label(window, bd=0, bg="black")
label.pack()

# loop the program
window.after(1, update, cycle, check, event_number, x)

window.mainloop()
