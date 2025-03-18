from customtkinter import *

tela = CTk()
tela._set_appearance_mode('light')
tela.title('Login')
tela.geometry("350x400")
tela.resizable(False, False) # impossibilita redimensionar a tela
tela.iconbitmap('login.ico') # mudar o icone do titulo da tela

frame_1 = CTkFrame(tela, width=300, height=360, fg_color='gray', bg_color='white')
frame_1.place(x=25, y=20)

frame_2 = CTkFrame(frame_1, width=280, height=20, fg_color='white', bg_color='gray')
frame_2.place(x=10, y=10)

frame_3 = CTkFrame(frame_1, width=140, height=310, fg_color='white', bg_color='gray')
frame_3.place(x=10, y=38)

label_na_frame2 = CTkLabel(frame_2, text='Curso Custom Tkinter', text_color='black', font=('SF Pro Display', 13))
label_na_frame2.place(relx=0.50, rely=0.50, anchor=CENTER)

frame_4 = CTkFrame(frame_1, width=140, height=140, fg_color='white', bg_color='gray')
frame_4.place(x=155, y=38)
tela.mainloop()