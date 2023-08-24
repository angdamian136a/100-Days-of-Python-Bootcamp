from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.08
reps = 0
timer = None


def raise_window(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        countdown(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min <10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        # raise_window(window)
        start_timer()
        marks = " "
        work_sessions = math.floor((reps-1)/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=timer_reset)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

window.mainloop()

