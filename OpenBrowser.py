import webbrowser
from tkinter import *

root = Tk( ) # o root representa o Tk

root.title('Abrir Browser') # O título do root
root.geometry('300x200') # o tamanho do root

def google(): # função para abrir o browser no google
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20) #botão e definições do botão
root.mainloop() # chama a função