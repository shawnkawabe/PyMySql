# ----- import modules ------
from datac import *
from About import *
from Login import *
# ----------------------------
# -----   import packages  ------
from tkinter import *
from tkinter import scrolledtext
import pymysql
import pymysql.cursors
import ctypes
# -------------------------------
def getname():
    named = nt.get()
    name = named
    #      --------- Conexão MYSQL--------------
    #db1data(name)
    #       --------- Fim de Conexão ----------
         
    ctypes.windll.user32.MessageBoxW(0, "Inicie suas atividades agora mesmo.", "Bem vindo á "+name+".", 0)
    
    home(name)
    
    
#-------   HOME   -------
def home(name):
    
    
    home = Tk()
    home.title("Home")
    home.geometry('800x600')

    vd = Label(home,text="Welcome\nto\n"+name+"",font=('Consolas',45),fg="#483D8B",bg="#1f1f2e" )
    vd.place(x=300,y=150)

    menu = Menu(home)
    fmenu = Menu(menu,background='#1f1f2e',font=('Consolas',12),fg='#483D8B')
    menu.add_cascade(label='Main Menu', menu=fmenu)
    fmenu.add_command(label='Login', command=logwd)
    fmenu.add_command(label='About',command=About)
    fmenu.add_command(label='Contact',command=Contact)


    #fmenu.add_separator()
    home.config(menu=menu,background='#1f1f2e')
    home.mainloop()
    init.quit()
#    -------  START   -------    

init = Tk()
init.title("Digite o nome do sistema")
init.geometry('300x100')
nt = Entry(init,font=('Consolas',10),width=25,fg='#1f1f2e')
btn_n = Button(init,text='Entrar',font=('Consolas',10), command=getname)
label = Label(init,text='Digite o nome do sistema',font=('Consolas',10),fg='#c2c6c9',background='#44475A')
btn_n.config(fg="#6272A4", bg="#282A36")
btn_n.place(x=125,y=60)
nt.place(x=60,y=30)
label.place(x=65,y=10)
init.config(background='#44475A')
init.mainloop()


if __name__== "__main__":
    init.mainloop()