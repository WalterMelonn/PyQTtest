#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

combobox_need = 14


class DynamicComboBoxes(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DynamicComboBoxes, self).__init__(parent)
        vbox = QtWidgets.QVBoxLayout(self)
        spinbox = QtWidgets.QSpinBox(self)
        spinbox.setRange(0, combobox_need)
        spinbox.valueChanged.connect(self.onChangeValue)

        qbtn = QPushButton('Рассчитать', self)
        qbtn.clicked.connect(self.onBtnClick)
        self.itemlist = []
        self.btncounter0 = 0

        vbox.addWidget(qbtn)
        vbox.addWidget(spinbox)

        self.grid = QtWidgets.QGridLayout()
        self.itemlist = []
        vbox.addLayout(self.grid)
        vbox.addStretch(1)

    def onChangeValue(self, val):
        for label, combobox in self.itemlist:
            label.deleteLater()
            combobox.deleteLater()
        self.itemlist = []
        for i in range(val):
            label = QtWidgets.QLabel('This is Label {}'.format(i+1))
            combobox = QtWidgets.QComboBox()
            self.grid.addWidget(label, i, 0)
            self.grid.addWidget(combobox, i, 1)
            self.itemlist.append([label, combobox])
            # print(self.itemlist[i][1])
        nameslist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
        btncounter = self.btncounter0
        while btncounter != combobox_need:
            try:
                btncounter += 1

                self.itemlist[btncounter-1][1].addItems([str(nameslist[btncounter-1])])
                #self.itemlist[btncounter - 1][1].addItems([str(btncounter)])
            except:
                print(Exception)
            print("Завершение программы")

    def onBtnClick(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = DynamicComboBoxes()
    box.show()
    sys.exit(app.exec_())
