from customtkinter import *

tela = CTk()
tela.config(background='white')
tela.title('Login')
tela.geometry("700x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

tela.mainloop()