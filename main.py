import os
import random
import string
import tkinter

version = "1.52"

website = "onderkin.tk"


def generate(arg):
    for _ in range(5):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for _ in range(arg))
        if not os.path.exists(result_str):
            os.makedirs(result_str)
        else:
            print('test')


window = tkinter.Tk()
btn = tkinter.Button(window,text="generate 5 random folders",fg='blue',command=lambda:generate(random.randint(1, 10)))
btn.place(x=50, y=62)
lbl = tkinter.Label(window, text="Random Folder Generator", fg='black', font=("Helvetica", 16))
lbl.place(x=50, y=20)
bta = tkinter.Label(window, text=f'production build v{version} \nby Maarten van Heusden \nhttps://{website}/')
bta.place(x=120, y=160)
window.title(f'RandomFolderGenerator v{version}')
window.geometry("300x210+800+200")
window.mainloop()
