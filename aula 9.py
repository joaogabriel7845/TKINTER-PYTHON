from customtkinter import *

tela = CTk()
tela.config(background='white')
tela.title('Login')
tela.geometry("700x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela
def mostrarsenha():
    if mostrarsenhavar.get():
        senha._entry.configure(show='')
    else:
        senha._entry.configure(show='*')

senha = CTkEntry(tela, bg_color='white',placeholder_text='Digite sua senha', show='*')
senha.place(relx=0.50, rely=0.45, anchor=CENTER)
mostrarsenhavar = BooleanVar(value=False)
mostrarsenha = CTkCheckBox(tela, text='Mostrar senha', bg_color='white', variable=mostrarsenhavar ,text_color='black', command=mostrarsenha)
mostrarsenha.place(relx=0.70, rely=0.45, anchor=CENTER)

combobox = CTkComboBox(tela, values=['Tkinter', 'CTk', 'Pandas', 'Flask'], width=300, bg_color='white')
combobox.set('Selecionar')
combobox.pack()
tela.mainloop()