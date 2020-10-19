import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class main(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        self.setWindowTitle('客房管理系统')
        self.vbox = QVBoxLayout()
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.hbox = QHBoxLayout()
        self.tabelwidget = QTableWidget()
        self.item_num = 2
        self.initUI()

    def initUI(self):

        # self.tabelwidget.setRowCount(self.item_num)
        self.tabelwidget.setRowCount(20)
        self.tabelwidget.setColumnCount(3)
        self.hbox.addWidget(self.tabelwidget)
        self.tabelwidget.setHorizontalHeaderLabels(['房间号', '房间类型', '房间价格'])
        file = open('item.txt', encoding='utf-8')
        items = []
        while True:
            line = file.readline()
            if not line:
                break
            items.append(line)
        file.close()
        i = 0
        for item in items:
            item = item.replace('\n', '')
            list = item.split(' ')
            for j in range(3):
                temp = QTableWidgetItem(list[j])
                temp.setTextAlignment(Qt.AlignCenter)
                self.tabelwidget.setItem(i, j, temp)
            i = i + 1
        self.tabelwidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabelwidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabelwidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tabelwidget.verticalHeader().setVisible(False)

        self.widget1.setLayout(self.hbox)
        self.vbox.addWidget(self.widget1)
        self.setLayout(self.hbox)

        self.form1 = QFormLayout()
        self.form2 = QFormLayout()
        self.form3 = QFormLayout()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = main()
    main.show()
    sys.exit(app.exec_())