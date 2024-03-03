import tkinter
from tkinter import messagebox

fenetre = tkinter.Tk()
fenetre.option_add("*font", "lucida 30 bold italic")
fenetre.title('Ma Fenetre :)')

titreLabel = tkinter.Label(fenetre, text="📢 Bonjour Python !",
                           background="#7C7C7C", foreground="#ffffff", font=('Courier New', 42))
titreLabel.pack()

prenomEntry = tkinter.Entry(fenetre, width=50)
prenomEntry.pack()

bonjourButton = tkinter.Button(
    fenetre,
    text="Dis Bonjour",
    command=lambda: messagebox.showinfo(
        "Bonjour", "Bonjour " + prenomEntry.get() + " !")
)
bonjourButton.pack()

exitButton = tkinter.Button(fenetre, text="Bye bye",
                            command=lambda: fenetre.quit())
exitButton.pack()

dessinCanvas = tkinter.Canvas(fenetre, width= 800, height= 400, background='orange')
dessinCanvas.pack()
dessinCanvas.create_rectangle(10, 10, 500, 300, fill='white')
dessinCanvas.create_oval(520, 10, 570, 60, fill='white')


fenetre.mainloop()
