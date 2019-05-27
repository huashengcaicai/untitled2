import pymysql
import xlrd


db = pymysql.connect(host='db.stg.helijia.com', user='hljtest_dev',
                     passwd='hljtest_dev123456',
                     db='hlj',
                     port=6006,
                     charset='utf8')

def call(m,n):
    if book.cell(m,n).value == "":
        return 0
    else:
        return book.cell(m,n).value
def search_count():
    cursor = db.cursor()
    select = 'select count(id) from save'  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line_count = cursor.fetchall()
    print(line_count[0])

if __name__ == '__main__':
    search_count()



def open_excel():
    try:
        book = xlrd.open_workbook(
           'D:/Users/pwjnew/Desktop/xinde.xlsx')  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("0308所有接口QPS")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")





def insert_deta():
    sheet = open_excel()
    cursor = db.cursor()
    row_num = sheet.nrows

    for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        row_data = sheet.row_values(i)
        value = (row_data[0], row_data[1], row_data[2], row_data[3], row_data[4],row_data[5],row_data[6],row_data[7],row_data[8],row_data[9],row_data[10],row_data[11])
        # print(i)
        # print(row_data)
        print(value)



        sql = 'INSERT INTO save(instance_name,max190311,exp_190311,' \
              'exp_190311_single,max181111,max180919,max180515,max180311,' \
              'max171111,max170923,max170515,max170311)VALUES(%s,%s,%s,%s,' \
              '%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,value)  # 执行sql语句
        db.commit()
        print(sql)


    cursor.close()  # 关

if __name__ == '__main__':
    insert_deta()


