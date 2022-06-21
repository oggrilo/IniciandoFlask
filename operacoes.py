import mysql.connector
import conexaoBD

db_connection = conexaoBD.conexao()#abrir a conexão
con = db_connection.cursor()#acesso ao banco (insert,update, release)

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "Insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, dataDeNascimento)
        con.execute(sql)
        db_connection.commit()#"crtl + enter do banco de dados"
        return con.rowcount , "Inserido!"
    except Exception as erro:
        return erro

def consultar():
    try:

    except Exception as erro:
        return erro