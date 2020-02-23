from tkinter import *
# ---------- ABOUT WINDOW -----------    

def About():
        
    ab =  Tk()
    ab.title("About this project")
    ab.geometry('800x600')
    lbl = Label(ab,text="Projeto feito apenas para fins acadêmicos;\nQualquer uso é de responsabilidade do usuário;\nCaso use e tenha algum problema contribua com o projeto e o aprimore;\nGLHF;")
    lbl.configure(font=('Consolas',14),fg='#50fa7b',bg='#44475A')
    ab.config(bg='#44475A')
    lbl.place(x=60,y=100)
    ab.mainloop()
    
# ---------- Contact WINDOW -----------  
def Contact():
    
    ab =  Tk()
    ab.title("About this project")
    ab.geometry('800x600')
    lbl = Label(ab,text="github.com/shawnkawabe\nshawn kawabe")
    lbl.configure(font=('Consolas',14),fg='#50fa7b',bg='#44475A')
    ab.config(bg='#44475A')
    lbl.place(x=300,y=100)
    ab.mainloop()
