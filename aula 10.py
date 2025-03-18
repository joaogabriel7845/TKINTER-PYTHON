from customtkinter import *

tela = CTk()
tela.config(background='white')
tela.title('Login')
tela.geometry("700x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

radiobutton = CTkRadioButton(tela, text='Aceito!', bg_color='white', text_color='black', border_color='black')
radiobutton.pack(pady=20)

switch = CTkSwitch(tela, text='Ligar', bg_color='white', text_color='black', button_color='black', hover=None)
switch.pack()
tela.mainloop()