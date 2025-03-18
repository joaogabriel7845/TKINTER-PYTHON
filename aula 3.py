from customtkinter import *

tela = CTk()
tela._set_appearance_mode('light')
tela.title('Login')
tela.geometry("700x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

botao_1 = CTkButton(tela, width=200, height=30, text='Botão 1', bg_color='white')
botao_1.pack(pady=20)

botao_2 = CTkButton(tela, width=200, height=30, text='Botão 1', bg_color='white')
botao_2.pack(pady=20)

botao_3 = CTkButton(tela, width=200, height=30, text='Botão 1', bg_color='white')
botao_3.pack(pady=20)
tela.mainloop()