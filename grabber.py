#LAB1 Python starter code
#Based upon manual at http://mysql-python.sourceforge.net/MySQLdb.html

#imports go here
#import MySQLdb
import _mysql

#code goes here

db = _mysql.connect(host="localhost",user="root",passwd="cyberpower550",db="ian")
db.query("""SELECT * FROM Music;""")
r = db.store_result()
nR = r.num_rows()
while(nR > 0):
	print(r.fetch_row())
	nR = nR - 1
db.close()