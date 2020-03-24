from flask import Flask, render_template, request
import psycopg2
from psycopg2.extras import RealDictCursor
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('loginusers.html')

@app.route('/utype',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
   		
   		result = request.form
   		if result['log']=="Consumer":
   			return render_template("Consumer.html")
   		elif result['log']=="Cultivator":
   			return render_template("Cultivator.html")
   		elif result['log']=="Labour":
   			return render_template("Labour.html")
   		#elif result['log']=="":
   		#	return render_template("Consumer.html",result = result)
   		#elif result['log']=="Consumer":
   		#	return render_template("Consumer.html",result = result)
   		else:
   			return "aaaaaa"

@app.route('/consumer',methods=['POST','GET'])
def consumer():
	if request.method == 'POST':
		result=request.form
		connection = psycopg2.connect(user = "postgres",
                                  password = "dhanu26",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "AgriDB")
		cursor = connection.cursor()
		sql="INSERT INTO CONSUMER VALUES('"+result['id']+"','"+result['fname']+"','"+result['lname']+"','"+result['phone']+"','"+result['email']+"','"+result['addr']+"','"+result['pass']+"','"+result['uname']+"')"
		cursor.execute(sql)
		connection.commit()
		return render_template("success.html")



@app.route('/cultivator',methods=['POST','GET'])
def cultivator():
  if request.method == 'POST':
    result=request.form
    connection = psycopg2.connect(user = "postgres",
                                  password = "dhanu26",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "AgriDB")
    cursor = connection.cursor()
    sql="INSERT INTO Cultivator VALUES('"+result['id']+"','"+result['name']+"','"+result['email']+"','"+result['aadhar']+"','"+result['phone']+"','"+result['addr']+"','"+result['pass']+"','"+result['uname']+"')"
    cursor.execute(sql)
    connection.commit()
    return render_template("success.html")

@app.route('/login')

def login():
  
  return render_template('login.html')

@app.route('/loginn',methods=['POST','GET'])
def loginn():
  if request.method=='POST':
    result=request.form
    connection = psycopg2.connect(user = "postgres",
                                  password = "dhanu26",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "AgriDB")
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    sql="select * from "+result['log']
    cursor.execute(sql)
    rows=cursor.fetchall()
    sql="select COUNT(*) FROM "+result['log']
    cursor.execute(sql)
    cnt=cursor.fetchall()
    cnt=int(cnt[0]['count'])
    for i in range(0,cnt):
      if rows[i]['username']==result['uname'] and rows[i]['password']==result['pass']:
        web=result['log']+"l.html"
        if result['log']=='Cultivator':
          sql="select harvest_id,crop_id,name,from_date,land_id,processor_id from harvest natural join crop natural join land_crop where cultivator_id="+str(rows[i]['cultivator_id'])+" and to_date is NULL"
          cursor.execute(sql)
          r=cursor.fetchall()
          cursor.execute("select count(*) from ("+sql+") as Count")
          n=cursor.fetchall()
          n=int(n[0]['count'])
        return render_template(web,row=rows[i],r=r,n=n)

    return render_template('failure.html',cnt=cnt)

    


if __name__ == '__main__':
   app.run(host="localhost",port=5000, debug = True)