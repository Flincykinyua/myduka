import psycopg2

conn=psycopg2.connect(user="postgres", host="localhost" ,ports="5432", password="flincy" , database="")

cur = conn.cursor()
print("[+] Database connected successfull")

query="select * from products ;"
cur.execute(query)
products=cur.fetchall()
print(products)


query ='select * from sales ;'
cur.execute(query)
sales=cur.fetchall()
print(sales)

def fetch_data(table_name):
    query=f"select * from {table_name}"
    cur.execute(query)
    data=cur.fetchall()
    return(data)

z=fetch_data("products")
print(z)

query="insert into products(name,buying_price,selling_price,stock_quantity)values('lemon',100,200,50);"
cur.execute(query)
conn.commit()

products=fetch_data("products")
print(products)