#! C:\Users\Dhanush\AppData\Local\Programs\Python\Python37\python.exe


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/utype")
def utype():
   if request.method == 'POST':
    	result = request.form['log']
    	return "aaa"
    	#if result=="Consumer" :
    	##lif result=="Cultivator" :
    	#	return render_template("result1.html",result = "dhanushR!")



if __name__ == '__main__':
   app.run(debug = True)


import paho.mqtt.client as mqtt
import psycopg2
import json
import csv
  

connection = psycopg2.connect(user = "postgres",
                                  password = "dhanu26",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "AgriDB")
# Callback Function on Connection with MQTT Server
cursor = connection.cursor()
    # Print PostgreSQL Connection properties
print ( connection.get_dsn_parameters(),"\n")

try:
  	print(" INSERT INTO devices("+c1+") VALUES("+c2+")")
  	cursor.execute("SELECT * from Consumer")
  	rows = cursor.fetchall()
  	
  	connection.commit()
  	
  except (Exception, psycopg2.Error) as error :
    pass
  else:
    	print("done1")
    	#cursor.execute("SELECT SUM(temp1),SUM(temp2) FROM easy")
    	#print("done2")
    	#print(cursor.fetchall())
    	print("done3")
  