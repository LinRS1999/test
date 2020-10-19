import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import copy
import pymysql

class refund(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('客房管理系统')
        self.initUI()

    def initUI(self):
        self.vbox = QVBoxLayout()
        self.lineEdit = QLineEdit()
        self.form2 = QFormLayout()
        self.form2.addRow('请输入您的姓名：', self.lineEdit)
        self.widget = QWidget()
        self.widget.setLayout(self.form2)
        self.vbox.addWidget(self.widget)

        self.button = QPushButton('确认退房')
        self.button.clicked.connect(self.delete)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)

    def delete(self):
        reply = QMessageBox.question(self, '确认退房', '你确认要退房吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = pymysql.connect(
                host='localhost',
                user='root',
                password='623156869',
                database='test',
            )
            cursor = conn.cursor()
            name = self.lineEdit.text()
            sql = 'delete from roomtable where cust_name = %s'
            try:
                cursor.execute(sql, name)
                conn.commit()
            except:
                print('error')
            conn.close()
            flag = cursor.rowcount
            if flag > 0:
                QMessageBox.about(self, ' ', '退房成功！')
            else:
                QMessageBox.about(self, ' ', '退房失败！')