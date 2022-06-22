from aem import Query
import numpy as np
import pandas as pd
import mysql.connector

import time
import yahoo_fin.stock_info as si


def price_getter(stock):
    price = si.get_live_price(stock)
    price_f = "{:,.5f}".format(price)
    price = float(price)
    return price, stock


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'sys12345',
    database = 'Asset_Prices'
)

mycursor = mydb.cursor()

def store_sql(stock):
    data = price_getter(stock)
    data = data[0]
    Stock_name = str(stock)
    timestamp = time.strftime("%H:%M:%S")
    Stock_price_date = time.strftime("%Y-%m-%d") 
    Query = "INSERT INTO Asset_Price (Asset_Name, Price, Time, Date) VALUES (%s, %s, %s, %s)"
    entrys = (Stock_name, data, timestamp, Stock_price_date)
    mycursor.execute(Query, entrys)
    mydb.commit()    
    print (timestamp)



x = 100000



# while x > 0:
#     store_sql("STRAX-USD")
#     x = x - 1
#     time.sleep(1)


if mydb.is_connected():
    print('Connected to MySQL database')
else:
    print('Error connecting to MySQL database')




def store_csv(data, filename):
    data = pd.DataFrame(data)
    data.to_csv(filename, index=False, header=False)





