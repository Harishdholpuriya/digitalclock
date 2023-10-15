from tkinter import Label, Tk 
from tkinter import Label, Tk 
import time
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#000000"
foreground= "#7FFF00"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S %p")
   label.config(text=time_live) 
   label.after(200, digital_clock)
   label.pack(anchor='center')

digital_clock()
app_window.mainloop()

