import requests
import json
import mysql.connector
import sys
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database=' entitiesdb')
except mysql.connector.Error as e:
    sys.exit("db connection error")
mycursor=mydb.cursor()        
data=requests.get("https://api.publicapis.org/entries").text
data_info=json.loads(data)
print(data_info)

datainf=data_info["entries"]
for i in datainf:
    https=str(i['HTTPS'])
    sql="INSERT INTO `entities`(`api`, `Description`, `Auth`, `HTTPS`, `Cors`, `Link`, `Category`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    #sql="INSERT INTO `entities`(`api`, `Description`, `Auth`, `HTTPS`, `Cors`, `Link`, `Category`) VALUES (%s,%s,%s,%s,%s,%s,%s)
    #sql="INSERT INTO `entities`(`api`, `Description`, `Auth`, `HTTPS`, `Cors`, `Link`, `Category`) VALUES ('"+i['API']+"','"+i['Description']+"','"+i['Auth']+"','"+https+"','"+i['Cors']+"','"+i['Link']+"','"+i['Category']+"')"
    data=(i['API'],i['Description'],i['Auth'],i['HTTPS'],i['Cors'],i['Link'],i['Category'])
    mycursor.execute(sql,data)
    mydb.commit()
    print("data inserted success",i['API'])

