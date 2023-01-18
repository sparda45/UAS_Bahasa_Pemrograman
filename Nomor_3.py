from tkinter import * #module tkinter untuk membuat GUI

window = Tk()

window.title("Gui respond") #untuk judul di windows

window.geometry('350x200') #ukuran windows GUI

lbl = Label(window, text="Hello") #text/label yang ada di dalam GUI 

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Sudah di klik!!") #action ketika kita mengklik button

btn = Button(window, text="coba pencet", command=clicked) #membuat button serta membuat text yang ada di dalamnya

btn.grid(column=1, row=0)

window.mainloop()