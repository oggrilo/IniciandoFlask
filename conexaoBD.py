import mysql.connector
from mysql.connector import errorcode

def conexao():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='',database='cadastroFlask')
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print(" Banco de Dados Inexistente :/ ")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" Nome de Usuário ou senha errados! ")
        else:
            print(error)
    else:
        db_connection.close()