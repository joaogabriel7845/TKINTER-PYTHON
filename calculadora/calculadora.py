from customtkinter import *
from PIL import ImageFont, Image, ImageTk
import pygame
import os
import sys
import tkinter as tk  # Importe o tkinter nativo para definir o ícone
# from tkinter import font as tkFont

# Função para carregar recursos
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Criação da janela principal com tkinter
root = tk.Tk()
root.title('Calculadora')
root.geometry('400x500')
root.resizable(False, False)

# Defina o ícone da janela
root.iconbitmap(default=resource_path(os.path.join('icones', 'calculadora.ico')))  # Ajuste o caminho do ícone

# Carregar a fonte personalizada
fonte_minecraft = ImageFont.truetype(resource_path(os.path.join('fonts', 'Minecraft.ttf')), 15)

# Criação da janela do customtkinter
janela = CTkFrame(root, fg_color='#0D0D0D', bg_color='black')
janela.pack(fill="both", expand=True)

# Inicialização do PyGame
pygame.mixer.init()

# FUNÇÕES
def calcular():
    try:
        # Obtém a expressão do campo de entrada
        expressao = valores.get().strip()
        
        # Avalia a expressão matemática
        resultado = eval(expressao)

        # Limpa o campo de entrada e insere o resultado
        valores.delete(0, 'end')
        valores.insert(0, f'{resultado}')

        # Toca o som do botão
        sombotao()
    except (NameError, TypeError):
        # Se ocorrer um erro, exibe uma mensagem de erro
        valores.delete(0, 'end')
        valores.insert(0, f'Erro: Expressão inválida')
        sombotao()
    except ZeroDivisionError:
        valores.delete(0, 'end')
        valores.insert(0, 'Erro: Divisão por zero')
        sombotao()

def adicionarNUM(num):
    valores.insert('end', num)
    sombotao()

def trocarsinal():
    try:
        valor_atual = valores.get().strip()

        if valor_atual:
            if valor_atual.startswith('-'):
                novo_valor = valor_atual[1:]
            else:
                novo_valor = '-' + valor_atual

            valores.delete(0, 'end')
            valores.insert(0, novo_valor)
        sombotao()
    except Exception as e:
        print(f'Erro ao trocar o sinal: {e}')
        sombotao()

def sombotao():
    try:
        pygame.mixer.music.load(resource_path(os.path.join('sons', 'clique.mp3')))
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Erro ao reproduzir o som: {e}")

def apagarNUM():
    valores.delete(0, 'end')
    sombotao()


# Entry
valores = CTkEntry(root, fg_color='#0D0D0D',bg_color='#0D0D0D',width=250, border_color='#0D0D0D',height=50, font=('Inter', 50))
valores.place(x=20, y=30)

# Button
apagar = CTkButton(janela, text='CE', fg_color='#35C2C2', width=70, height=65, font=('Inter', 20, 'bold'), command=apagarNUM)
apagar.place(x=20, y=120)

# Button
trocarsinal = CTkButton(janela, text='+/-', fg_color='#35C2C2', width=70, height=65, font=('Inter', 20, 'bold'), command=trocarsinal)
trocarsinal.place(x=110, y=120)

# Lista de imagens para alternar
imagens = [
    resource_path(os.path.join('calculadora', 'imagens', 'simpsons.jpg')),
    resource_path(os.path.join('calculadora', 'imagens', 'dogcore.jpg')),
    resource_path(os.path.join('calculadora', 'imagens', 'bia.png')),
    resource_path(os.path.join('calculadora', 'imagens', 'dogcore2.jpg')),
    resource_path(os.path.join('calculadora', 'imagens', 'tchola.jpg')),
    resource_path(os.path.join('calculadora', 'imagens', 'xiu.jpg')),
    resource_path(os.path.join('calculadora', 'imagens', 'esse cara.png')),
    resource_path(os.path.join('calculadora', 'imagens', 'dogcore3.jpg')),
    resource_path(os.path.join('calculadora', 'imagens', 'xuxu.jpg')),
    resource_path(os.path.join('calculadora', 'imagens', 'gb.png'))
]

# Índice da imagem atual
indice_imagem = 0

def mudar_foto():
    global indice_imagem
    sombotao()
    # Alterna para a próxima imagem na lista
    indice_imagem = (indice_imagem + 1) % len(imagens)
    imagem = Image.open(imagens[indice_imagem])
    imagem = imagem.resize((60, 45), Image.LANCZOS)
    imagem_tk = ImageTk.PhotoImage(imagem)
    dogcore.configure(image=imagem_tk)
    dogcore.image = imagem_tk  # Manter referência da imagem

# Imagem inicial do botão
imagem_inicial = Image.open(imagens[indice_imagem])
imagem_inicial = imagem_inicial.resize((60, 45), Image.LANCZOS)
imagem_tk_inicial = ImageTk.PhotoImage(imagem_inicial)

dogcore = CTkButton(
    janela, 
    text='', 
    image=imagem_tk_inicial,
    width=70, 
    height=65,
    fg_color='#35C2C2',
    bg_color='#0D0D0D',
    command=mudar_foto
)
dogcore.place(x=200, y=120)

botoes = [
    ('7', 20, 195), ('8', 110, 195), ('9', 200, 195), ('+', 300, 195),
    ('4', 20, 270), ('5', 110, 270), ('6', 200, 270), ('-', 300, 270),
    ('1', 20, 345), ('2', 110, 345), ('3', 200, 345), ('*', 300, 345),
    ('0', 20, 420), ('/', 300, 120), ('.', 200, 420), ('=', 300, 420)
]

for texto, x, y in botoes:
    if texto == '0':
        CTkButton(janela, text=texto, fg_color='#171718', width=160, height=65, hover_color='gray', font=('Inter', 20, 'bold'), command=lambda t=texto: adicionarNUM(t)).place(x=x, y=y)
    elif texto == '=':
        CTkButton(janela, text=texto, fg_color='#35C2C2', width=70, height=65, font=('Inter', 20, 'bold'), command=calcular).place(x=x, y=y)
    elif texto == '+' or texto == '-' or texto == '*' or texto == '/' or texto == '.':
        CTkButton(janela, text=texto, fg_color='#35C2C2', width=70, height=65, font=('Inter', 20, 'bold'), command=lambda t=texto: adicionarNUM(t)).place(x=x, y=y)
    else:
        CTkButton(janela, text=texto, fg_color='#171718', width=70, height=65, hover_color='gray', font=('Inter', 20, 'bold'), command=lambda t=texto: adicionarNUM(t)).place(x=x, y=y)

# Inicialização da janela
root.mainloop()