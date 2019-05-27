

# import datetime #获取当前日期
# from datetime import datetime
# now = datetime.now() # 获取当前datetime
# print(now)
# print(type(now))

#指定日期
# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
# print(dt)


from datetime import datetime
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt.timestamp()) # 把datetime转换为timestamp

from datetime import datetime
t = 11162941700
print(datetime.fromtimestamp(t))


from datetime import datetime
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间
print(datetime.utcfromtimestamp(t)) # UTC时间

# str转换为datetime
from datetime import datetime
cday = datetime.strptime('2015?6?1 18.19.59', '%Y?%m?%d %H.%M.%S')
print(cday)
print(type(cday))

# datetime转换为str
from datetime import datetime
now = datetime.now()
now = now.strftime('%A %B %Y %H:%M:%S')
print(now)
print(type(now))





#计算两个时间差
from datetime import datetime
time1 = datetime(2016, 10, 20, 10,10)
time2 = datetime(2015, 11, 2, 10,40)
print(time2-time1)

#转化日期为星期几
from datetime import datetime
dayOfWeek = datetime.now().isoweekday()
print(dayOfWeek)



