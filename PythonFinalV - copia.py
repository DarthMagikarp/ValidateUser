from flask import Flask, request
import pymysql

app = Flask(__name__)

class DataBase:
        def __init__(self):
            self.connection = pymysql.connect(
                host='bhp-database.cud8ycraupgr.sa-east-1.rds.amazonaws.com',
                user='admin',
                password='Enz*ooolico18041986',
                db='bhp_appointments'
            )
            self.cursor = self.connection.cursor()
            print("conexión exitosa")

        def buscaRut(self, rut):
            sql = "select * from encuestas  where rut = '{}' limit 1".format(rut)
            try:
                self.cursor.execute(sql)
                user = self.cursor.fetchone()
                print("id", user[0])
                print("sessionCode", user[1])
                print("name", user[2])
                return("True")
            except Exception as e:
                print("no está")
                return("False")

@app.route("/final", methods=['POST'])
def welcome() :
        database = DataBase()
        identificador = request.json['rut']
        print("req: "+identificador)        
        return database.buscaRut(identificador)

if __name__=="__main__" :
    app.run()




