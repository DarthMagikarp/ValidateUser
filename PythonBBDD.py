import pymysql

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
            sql = 'select * from encuestas  where id = {} limit 10'.format(id)

            try:
                self.cursor.execute(sql)
                user = self.cursor.fetchone()

                print("id", user[0])
                print("sessionCode", user[1])
                print("name", user[2])

            except Exception as e:
                print("no está");

database = DataBase()
database.selecttop(1)