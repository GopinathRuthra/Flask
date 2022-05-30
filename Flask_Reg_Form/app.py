from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
@app.route('/index')

def homepage():
    return render_template('index.html')

@app.route('/display.html', methods=['POST','GET'])
def index():
    if request.method=="POST":
        a=request.form.get('Customername')
        b=request.form.get('Job')
        c=request.form.get('BName')
        d=request.form.get('tname')
        e=request.form.get('CType')
        f=request.form.get('State')
        g=request.form.get('Tenure')
        h=request.form.get('Goals')
        i=request.form.get('Service')
        j=request.form.get('Product')
        return render_template('display.html', Customername=a, Job=b, BName=c, tname=d, CType=e, State=f, Tenure=g, Goals=h, Service=i, Product=j)

    if __name__=='__main__':
        app.run(debug=True)
