# 计算生日是星期几
import datetime
def get_birthday_weekday(birthday_str):
    # 构建一个列表，存储周一至周日
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # 实例化一个datetime对象，并指定日期的格式
    birthday = datetime.datetime.strptime(birthday_str,'%Y-%m-%d')
    print(type(birthday))
    # 通过datetime中的weekday方法来获取下标(0,1,2,3,4,5,6)
    num = birthday.weekday()
    print(num)
    print(20190201)
    print(weekdays[num])
    # 根据传入的日期和weekdays列表的下标来获取是星期几
    print('your birthday {0} is {1}'.format(birthday_str,weekdays[num]))

gf_birthday='2019-2-18'
bf_birthday='2019-3-29'
get_birthday_weekday(gf_birthday)
get_birthday_weekday(bf_birthday)