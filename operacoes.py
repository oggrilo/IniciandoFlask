import mysql.connector
import conexaoBD
import this
this.msg = ""

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
        sql = "Select * from pessoa"
        con.execute(sql)

        this.msg = ""
        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            this.msg = this.msg + "Código: {}, Nome: {}, Telefone: {}, Endereço: {}, Data De Nascimento {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
        return this.msg
    except Exception as erro:
        return erro

def consultar(cod):
    try:
        sql = "select * from pessoa where codigo = '{}'".format(cod)
        con.execute(sql)

        this.msg = ""
        this.msg = " Nenhum Dado Encontrado! "
        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            if int(codigo) == int(cod):
                this.msg =  "Código: {}, Nome: {}, Telefone: {}, Endereço: {}, Data De Nascimento {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
                return this.msg
        return this.msg
    except Exception as erro:
        return erro