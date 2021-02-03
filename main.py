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
            label = QtWidgets.QLabel('This is Label {}'.format(i))
            combobox = QtWidgets.QComboBox()
            self.grid.addWidget(label, i, 0)
            self.grid.addWidget(combobox, i, 1)
            self.itemlist.append([label, combobox])
            # print(self.itemlist[i][1])
        """
        for 
            try:
                self.itemlist[i-1][1].addItems(["DEFAULT", "PATCH"])
                self.itemlist[i][1].addItems(["1111", "2222"])
            except:
                print(Exception)
            print("Завершение программы")
        """
        for i in range(2):
            try:
               # DynamicComboBoxes.itemlist[i - 1][1].addItems(["1", "2", "3", "4", "5"])
                self.itemlist[0][1].addItems(["1"])
                self.itemlist[1][1].addItems(["2"])
            except:
                print(Exception)
            print("Завершение программы")

    def onBtnClick(self):
        for i in range(2):
            try:
               # DynamicComboBoxes.itemlist[i - 1][1].addItems(["1", "2", "3", "4", "5"])
                self.itemlist[0][1].addItems(["1"])
                self.itemlist[1][1].addItems(["2"])
            except:
                print(Exception)
            print("Завершение программы")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = DynamicComboBoxes()
    box.show()
    sys.exit(app.exec_())
