from customtkinter import *

tela = CTk()
tela._set_appearance_mode('light')
tela.title('Login')
tela.geometry("700x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

botao = CTkButton(tela, width=200, height=30, text='Clique Aqui!', bg_color='white')
botao.place(x=1, y=10)

tela.mainloop()