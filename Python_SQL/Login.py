# -----   import packages  ------
from tkinter import *
import pymysql
import pymysql.cursors
# -------------------------------

def logwd():
    def trylog():
        log ="'"+ Log_name.get()+"'"
        pas = Log_senha.get()
        # ----------------- CONSULTA DE DADOS --------------------
        con =  pymysql.connect(db='projectpy',user='',passwd='')
        cursor = con.cursor()
        cursor.execute("SELECT passwd FROM accounts WHERE username = %s"%(log))
        r = cursor.fetchall()
        n =""
        for i in range(len(r[0][0])):
            n = n+r[0][0][i]
        con.close()
        print(n)
        if pas == n:
            con =  pymysql.connect(db='projectpy',user='',passwd='')
            cursor = con.cursor()
            cursor.execute("SELECT typeu FROM accounts WHERE username = %s"%(log))
            a = cursor.fetchall()
            typeus = ""
            for i in range(len(a[0][0])):
                typeus = typeus+a[0][0][i]
            con.close()
            print(typeus)
            if typeus == "admin":
                #chamada de interface de usuário admin
                print("admin")
            elif typeus == "dft":
                #chamda de interface de usuário padrão
                print("default")      
            
        elif pas != n:
            print()
        
        #Call da próxima função menu.    
            
        
            
        
    loginwd = Tk()
    loginwd.title('Login')
    loginwd.geometry('800x600')
    Log_name = Entry(loginwd,font=('Times',16),width=20)
    Log_senha = Entry(loginwd,font=('Times',16),width=20)

    btn_log = Button(loginwd,font=('Times',16),width=12,text='Login',command = trylog)


    Log_name.place(x=400,y=270,anchor=CENTER)
    Log_senha.place(x=400,y=300,anchor=CENTER)
    btn_log.place(x=400,y=360,anchor=CENTER)

    Log_senha.config(show="*",fg='#483D8B') 
    btn_log.config(bg='#1f1f2e',fg='#483D8B')
    loginwd.config(background='#1f1f2e')
    loginwd.mainloop()   
    

