import excel_reader as er
import pandas as pd
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

combobox_need = er.excelRead.parameters_counter()


class DynamicComboBoxes(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DynamicComboBoxes, self).__init__(parent)
        vbox = QtWidgets.QVBoxLayout(self)
        spinbox = QtWidgets.QSpinBox(self)
        spinbox.setRange(0, combobox_need)
        spinbox.valueChanged.connect(self.onChangeValue)
        self.combobox_need_class = combobox_need

        qbtn = QPushButton('Рассчитать', self)
        qbtn.clicked.connect(self.onBtnClick)
        self.itemlist = []
        self.btncounter0 = 0
        self.m1 = 0

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
            label = QtWidgets.QLabel('This is Label {}'.format(i + 1))
            combobox = QtWidgets.QComboBox()
            self.grid.addWidget(label, i, 0)
            self.grid.addWidget(combobox, i, 1)
            self.itemlist.append([label, combobox])

        mainDf = er.ReadEx.lltrsDf
        list1 = []
        global_itemslist = []
        # combobox_need_func = self.combobox_need_class
        for current_cell in range(len(mainDf)):
            cell_value = mainDf.iloc[current_cell, 0]
            if cell_value != 'X':
                itemslist = global_itemslist
                itemslist.append(mainDf.iloc[current_cell, 2])
            else:
                list1.append(global_itemslist)
                itemslist = []
                global_itemslist = []
        print("Исходный:", list1)

        current_combobox_list = list1

        for m in range(combobox_need):
            nameslist = current_combobox_list[m]
            try:
                self.itemlist[m][1].addItems(nameslist)
            except:
                print(Exception)
            print("Завершение программы заполнения", m, "комбобокса")




        """
        for each_list in range(len('2')):
            each_current_combobox_list = nameslist[each_list]
            for each_current_combobox in range(combobox_need):

                try:
                    self.itemlist[each_current_combobox][1].addItems(each_current_combobox_list)
                except:
                    print(Exception)
                print("Завершение программы заполнения", each_current_combobox, "комбобокса")

        
            for each_list in range(len(nameslist)):
            current_list = nameslist[each_list]
            print(current_list)
            for each_current_combobox in range(combobox_need):
                try:
                    self.itemlist[each_current_combobox][1].addItems(current_list)
                except:
                    print(Exception)
                print("Завершение программы заполнения", each_current_combobox, "комбобокса")
           
        nameslist = list1
        #self.itemlist[0][1].addItems(["1"])
        btncounter = self.btncounter0
        while btncounter != combobox_need:
            try:
                btncounter += 1
                m = self.m1
                while m != 2:
                    try:
                        m += 1
                        print("Зашли в цикл №1, m =", m)
                        self.itemlist[int(m)][1].addItems([str(nameslist[0][m])])
                        #self.itemlist[btncounter - 1][1].addItems("0")
                        # print(self.itemlist[btncounter - 1][1].addItems([str(nameslist[btncounter - 1][m-1])]))
                        m += 1
                        print("Выжили в цикле в цикл 1, m =", m)
                    except:
                        print(Exception)
                    print("Завершение программы заполнения ", btncounter, "комбобокса")
                m = 0
            except:
                print(Exception)

            print("Завершение программы начинения всех комбобоксов")
            """

    def onBtnClick(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    box = DynamicComboBoxes()
    box.show()
    sys.exit(app.exec_())
