from asyncio.windows_events import NULL
from flask import Flask, render_template, request
import sqlite3

app=Flask(__name__)

@app.route('/')
@app.route('/index')

def homepage():
    return render_template('index.html')

@app.route('/display', methods=['POST','GET'])
def index():
    rows = list()
    if request.method=="POST":
        a=request.form.get('Customername')
        b=request.form.get('Job')
        # c=request.form.get('BName')
        c= "BName"
        d=request.form.get('tname')
        e=request.form.get('CType')
        f=request.form.get('State')
        g=request.form.get('Tenure')
        h=request.form.get('Goals')
        i=request.form.get('Service')
        j=request.form.get('Product')
        # return render_template('display.html', Customername=a, Job=b, BName=c, tname=d, CType=e, State=f, Tenure=g, Goals=h, Service=i, Product=j)

        try:  
            with sqlite3.connect("customer.db") as con:
                print("Connected")    
                cur = con.cursor()  
                print("Got cursor")  
                cur.execute("INSERT into Registration (Customername, Job, BName,tname,CType,State,Tenure,Goals,Service,Product) values (?,?,?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h,i,j))  
                print("executed successfully")  
                con.commit()  
                print("Customer successfully Added")  
                
                cur.execute("select * from Registration")  
                rows = cur.fetchall()
                print(rows)  
        except Exception as e:   
            con.rollback()
            print(e)  
            print("We can not add the customer to the list" ) 
        finally:  
            
            return render_template("display.html",rows = rows) 
            con.close() 

    if __name__=='__main__':
        app.run(debug=True)
