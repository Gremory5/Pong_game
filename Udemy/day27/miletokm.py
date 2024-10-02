from tkinter import *


#creare la finestra iniziale
window = Tk()
window.title("Miles to KM converter")
window.minsize(width=150, height=150)
window.config(padx=20,pady=20)

def convert():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

#labels
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)
miles_label.config(padx=2,pady=2)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=2)
equal_label.config(padx=2,pady=2)

km_result_label = Label(text="0")
km_result_label.grid(column=1,row=2)
km_result_label.config(padx=2,pady=2)

km_label = Label(text="Km")
km_label.grid(column=2,row=2)
km_label.config(padx=2,pady=2)

#Entry

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)


#Button

button = Button(text="Calculate", command=convert)
button.grid(column=1,row=3)
button.config(padx=2,pady=2)






window.mainloop() # Deve stare sempre alla fine del codice