from customtkinter import *

tela = CTk()
tela._set_appearance_mode('light')
tela.title('Login')
tela.geometry("700x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

entry = CTkEntry(tela, width=200, bg_color='white', placeholder_text='Digite seu nome')
entry.pack(pady=20)

textbox = CTkTextbox(tela, width=200, height=300, bg_color='white')
textbox.pack()
tela.mainloop()