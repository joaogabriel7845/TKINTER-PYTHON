from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygame, time, os, sys

# Função para carregar recursos
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def sombotao():
    pygame.init()
    pygame.mixer.init()
    som1 = pygame.mixer.Sound('clique.mp3')
    som2 = pygame.mixer.Sound('calmacalabreso.mp3')

    som1.play()

    pygame.time.wait(int(som1.get_length() * 0.1))

    som2.play()

def calma():
    calabreso = Image.open("calmaCALA.gif")  # Abre o arquivo GIF
    frames = [ImageTk.PhotoImage(frame.resize((200, 200))) for frame in ImageSequence.Iterator(calabreso)]  # Extrai os frames do GIF

# 1. Cria um label para exibir o GIF
    label = CTkLabel(tela, text="")  # Cria um label vazio
    label.place(relx=0.50, rely=0.55, anchor=CENTER)  # Posiciona o label na janela

# 2. Função para animar o GIF
    def animar_gif(frame_num=0):
        label.configure(image=frames[frame_num])  # Atualiza o frame exibido no label
        tela.after(100, animar_gif, (frame_num + 1) % len(frames))  # Chama a função novamente após 100ms

    animar_gif()  # Inicia a animação
    texto.configure(text='CALMA CALABRESO !') 
    sombotao()
    def fechar():
        sombotao()
        time.sleep(0.5)
        tela.destroy()
    frame = CTkFrame(tela, width=250, height=350, bg_color='#242424')
    frame.place(relx=0.50, rely=0.90, anchor=CENTER)
    botao_fechar = CTkButton(frame, text='Fechar', command=fechar, bg_color='#242424',fg_color='green',hover_color='red', font=('Minecraft', 12))
    botao_fechar.pack(pady=20)
    botao.pack_forget()

tela = tk.Tk()
tela.title('Login')
tela.geometry("400x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela
janela = CTkFrame(tela, bg_color='#242424')
janela.pack(fill="both", expand=True)

imagem2 = CTkImage(Image.open('clique.png'), size=(20, 20))
verde_escuro = '#006400'
botao = CTkButton(janela, width=200, height=50,text='Clique aqui calabreso!', image=imagem2, bg_color='#242424',fg_color='green', hover_color=verde_escuro, font=('Minecraft', 12),command=calma)
botao.pack(pady=155)
texto = CTkLabel(janela, text='', font=('Minecraft', 20))
texto.pack(pady=50)

tela.mainloop()