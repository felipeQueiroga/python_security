import webbrowser
from tkinter import *

def dispra_caminho():
    webbrowser.open(my_text.get())  

root = Tk( )
root.title('Abrir Browser')
root.geometry('300x200')

#anchor N=norte, S=sul, E=Leste, W=oeste

label = Label(root, text="URL:", background="#dde", foreground="#009", anchor=W)
label.place(x=10, y=20, width=100, height=20)

my_text = Entry(root)
my_text.place(x=10, y=40, width=200, height=20)

button = Button(root, text='Abrir a URL', command=dispra_caminho)
button.pack(pady=60)

root.mainloop()



