import psycopg2
# con = psycopg2.connect(user="postgres", database="dvdrental", password=2299, host="localhost", port=5432)
# cur = con.cursor()
# sql_query = "select * from table1"
# cur.execute(sql_query)
# # con.commit()
# y = cur.fetchall()
# print(y)
# cur.close()
# con.close()



# id = input("enter id:")
# country = input("enter country:")
# try:
#     con = psycopg2.connect(user="postgres", database="dvdrental", password=2299, host="localhost", port=5432)
#     cur = con.cursor()
#     sql_query = "update table1 set country = %s where id = %s"
#     cur.execute(sql_query, (country, id))
#     con.commit()
#     sql_query1 = "select * from table1"
#     cur.execute(sql_query1)
#     print(cur.fetchall())
#
# except(Exception,psycopg2.Error) as error:
#     print("find the error:",error)
# finally:
#     cur.close()
#     con.close()



