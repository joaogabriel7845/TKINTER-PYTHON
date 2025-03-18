from customtkinter import *
import getpass, platform, pygame, time, os, sys
from PIL import Image

tela = CTk()
tela.config(background='white')
tela.title('Login')
tela.geometry("350x400")
tela.resizable(False, False) # impossibilita redimensionar a tela

def resource_path(relative_path):
    """ Retorna o caminho absoluto para um arquivo PNG, funcionando para .py e .exe """
    if hasattr(sys, '_MEIPASS'):
        # Quando rodando no .exe, usa o diretório temporário
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


pagina1 = CTkFrame(tela, width=340, height=390, fg_color='#c9c8c7', bg_color='white')
pagina1.pack(pady=10)

email = CTkEntry(pagina1, placeholder_text='Digite o seu email.', width=200)
email.place(x=70, y=300)


label1_pag1 = CTkLabel(pagina1, text='Bem-vindo ao App de Informações!', text_color='black', font=('Minecraft', 15))
label1_pag1.place(relx=0.50, rely=0.10, anchor=CENTER)

label2_pag2 = CTkLabel(pagina1, text='Clique em continuar para ver seus dados pessoais.', text_color='black', font=('Minecraft', 10))
label2_pag2.place(relx=0.50, rely=0.30, anchor=CENTER)

dogcore = CTkLabel(pagina1, text='By dogcore', text_color='black', font=('Minecraft', 10))
dogcore.place(x=15, y=340)

imagem = CTkImage(Image.open('informacao.png'), size=(100, 100))
label = CTkLabel(pagina1, image=imagem, text=None)
label.place(relx=0.50, rely=0.55, anchor=CENTER)

def nav_pagina2():
    usuario = getpass.getuser()
    sistema = platform.system()
    versao = platform.version()
    arquitetura = platform.architecture()[0]    

    pagina1.forget()
    
    email_digitado = email.get() if email.get() != '' else 'Não informado'

    pagina2 = CTkFrame(tela, width=340, height=390, fg_color='#c9c8c7', bg_color='white')
    pagina2.pack(pady=10)

    label1_pag2 = CTkLabel(pagina2, text='Informações Pessoais', text_color='black', font=('Minecraft', 15))
    label1_pag2.place(relx=0.50, rely=0.20, anchor=CENTER)

    label2_pag1 = CTkLabel(pagina2, text=f'Nome: {usuario}\nEmail: {email_digitado}\nSistema: {sistema +  versao}\nArquitetura do Sistema: {arquitetura}', text_color='black', font=('SF Pro Display', 13))
    label2_pag1.place(relx=0.50, rely=0.40, anchor=CENTER)

    
    def fecharsom():
        sombotao()
        time.sleep(0.5)
        tela.destroy()
    fechar = CTkButton(pagina2, text='Fechar', width=100, font=('Minecraft', 10), fg_color='black', hover_color='red', command=fecharsom)
    fechar.place(x=230, y=340)
    

    def voltar():
        pagina2.forget()
        pagina1.pack(pady=10)
        sombotao()
    botao_voltar = CTkButton(pagina2, text='Voltar', width=100, font=('Minecraft', 10), fg_color='black', hover_color='gray', command=voltar)
    botao_voltar.place(x=10, y=340)

def sombotao():
    pygame.init()
    pygame.mixer.music.load('clique.mp3')
    pygame.mixer.music.play()

def fazertudo():
    nav_pagina2()
    sombotao()
botao_continuar = CTkButton(pagina1, width=100, text='Continuar', font=('Minecraft', 10), fg_color='black', hover_color='gray', command=fazertudo)
botao_continuar.place(x=230, y=340)
tela.mainloop()