import random
import os
import tkinter as tk
from PIL import Image, ImageTk

class Meme:
    def game():
        window=tk.Toplevel()
        window.title('What do you meme?')
        window.geometry("1300x675")
        pull=str(random.choice(os.listdir(Dir.get())))
        img=Image.open(Dir.get()+'/'+pull)
        width, height = img.size
        if width>762 and height>700:
            imgres=img.resize((762,700))
        else:
            imgres=img
        imgfin=ImageTk.PhotoImage(imgres)
        canvas=tk.Label(master=window,image=imgfin)
        canvas.pack()
        window.mainloop()

root=tk.Tk()
root.title('Picture Generator')
root.geometry("400x100")

File=tk.Label(root,text='Specify Folder:')
File.pack()
Dir=tk.Entry(root)
Dir.pack()
butt=tk.Button(master=root,text="Generate",command=lambda:Meme.game())
butt.pack()
Note=tk.Label(root, text='Make sure the folder you are referencing is in the same folder as the program!!!',font=('Arial', 10),wraplength=400)
Note.pack()

root.mainloop()