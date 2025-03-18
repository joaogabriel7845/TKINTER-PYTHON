from customtkinter import *

tela = CTk()
tela._set_appearance_mode('light')
tela.title('Login')
tela.geometry("700x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

botao_1 = CTkButton(tela, width=100, height=30, text='Botão 1', bg_color = 'white')
botao_1.grid(row=0, column=0)

botao_2 = CTkButton(tela, width=100, height=30, text='Botão 2', bg_color = 'white')
botao_2.grid(row=0, column=1)

botao_3 = CTkButton(tela, width=100, height=30, text='Botão 3', bg_color = 'white')
botao_3.grid(row=1, column=0)

botao_4 = CTkButton(tela, width=100, height=30, text='Botão 4', bg_color = 'white')
botao_4.grid(row=1, column=1)

tela.mainloop()