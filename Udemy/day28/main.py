from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- POP - UP MECHANISM ------------------------------- # 
def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    start_bt.config(state="normal")
    reset_bt.config(state="disabled")
    window.after_cancel(timer)
    #Could not use the .config() here. Since this is a canvas, you have to use itemconfig(). Also, when you initially
    # create the timer_text, you had to use canvas.create_text to create it (see the code further down in the program).
    canvas.itemconfig(timer_text, text="00:00")
    #reset the title label to "timer"
    label_text.config(text="Timer")
    #reset the checkmarks
    check_text.config(text="")

    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    start_bt.config(state="disabled")
    reset_bt.config(state="normal")
    
    #if it's the 2nd/4th/6th rep:
    if reps % 2 == 0:
        countdown(short_break_sec)
        label_text.config(text="SHORT BREAK", fg=PINK)
        focus_window("on")
        
        
    #if it's the 8th rep: 
    elif reps % 8 == 0:
        countdown(long_break_sec)
        label_text.config(text="LONG BREAK", fg=PINK)
        focus_window("on")
    #if it's the 1st/3rd/5th/7th rep:
    else:
        countdown(work_sec)
        label_text.config(text="WORK", fg=RED)
        focus_window("off")


    
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global reps
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    #aggiornamento del timer in base al tempo passato
    if count > 0:
        global timer
        timer = window.after(100,countdown, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for n in range(work_sessions):
            marks += "✔"
        check_text.config(text=marks)




        




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,background=YELLOW)




canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(102,130, text="00:00",fill ="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1 )



label_text = Label(text="Timer",width=12, font=(FONT_NAME,26,"bold"),fg=GREEN,bg=YELLOW,highlightthickness=0)
label_text.grid(column=1,row=0)
check_text = Label( font=(FONT_NAME,15,"bold"),fg=GREEN,bg=YELLOW,pady=10)
check_text.grid(column=1,row=2)


start_bt = Button(text="Start",font=(FONT_NAME,10),highlightthickness=0, command=start_timer, state="normal")
start_bt.grid(column=0,row=2)
reset_bt = Button(text="Reset",font=(FONT_NAME,10),highlightthickness=0, command=reset_timer, state="disabled")
reset_bt.grid(column=2,row=2)





window.mainloop()