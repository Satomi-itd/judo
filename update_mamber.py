#!C:\Program Files\Ampps\Python\Python.exe
import cgi
import mysql.connector

# HTMLヘッダ
print("Content-type: text/html\n\n")
print("<html><head><title>Update Member</title></head><body>")

# フォームデータの取得
form = cgi.FieldStorage()
VID = form.getvalue('id')
VFName = form.getvalue('firstname')
VLName = form.getvalue('lastname')
VRank = form.getvalue('level')

# 入力データの確認
if not VID or not VFName or not VLName or not VRank:
    print("<p>Missing data, please fill out all fields!</p>")
else:
    # MySQL接続
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="judoclub"
    )

    # SQLインジェクション防止のためパラメータ化クエリを使用
    mycursor = mydb.cursor()
    update_query = "UPDATE memberlist SET firstname = %s, lastname = %s, level = %s WHERE id = %s"
    mycursor.execute(update_query, (VFName, VLName, VRank, VID))
    mydb.commit()

    print(f"<h2>Member {VID} updated successfully!</h2>")

print("</body></html>")
