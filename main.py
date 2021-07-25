import random
import os
import tkinter as tk
from PIL import Image, ImageTk

class Meme:
    def game():
        window=tk.Toplevel()
        window.title('What do you meme?')

        def normal():
            imgres=img.rotate(0)
            width, height = imgres.size
            if width>1012 or height>675:
                imgsize=imgres.resize((1012,675))
            elif width<216 or height<144:
                imgres=img.resize((216,144))
            else:
                imgsize=imgres
            imgfin=ImageTk.PhotoImage(imgsize)
            canvas.configure(image=imgfin)
            canvas.image=imgfin

        def rotateright():
            imgres=img.rotate(90)
            width, height = imgres.size
            if width>1012 or height>675:
                imgsize=imgres.resize((1012,675))
            elif width<216 or height<144:
                imgres=img.resize((216,144))
            else:
                imgsize=imgres
            imgfin=ImageTk.PhotoImage(imgsize)
            canvas.configure(image=imgfin)
            canvas.image=imgfin

        def rotateleft():
            imgres=img.rotate(270)
            width, height = imgres.size
            if width>1012 or height>675:
                imgsize=imgres.resize((1012,675))
            elif width<216 or height<144:
                imgres=img.resize((216,144))
            else:
                imgsize=imgres
            imgfin=ImageTk.PhotoImage(imgsize)
            canvas.configure(image=imgfin)
            canvas.image=imgfin

        def flipup():
            imgres=img.rotate(180)
            width, height = imgres.size
            if width>1012 or height>675:
                imgsize=imgres.resize((1012,675))
            elif width<216 or height<144:
                imgres=img.resize((216,144))
            else:
                imgsize=imgres
            imgfin=ImageTk.PhotoImage(imgsize)
            canvas.configure(image=imgfin)
            canvas.image=imgfin

        button=tk.Button(window, text="Normal",command=lambda:normal())
        button.grid(row=0,column=0,sticky="WENS")

        button1=tk.Button(window,text="Rotate Left",command=lambda:rotateright())
        button1.grid(row=0,column=1,sticky="WENS")

        button2=tk.Button(window,text="Rotate Right", command=lambda:rotateleft())
        button2.grid(row=0, column=2,sticky="WENS")

        button3=tk.Button(window,text="Flip", command=lambda:flipup())
        button3.grid(row=0, column=3,sticky="WENS")

        canvas=tk.Label(window,text="")

        #data pull
        pull=str(random.choice(os.listdir(Dir.get())))
        img=Image.open(Dir.get()+'/'+pull)
        
        #image size check
        width, height = img.size
        if width>1012 or height>675:
            imgres=img.resize((1012,675))
        elif width<216 or height<144:
            imgres=img.resize((216,144))
        else:
            imgres=img

        #image load
        imgfin=ImageTk.PhotoImage(imgres)
        canvas.configure(image=imgfin)

        canvas.grid(row=1,column=0,columnspan=4,sticky="WENS",padx=150)
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
