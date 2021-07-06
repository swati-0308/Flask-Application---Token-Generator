from flask import Flask, render_template, request
from flask_mysqldb import MySQL,MySQLdb
import random
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yaml'),Loader=yaml.FullLoader)

app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	random_number=random.randint(1,100)
	if request.method == 'POST':
		userDetails = request.form
		customer_id = userDetails['cid']
		#random_number=randint(1,100)
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users (customer_id,token) VALUES(%s,%s)",(customer_id, random_number))
		mysql.connection.commit()
		cur.close()
	return render_template("index.html",random_number=random_number)

if __name__ == '__main__':
	app.run(debug=True)
