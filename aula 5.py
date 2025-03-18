from customtkinter import *

tela = CTk()
tela.title('Login')
tela.geometry("700x400")
tela.config(background='white')
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

label = CTkLabel(tela, text='Curso de Custom Tkinter', text_color='black', bg_color='white', font=('Montserrat', 20, 'bold'))
label.pack(pady=20)
tela.mainloop()