import pymysql
#链接数据库，并创建游标
conn = pymysql.connect(host='47.98.147.125',port=3308,user='root',passwd='123456',db='api_test1')
#创建游标，通过游标去执行sql
cur = conn.cursor()
#把输出的格式转换成
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
cur.execute('create table t1(id INT(10),name VARCHAR(20))ENGINE=InnoDB DEFAULT CHARSET=utf8')

cur.execute('insert into t1(id,name) VALUES (1001,"madaqiang")')
#count = cur.executemany('insert into t1(id,name ) VALUES (%s,%s)',[(1002,'eric'),(1003,'tom')])
cur.execute('select * from t1')
#取出第一条数据
line = cur.fetchone()
print(line)

conn.commit()  #执行
cur.close() #关闭游标
conn.close() #关闭连接
