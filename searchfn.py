#!C:\Program Files\Ampps\Python\Python.exe 
import cgi, cgitb 
# HTML
print("Content-type: text/html\n\n")
print("<html><head>")
print("<style>")
print("body {margin: 0;font-family: Arial, Helvetica, sans-serif;}")
print(".topnav {overflow: hidden;background-color: #A9A9A9; height: 90px;}")
print(".topnav a {color: white;text-align: center;padding: 20px 20px;text-decoration: none;font-size: 20px;padding-bottom: 10px;}")
print(".topnav a:hover {background-color: grey;color: black;}")
print(".topnav a.active {background-color: ;color: white;}")
print(".Logo{width: 35px;height: 45px;}")
print(".ImageLogo{width: 90px;height: 70px;padding:15px;}")
print("td,th {border: 1px solid rgb(190, 190, 190);padding: 10px;}")
print("td {text-align: center;}")
print("tr:nth-child(even) {background-color: #eeeeee;}")
print("table {text-align: center; margin: 0 Auto;border-collapse: collapse;border: 2px solid rgb(200, 200, 200);letter-spacing: 1px;font-family: Verdana;font-size: .8rem;}")
print(".Result {text-align: center; margin: 0 Auto;font-family: Arial, Helvetica, sans-serif;}")
print("</style>")
print("</head>")
print("<body>")


print("<div class='topnav'>")
print("<div class='Logo'><img src='/images/judo.jpg' class='ImageLogo'></div>")
print("<center>")
print("<div>")
print ("<a class='active' href='list.py'>List</a>")
print ("<a href='searchdb.py'>Search</a>")
print ("<a href='adddb.py'>Add</a>")
print ("<a href='editdb'>Edit</a>")
print ("<a href='deletedb'>Delete</a>")

print("</center>")
print("</div>")
print("</div>")

print ("<div class = 'result'>")
#print ("Welcome to my Home page")
form = cgi.FieldStorage() 
MemID = form.getvalue('MemberID')
#print (MemID)
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="judoclub"
)
# Cursor is Another name Recordset 
mycursor = mydb.cursor()
SqlStr = "Select * from Memberlist where MemberID = " + MemID
#print (SqlStr)
mycursor.execute(SqlStr)

myresult = mycursor.fetchall()
print ("<table>")
print ("<Tr>")
print ("<th>ID</th>")
print ("<th>First Name</th>")
print ("<th>Last Name</th>")
print ("<th>Date of Birth </th>")
print ("<th>Belt Rank</th>")
for x in myresult:
	print ("<Tr>")
	print ("<td>")
	print (x[0])
	print ("</Td>")
	print ("<td>")
	print (x[1])
	print ("</Td>")
	print ("<td>")
	print (x[2])
	print ("</Td>")
	print ("<td>")
	print (x[3])
	print ("</Td>")
	print ("<td>")
	print (x[4])
	print ("</Td>")
	print ("</Tr>")
	
    
	
print ("</Table>")

print ("</div>")
print ("</body>")
print ("</html>")