import sys
import copy
import pymysql
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

room1 = [101, 102, 103, 80]
room2 = [201, 202, 203, 140]
room3 = [301, 302, 303, 200]

class query(QWidget):
    def __init__(self, temp1, temp2, temp3, temp4):
        super().__init__()
        self.setWindowTitle('客房查询结果')
        self.resize(450, 400)
        self.vbox = QVBoxLayout()
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.hbox = QHBoxLayout()
        self.tabelwidget = QTableWidget()
        self.room_type = copy.deepcopy(temp1)
        self.day = copy.deepcopy(temp2)
        self.in_time = copy.deepcopy(temp3)
        self.out_time = copy.deepcopy(temp4)
        self.room_list, self.price = self.querysql()
        self.initUI()

    def initUI(self):

        self.tabelwidget.setRowCount(len(self.room_list))
        self.tabelwidget.setColumnCount(3)
        self.tabelwidget.setHorizontalHeaderLabels(['房间号', '房间类型', '房间价格'])

        for i in range(len(self.room_list)):
            for j in range(3):
                if j == 0:
                    temp = QTableWidgetItem(str(self.room_list[i]))
                elif j == 1:
                    temp = QTableWidgetItem(str(self.room_type))
                else:
                    temp = QTableWidgetItem(str(self.price))
                temp.setTextAlignment(Qt.AlignCenter)
                self.tabelwidget.setItem(i, j, temp)
        self.tabelwidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabelwidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabelwidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabelwidget.verticalHeader().setVisible(False)
        self.hbox.addWidget(self.tabelwidget)
        self.widget1.setLayout(self.hbox)
        self.vbox.addWidget(self.widget1)

        room_num_list = []
        for i in range(len(self.room_list)):
            room_num_list.append(self.tabelwidget.item(i, 0).text())

        self.combo = QComboBox()
        for item in room_num_list:
            self.combo.addItem(item)

        self.form1 = QFormLayout()
        self.form1.addRow('请选择房间号：', self.combo)

        self.widget2 = QWidget()
        self.widget2.setLayout(self.form1)
        self.vbox.addWidget(self.widget2)

        self.lineEdit = QLineEdit()

        self.form2 = QFormLayout()
        self.form2.addRow('请输入您的姓名：', self.lineEdit)
        self.widget3 = QWidget()
        self.widget3.setLayout(self.form2)
        self.vbox.addWidget(self.widget3)

        self.button = QPushButton('提交订单')
        self.vbox.addWidget(self.button)
        self.button.clicked.connect(self.submit)

        self.setLayout(self.vbox)


    def submit(self):
        name = self.lineEdit.text()
        room = self.combo.currentText()
        str1 = '订购房间号为：' + self.combo.currentText() + '\n入住时间为：' + self.in_time +\
               '\n退房时间为：' + self.out_time + '\n入住天数为：' + str(self.day) + '\n总房费为：' + str(self.price * self.day)
        reply = QMessageBox.question(self, '确认订单', str1, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            flag = self.insertsql(name, room)
            if flag > 0:
                QMessageBox.about(self, ' ', '订房成功！')
            else:
                QMessageBox.about(self, ' ', '订房失败！')

    def querysql(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='623156869',
            database='test',
        )
        cursor = conn.cursor()
        in_time = self.time_to_int(self.in_time)
        type = self.room_type
        sql = 'select * from roomtable where in_time <= %d and out_time >= %d and room_type = %d'
        try:
            cursor.execute(sql % (in_time, in_time, type))
            result = cursor.fetchall()
        except:
            print('error')
        conn.close()

        temp = []
        for item in result:
            temp.append(item[1])
        room_list = []
        if type == 1:
            for i in range(3):
                if room1[i] not in temp:
                    room_list.append(room1[i])
            return room_list, room1[3]
        elif type == 2:
            for i in range(3):
                if room2[i] not in temp:
                    room_list.append(room2[i])
            return room_list, room2[3]
        else:
            for i in range(3):
                if room3[i] not in temp:
                    room_list.append(room3[i])
            return room_list, room3[3]


    def time_to_int(self, string):
        temp = string.replace('.', '')
        print(int(temp))
        return int(temp)


    def insertsql(self, name, room):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='623156869',
            database='test',
        )
        cursor = conn.cursor()
        in_time = self.time_to_int(self.in_time)
        out_time = self.time_to_int(self.out_time)
        type = self.room_type
        price = self.price * self.day
        sql = 'insert into roomtable values (%s, %s, %s, %s, %s, %s) '
        try:
            cursor.execute(sql, (name, room, type, in_time, out_time, price))
            conn.commit()
        except:
            print('error')
        conn.close()
        return cursor.rowcount




