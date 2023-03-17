from tkinter import *
from tkinter import filedialog 
from PIL import ImageTk, Image
from main import *
import tkinter as tk

top = Tk()
top.geometry('1280x720')
top.title("Search with Camera")
top.configure(background='#FFFDD0')

window_title = Label(top, text='SEARCH WITH CAMERA', background='#FFFDD0', font=('Ubuntu', 20, 'bold'))
window_title.pack(side=TOP, pady=10)

open_camera = Button(top, text="Open Camera", command= lambda: recog(), padx=10, pady=5)
open_camera.configure(background='#364156', foreground='white', font=('Ubuntu', 12, 'bold'))
open_camera.pack(side=TOP, pady=15)

# TODO: Read the keywords detected by camera and display it in a container with its index numbers

keywords_label = Label(top, text='Detected Keywords:', font=("Ubuntu", 10))
keywords_label.pack(side=TOP)

# scroll=Scrollbar(top, orient='vertical')
# scroll.pack(side=RIGHT, fill='y')

result = recog()

display_keywords = tk.Text(top, height=20, width=45)
for i in range(len(result)):
     display_keywords.insert(tk.END, f'{i} : {result[i]}\n')

# scroll.config(command=display_keywords.yview)
display_keywords.pack(side=TOP, pady=20)

entry_label = Label(top, text='Enter Number:', font=('Ubuntu', 10))
entry_label.place(x=275, y=650)

entry = Entry(top, width=40)
entry.focus_set()
entry.place(x=400, y=650)

def get_text():
    number = int(entry.get())
    # query = ' '.join([result[i] for i in range(number, len(result)) if len(result[i]) != 0 ])
    return google_search(result[number], result[number + 1])


search = Button(top, text="Search", command=lambda: get_text(), padx=10, pady=2)
search.configure(background='#364156', foreground='white', font=('Ubuntu', 10, 'bold'))
search.place(x=850, y=647.5)


top.mainloop()