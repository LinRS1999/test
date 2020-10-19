import pymysql


conn = pymysql.connect(
            host='localhost',
            user='root',
            password='623156869',
            database='test',
        )

cursor = conn.cursor()

# in_time = self.time_to_int(self.in_time)
# out_time = self.time_to_int(self.out_time)
# type = self.room_type

sql = 'insert into roomtable values (%s, %s, %s, %s, %s, %s) '

try:
    cursor.execute(sql, ('hsw', 103, 1, 20201010, 20201013, 240))
    conn.commit()
    # print(result)
except:
    print('error')

conn.close()
