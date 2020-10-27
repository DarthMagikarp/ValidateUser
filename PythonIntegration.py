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

        def selecttop(self, id):
            sql = 'select * from encuestas  where id = {} limit 1'.format(id)

            try:
                self.cursor.execute(sql)
                user = self.cursor.fetchone()
                print("id", user[0])
                print("sessionCode", user[1])
                print("name", user[2])
                return("True")

            except Exception as e:
                print("no está");
                return("False")


@app.route("/int", methods=['GET', 'POST'])
def welcome() :
        if request.method == 'GET':
            print("ENTRÓ AL GET")
            #reqJson = request.json
            #identificador = reqJson['idPost']
            database = DataBase()
            asd = database.selecttop(1)

            print("asd: ", asd)

            print(request.get_data)

            return asd
        
        elif request.method == 'POST':
            print("ENTRÓ AL POST")
            reqJson = request.json['idPost']
            print(reqJson)
            identificador = reqJson
            print ("erID: "+identificador)

            return 'POST'



if __name__=="__main__" :
    app.run()





    



