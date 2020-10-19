import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from query1 import query
from datetime import datetime
from refund1 import refund
import copy

class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('客房管理系统')
        self.vbox = QVBoxLayout()
        self.initUI()

    def initUI(self):
        self.form1 = QFormLayout()
        self.form2 = QFormLayout()
        self.form3 = QFormLayout()

        self.combo = QComboBox()
        self.combo.addItem('单人房')
        self.combo.addItem('双人房')
        self.combo.addItem('三人房')
        self.form1.addRow('房间类型：', self.combo)

        self.dateEdit1 = QDateTimeEdit(QDate.currentDate())
        self.dateEdit1.setDisplayFormat("yyyy.MM.dd")
        self.dateEdit1.setMinimumDate(QDate.currentDate().addDays(-3650))
        self.dateEdit1.setMaximumDate(QDate.currentDate().addDays(3650))
        self.dateEdit1.setCalendarPopup(True)
        self.form2.addRow('入住日期：', self.dateEdit1)

        self.dateEdit2 = QDateTimeEdit(QDate.currentDate())
        self.dateEdit2.setDisplayFormat("yyyy.MM.dd")
        self.dateEdit2.setMinimumDate(QDate.currentDate().addDays(-3650))
        self.dateEdit2.setMaximumDate(QDate.currentDate().addDays(3650))
        self.dateEdit2.setCalendarPopup(True)
        self.form3.addRow('退房日期：', self.dateEdit2)


        self.widght1 = QWidget()
        self.widght1.setLayout(self.form1)

        self.widght2 = QWidget()
        self.widght2.setLayout(self.form2)

        self.widght3 = QWidget()
        self.widght3.setLayout(self.form3)

        self.vbox.addWidget(self.widght1)
        self.vbox.addWidget(self.widght2)
        self.vbox.addWidget(self.widght3)

        self.button = QPushButton('查询房间')
        self.button.clicked.connect(self.query)
        self.vbox.addWidget(self.button)

        self.button = QPushButton('点击退房')
        self.button.clicked.connect(self.refund)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)


    def query(self):
        print(self.combo.currentText())
        print(self.dateEdit1.text())
        print(self.dateEdit2.text())
        time1 = self.dateEdit1.text()
        time2 = self.dateEdit2.text()
        result = timesub(time1, time2)
        if self.combo.currentText() == '单人房':
            temp = 1
        elif self.combo.currentText() == '双人房':
            temp = 2
        else:
            temp = 3
        temp1 = copy.deepcopy(temp)
        temp2 = copy.deepcopy(result)
        temp3 = copy.deepcopy(self.dateEdit1.text())
        temp4 = copy.deepcopy(self.dateEdit2.text())
        self.query = query(temp1, temp2, temp3, temp4)
        self.query.show()

    def refund(self):
        self.refund = refund()
        self.refund.show()


def timesub(time1, time2):
    temp1 = time1.split('.')
    temp2 = time2.split('.')
    cur = datetime(int(temp1[0]), int(temp1[1]), int(temp1[2]))
    next = datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]))
    return (next - cur).days

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = main()
    main.show()
    sys.exit(app.exec_())