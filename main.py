from flask import Flask,render_template,request,redirect,session
from database import  curr

# flask name initiates app- class obj
app = Flask(__name__)

# A decorator function is used to give a funcion or route more functionality. It runs before the 
# route function is processed
def login_required(f):
    @wraps(f)
    def protected():
        return redirect("/login")
    return protected


# Define a custom filter- this will be used to format the date
@app.template_filter('strftime')
def format_datetime(value, format="%B %d, %Y"):
    return value.strftime(format)


@app.route("/home")
def index():
    name="Friend"
    return render_template("index.html",name=name)

@app.route("/navbar")
def navb():
   
    return render_template("navbar.html")

@app.route("/about")
def about():
    return "About page info is supposed to be displayed on this route"

@app.route("/dashboard")
@login_required
def dashboardfunc():
    cur.execute("SELECT sum (p.selling_price * s.quantity) as sales, s.created_at from sales as s join products as p on p.id=s.pid GROUP BY created_at ORDER BY created_at;")
    daily_sales=cur.fetchall()
   # print(daily_sales)
    x=[]
    y=[]
    for i in daily_sales:
        x.append(i[1].strftime("%B %d, %Y"))
        y.append(float(i[0]))
        
    # list comprehension
    #lx = [i[1].strftime("%B %d, %Y") for i in daily_sales]
    #ly = [i[0] for i in daily_sales]

    #append happens because it is inside a list
    #you can also add an if statement
    #lx = [i[1].strftime("%B %d, %Y") for i in daily_sales if float(i[0])>60000]

    cur.execute("SELECT sum (p.selling_price * s.quantity) as Profit, p.name from products as p join sales as s on p.id=s.pid GROUP BY p.name ORDER BY profit desc;")
    profit_per_product=cur.fetchall()
    p=[]
    q=[]

    for z in profit_per_product:
        p.append(z[1])
        q.append(z[0])





