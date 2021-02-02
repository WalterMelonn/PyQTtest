#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):


class DynamicComboBoxes(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DynamicComboBoxes, self).__init__(parent)
        vbox = QtWidgets.QVBoxLayout(self)
        spinbox = QtWidgets.QSpinBox(self)
        spinbox.setRange(0, 10)
        spinbox.valueChanged.connect(self.onChangeValue)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    box = DynamicComboBoxes()
    box.show()
    sys.exit(app.exec_())
