import pymysql
import pymysql.cursors

# ----------------  Create 1º usuário (admin) -------------

def db1data(name):
    eadmin = "admin@"+name+".com"
    #      --------- Conexão MYSQL--------------
    con = pymysql.connect(db='projectpy',user='',passwd='')
    cursor = con.cursor()
    sql = "INSERT INTO `accounts` (`username`, `password`, `email`) VALUES ('admin', 'admin', %s )"
    cursor.execute(sql,(eadmin))
    con.commit()
    con.close()
    #       --------- Fim de Conexão ----------
def db2data():
    # ----------------- CONSULTA DE DADOS --------------------
    con =  pymysql.connect(db='projectpy',user='',passwd='')
    cursor = con.cursor()
    cursor.execute("SELECT passw FROM USUARIOS WHERE name = %s"%(log))
    r = cursor.fetchall()
    n =  r[0]
    if pas == n:
        cond = True
    elif pas != n:
        cond = False
    #Call da próxima função menu.  
    