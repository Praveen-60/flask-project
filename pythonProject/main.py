from flask import *
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']=""
app.config['MYSQL_DB']="library"
app.config['MYSQL_CURSORCLASS']="DictCursor"
mysql=MySQL(app)
@app.route('/sig')
def sec():
    return render_template('dash.html')
@app.route('/log')
def fun():
    return render_template('login.html')
@app.route('/')
def home():
    return render_template('login.html')
@app.route('/login')
def logout():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/au')
def au():
    return render_template('adduser.html')
#edit user
@app.route('/eu/<string:id>',methods=['GET','POST'])
def edituser(id):
    con = mysql.connection.cursor()
    con.execute("select * from user where user_id=%s",[id])
    r=con.fetchone()
    con.close()
    return render_template('edituser.html',id=r)
@app.route('/ab')
def ab():
    return render_template('addbooks.html')
@app.route('/eb/<string:id>',methods=['GET','POST'])
def editbooks(id):
    con = mysql.connection.cursor()
    con.execute("select * from book where book_id=%s",[id])
    r=con.fetchone()
    con.close()
    return render_template('editbooks.html',id=r)
@app.route('/ei/<string:id>',methods=['GET','POST'])
def editissues(id):
    con = mysql.connection.cursor()
    con.execute("select * from issues where issue_id=%s",[id])
    r=con.fetchone()
    con.close()
    return render_template('editissues.html',id=r)
@app.route('/ai')
def ai():
    return render_template('addissues.html')
@app.route('/at')
def at():
    return render_template('addtransaction.html')

@app.route('/et/<string:id>',methods=['GET','POST'])
def edittransactions(id):
    con = mysql.connection.cursor()
    con.execute("select * from transactions where transaction_id=%s",[id])
    r=con.fetchone()
    con.close()
    return render_template('edittransaction.html',id=r)

@app.route('/dash')
def dash():
    con =mysql.connection.cursor()
    con.execute("select * from user;")
    r = len(con.fetchall())
    con.execute("select * from book;")
    v = len(con.fetchall())
    con.execute("select * from issues")
    s= len(con.fetchall())
    con.close()
    return render_template('dash.html',data=r,data1=v,data2=s)
@app.route('/user')
def user():
    con = mysql.connection.cursor()
    con.execute("select * from user;")
    r = con.fetchall()
    con.close()
    return render_template('user.html',data=r)
@app.route('/book')
def book():
    con = mysql.connection.cursor()
    con.execute("select * from book;")
    r = con.fetchall()
    con.close()
    return render_template('books.html',data=r)
@app.route('/transactions')
def trans():
    con = mysql.connection.cursor()
    con.execute("select * from transactions;")
    r = con.fetchall()
    con.close()
    return render_template('transaction.html',data=r)
@app.route('/issuebook')
def issue():
    con = mysql.connection.cursor()
    con.execute("select * from issues;")
    r = con.fetchall()
    con.close()
    return render_template('issues.html',data=r)
#LOGIN PROCESS
@app.route('/ulogin',methods=['GET','POST'])
def ulogin():
    if request.method=="POST":
        uname=request.form['Uname']
        pas=request.form['Pass']
        con = mysql.connection.cursor()
        con.execute("select * from user where user_name=%s and password=%s;",[uname,pas])
        r = len(con.fetchall())
        con.close()
        if r==1:
            return redirect(url_for('dash'))
        else:
            flash("Invalid user_name or password")
            return redirect(url_for('home'))
#delete user
@app.route('/deleteuser/<string:id>',methods=['GET','POST'])
def deleteuser(id):
    con=mysql.connection.cursor()
    con.execute("delete from user where user_id = %s;",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('user'))
#delete books
@app.route('/deletebook/<string:id>',methods=['GET','POST'])
def deletebook(id):
    con=mysql.connection.cursor()
    con.execute("delete from book where book_id=%s;",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('book'))
#delete issuesbooks
@app.route('/deleteissues/<string:id>',methods=['GET','POST'])
def deleteissues(id):
    con=mysql.connection.cursor()
    con.execute("delete from issues where issue_id=%s;",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('issue'))
#delete transactions
@app.route('/deletetransactions/<string:id>',methods=['GET','POST'])
def deletetransactions(id):
    con = mysql.connection.cursor()
    con.execute("delete from transactions where transaction_id=%s;",[id])
    mysql.connection.commit()
    con.close()
    return redirect(url_for('trans'))
#Add user
@app.route('/adduser',methods=['GET','POST'])
def adduser():
    if request.method=="POST":
        id = request.form['id']
        name = request.form['name']
        email=request.form['email']
        pas=request.form['password']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO user(user_id,user_name,user_mail,password) values (%s,%s,%s,%s);",(id,name,email,pas))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))

@app.route('/addbooks', methods=['GET', 'POST'])
def addbooks():
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        pas = request.form['password']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO book(book_id,book_name,author,quantity) values (%s,%s,%s,%s);",(id, name, email, pas))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))

@app.route('/addissues', methods=['GET','POST'])
def addissues():
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        mail = request.form['mail']
        idate = request.form['idate']
        edate = request.form['edate']
        expdate = request.form['expdate']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO issues(issue_id,user_name,book_name,issue_date,exp_return_date,return_date) values (%s,%s,%s,%s,%s,%s);",(id,name,mail,idate,edate,expdate))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))

@app.route('/addtransaction', methods=['GET', 'POST'])
def addtransaction():
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        due = request.form['due']
        status = request.form['status']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO transactions(transaction_id,user_name,book_name,due,status) values (%s,%s,%s,%s,%s);",(id, name, email, due,status))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))
#update user
@app.route('/updateuser',methods=['GET','POST'])
def updateuser():
    if request.method=="POST":
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        pas = request.form['password']
        con = mysql.connection.cursor()
        con.execute("update user set user_id=%s,user_name=%s,user_mail=%s,password=%s where user_id=%s;",(id,name,email,pas,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('user'))
#update books
@app.route('/updatebook',methods=['GET','POST'])
def updatebook():
    if request.method=="POST":
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        pas = request.form['password']
        con = mysql.connection.cursor()
        con.execute("update book set book_id=%s,book_name=%s,author=%s,quantity=%s where book_id=%s;",(id,name,email,pas,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('book'))
#update issues
@app.route('/updateissues',methods=['GET','POST'])
def updateissues():
    if request.method=="POST":
        id = request.form['id']
        name = request.form['uname']
        mail = request.form['bname']
        idate = request.form['idate']
        edate = request.form['edate']
        expdate = request.form['rdate']
        con = mysql.connection.cursor()
        con.execute("update issues set issue_id=%s,user_name=%s,book_name=%s,issue_date=%s,exp_return_date=%s,return_date=%s where issue_id=%s;",(id,name,mail,idate,edate,expdate,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('issue'))
#update transaction
@app.route('/updatetransactions',methods=['GET','POST'])
def updatetransactions():
    if request.method=="POST":
        id = request.form['id']
        uname = request.form['uname']
        bname = request.form['bname']
        due = request.form['due']
        status = request.form['status']
        con = mysql.connection.cursor()
        con.execute("update transactions set transaction_id=%s,user_name=%s,book_name=%s,due=%s,status=%s where transaction_id=%s;",(id,uname,bname,due,status,id))
        mysql.connection.commit()
        con.close()
        return redirect(url_for('trans'))

if __name__=='__main__':
    app.secret_key="a123r"
    app.run(debug=True)