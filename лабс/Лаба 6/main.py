from peewee import *
import cherrypy
import datetime
#История проездов автомобилей: №, дата и время, номерной знак, марка автомобиля

db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db


class PassHistory(BaseModel):
    class Meta:
        db_table = "PassHistories"
    id = PrimaryKeyField(unique=True)
    number = IntegerField()
    dateTime = DateTimeField()
    plateNumber = CharField(max_length=150)
    carModel = CharField(max_length=150)

db.create_tables([PassHistory])

def Insert(snumber, sdateTime, splateNumber, scarModel):
    PassHistory(
        number = snumber,
        dateTime = sdateTime,
        plateNumber = splateNumber,
        carModel = scarModel
    ).save()

def Update(sid, snumber, sdateTime, splateNumber, scarModel):
    passHistory = PassHistory.get(id=sid)
    passHistory.number = snumber
    passHistory.dateTime = sdateTime
    passHistory.plateNumber = splateNumber
    passHistory.carModel = scarModel
    passHistory.save()

# PassHistory(
#     number=53234,
#     dateTime=datetime.datetime(2015, 10, 9, 23, 55),
#     plateNumber="#53D2F4",
#     carModel="Nisan"
# ).save()

passHistories = PassHistory.select()

class MainPage(object):
    @cherrypy.expose
    def index(self):
        code = f'''
        <html>
            <head>
                <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
                <link rel="stylesheet" href="styles.css">
            </head>
        
            <body>
                <table border="1">
                    <tr>
                        <td>№</td>
                        <td>дата и время</td>
                        <td>номерной знак</td>
                        <td>марка автомобиля</td>
                    </tr>
                    {"".join(["<tr><td>" + str(x.number) + "</td><td>" + str(x.dateTime) + "</td><td>" + str(x.plateNumber) + "</td><td>" + str(x.carModel) + "</td></tr>" for x in passHistories])}
                </table>
           </body>
        </html>
                '''
        return code

#snumber, sdateTime, splateNumber, scarModel
# Insert(1212, datetime.datetime(10, 3, 5, 10, 30), '#53F3ED', 'Пижо')
# Insert(5324, datetime.datetime(15, 5, 23, 23, 14), '#5342А3', 'Нисан')
# Insert(6434, datetime.datetime(4, 12, 23, 15, 20), '#632GD2', 'Таёта')
# Insert(9654, datetime.datetime(30, 1, 12, 14, 20), '#346332', 'Камаз')
Update(3, 0, datetime.datetime(2023, 1, 1, 1, 1), '#000000', 'Ноль')

cherrypy.quickstart(MainPage())