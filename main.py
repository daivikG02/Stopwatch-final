from tkinter import *
import datetime
 
root = Tk()
 
root.title("Stopwatch")
 
# width x height
root.geometry("550x300")
 
# just need an arbitrary date, then make sure it's set to 0 hours, 0 minutes and 0 seconds.
time = datetime.datetime(2022, 8, 5, 0, 0, 0)
 
# maybe later we can add milliseconds to make the stopwatch more precise
display = time.strftime("%H:%M:%S")
 
print(display)
 
# STOPWATCH DISPLAY ###########
 
stopwatch_label = Label(text=display, font=('Ariel', 80), height=0, width=0)
 
# side parameter 
stopwatch_label.pack(side=TOP)
 
# KEEP TRACK OF WHETHER STOPWATCH IS RUNNING
 
running = False
 
# FUNCTIONS #################
 
# Start the timer
def start():
 
    global running
 
    if not running:
 
        running = True
        update()
 
 
# Pause the timer
def pause():
    global running
 
    if running:
 
        stopwatch_label.after_cancel(update_time)
        running = False
 
# Reset the timer
def reset():
 
    pause()
 
    global time
    time = datetime.datetime(2022, 8, 5, 0, 0, 0)
 
    global display
    display = time.strftime("%H:%M:%S")
 
    stopwatch_label.config(text=display)
 
 
# Make the timer clock go up
def update():
 
    global time
    time += datetime.timedelta(seconds=1)
 
    global display
    display = time.strftime("%H:%M:%S")
 
    stopwatch_label.config(text=display)
 
    global update_time
    update_time = stopwatch_label.after(1000, update)
 
 
 
 
# BUTTONS ###################
 
# Make the start button
 
start_button = Button(text="Start", font=('Ariel', 30), height=4,width=7, command=start)
 
start_button.pack(side=LEFT)
 
# (using the code above as a hint:)
# Make the pause button
 
pause_button = Button(text="Pause", font=('Ariel', 30), height=4,width=7, command=pause)
 
pause_button.pack(side=LEFT)
 
# Make the reset button
 
reset_button = Button(text="Reset", font=('Ariel', 30), height=4,width=7, command=reset)
 
reset_button.pack(side=LEFT)
 
 
mainloop()
