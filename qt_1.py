# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1191, 899)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(290, 20, 761, 821))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_62 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_62.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.gridLayout.addWidget(self.label_62, 15, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_51.setObjectName("label_51")
        self.gridLayout.addWidget(self.label_51, 13, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.label_sale = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sale.setText("")
        self.label_sale.setObjectName("label_sale")
        self.horizontalLayout_5.addWidget(self.label_sale)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_55.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.gridLayout.addWidget(self.label_55, 17, 0, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 18, 0, 1, 1)
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.gridLayout.addWidget(self.lcdNumber_1, 16, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_47.setObjectName("label_47")
        self.gridLayout.addWidget(self.label_47, 11, 0, 1, 1)
        self.label_com = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_com.setText("")
        self.label_com.setObjectName("label_com")
        self.gridLayout.addWidget(self.label_com, 14, 0, 1, 1)
        self.label_hoz = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_hoz.setText("")
        self.label_hoz.setObjectName("label_hoz")
        self.gridLayout.addWidget(self.label_hoz, 12, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_val_cost = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_val_cost.setAlignment(QtCore.Qt.AlignCenter)
        self.label_val_cost.setObjectName("label_val_cost")
        self.horizontalLayout_2.addWidget(self.label_val_cost)
        self.label_val_cost_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_val_cost_2.setText("")
        self.label_val_cost_2.setObjectName("label_val_cost_2")
        self.horizontalLayout_2.addWidget(self.label_val_cost_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.pushButton_count = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_count.setObjectName("pushButton_count")
        self.gridLayout.addWidget(self.pushButton_count, 21, 0, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 20, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_tovar = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_tovar.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tovar.setObjectName("label_tovar")
        self.horizontalLayout.addWidget(self.label_tovar)
        self.comboBox_name = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_name.setObjectName("comboBox_name")
        self.horizontalLayout.addWidget(self.comboBox_name)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_sotrud_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sotrud_1.setObjectName("label_sotrud_1")
        self.verticalLayout.addWidget(self.label_sotrud_1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.lineEdit_count_day_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_count_day_1.setObjectName("lineEdit_count_day_1")
        self.verticalLayout.addWidget(self.lineEdit_count_day_1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_wages_full_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_full_1.setText("")
        self.label_wages_full_1.setObjectName("label_wages_full_1")
        self.verticalLayout.addWidget(self.label_wages_full_1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.label_ndfl_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ndfl_1.setText("")
        self.label_ndfl_1.setObjectName("label_ndfl_1")
        self.verticalLayout.addWidget(self.label_ndfl_1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_48.setObjectName("label_48")
        self.verticalLayout.addWidget(self.label_48)
        self.label_fss_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fss_1.setText("")
        self.label_fss_1.setObjectName("label_fss_1")
        self.verticalLayout.addWidget(self.label_fss_1)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_49.setObjectName("label_49")
        self.verticalLayout.addWidget(self.label_49)
        self.label_foms_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_foms_1.setText("")
        self.label_foms_1.setObjectName("label_foms_1")
        self.verticalLayout.addWidget(self.label_foms_1)
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_50.setObjectName("label_50")
        self.verticalLayout.addWidget(self.label_50)
        self.label_pfr_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pfr_1.setText("")
        self.label_pfr_1.setObjectName("label_pfr_1")
        self.verticalLayout.addWidget(self.label_pfr_1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_wages_out_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_out_1.setText("")
        self.label_wages_out_1.setObjectName("label_wages_out_1")
        self.verticalLayout.addWidget(self.label_wages_out_1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.lineEdit_count_day_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_count_day_2.setObjectName("lineEdit_count_day_2")
        self.verticalLayout_2.addWidget(self.lineEdit_count_day_2)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_wages_full_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_full_2.setText("")
        self.label_wages_full_2.setObjectName("label_wages_full_2")
        self.verticalLayout_2.addWidget(self.label_wages_full_2)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_2.addWidget(self.label_26)
        self.label_ndfl_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ndfl_2.setText("")
        self.label_ndfl_2.setObjectName("label_ndfl_2")
        self.verticalLayout_2.addWidget(self.label_ndfl_2)
        self.label_64 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_64.setObjectName("label_64")
        self.verticalLayout_2.addWidget(self.label_64)
        self.label_fss_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fss_2.setText("")
        self.label_fss_2.setObjectName("label_fss_2")
        self.verticalLayout_2.addWidget(self.label_fss_2)
        self.label_68 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_68.setObjectName("label_68")
        self.verticalLayout_2.addWidget(self.label_68)
        self.label_foms_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_foms_2.setText("")
        self.label_foms_2.setObjectName("label_foms_2")
        self.verticalLayout_2.addWidget(self.label_foms_2)
        self.label_58 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_2.addWidget(self.label_58)
        self.label_pfr_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pfr_2.setText("")
        self.label_pfr_2.setObjectName("label_pfr_2")
        self.verticalLayout_2.addWidget(self.label_pfr_2)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_wages_out_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_out_2.setText("")
        self.label_wages_out_2.setObjectName("label_wages_out_2")
        self.verticalLayout_2.addWidget(self.label_wages_out_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16)
        self.lineEdit_count_day_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_count_day_3.setObjectName("lineEdit_count_day_3")
        self.verticalLayout_4.addWidget(self.lineEdit_count_day_3)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21)
        self.label_wages_full_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_full_3.setText("")
        self.label_wages_full_3.setObjectName("label_wages_full_3")
        self.verticalLayout_4.addWidget(self.label_wages_full_3)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_4.addWidget(self.label_30)
        self.label_ndfl_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ndfl_3.setText("")
        self.label_ndfl_3.setObjectName("label_ndfl_3")
        self.verticalLayout_4.addWidget(self.label_ndfl_3)
        self.label_65 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_65.setObjectName("label_65")
        self.verticalLayout_4.addWidget(self.label_65)
        self.label_fss_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fss_3.setText("")
        self.label_fss_3.setObjectName("label_fss_3")
        self.verticalLayout_4.addWidget(self.label_fss_3)
        self.label_69 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_69.setObjectName("label_69")
        self.verticalLayout_4.addWidget(self.label_69)
        self.label_foms_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_foms_3.setText("")
        self.label_foms_3.setObjectName("label_foms_3")
        self.verticalLayout_4.addWidget(self.label_foms_3)
        self.label_59 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_59.setObjectName("label_59")
        self.verticalLayout_4.addWidget(self.label_59)
        self.label_pfr_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pfr_3.setText("")
        self.label_pfr_3.setObjectName("label_pfr_3")
        self.verticalLayout_4.addWidget(self.label_pfr_3)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_4.addWidget(self.label_22)
        self.label_wages_out_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_out_3.setText("")
        self.label_wages_out_3.setObjectName("label_wages_out_3")
        self.verticalLayout_4.addWidget(self.label_wages_out_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_6.addWidget(self.label_20)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_6.addWidget(self.label_27)
        self.label_wages_full_d = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_full_d.setText("")
        self.label_wages_full_d.setObjectName("label_wages_full_d")
        self.verticalLayout_6.addWidget(self.label_wages_full_d)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_6.addWidget(self.label_32)
        self.label_ndfl_d = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ndfl_d.setText("")
        self.label_ndfl_d.setObjectName("label_ndfl_d")
        self.verticalLayout_6.addWidget(self.label_ndfl_d)
        self.label_67 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_67.setObjectName("label_67")
        self.verticalLayout_6.addWidget(self.label_67)
        self.label_fss_d = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fss_d.setText("")
        self.label_fss_d.setObjectName("label_fss_d")
        self.verticalLayout_6.addWidget(self.label_fss_d)
        self.label_71 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_71.setObjectName("label_71")
        self.verticalLayout_6.addWidget(self.label_71)
        self.label_foms_d = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_foms_d.setText("")
        self.label_foms_d.setObjectName("label_foms_d")
        self.verticalLayout_6.addWidget(self.label_foms_d)
        self.label_61 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_61.setObjectName("label_61")
        self.verticalLayout_6.addWidget(self.label_61)
        self.label_pfr_d = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pfr_d.setText("")
        self.label_pfr_d.setObjectName("label_pfr_d")
        self.verticalLayout_6.addWidget(self.label_pfr_d)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_6.addWidget(self.label_28)
        self.label_wages_out_d = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_out_d.setText("")
        self.label_wages_out_d.setObjectName("label_wages_out_d")
        self.verticalLayout_6.addWidget(self.label_wages_out_d)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.label_17)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.label_wages_full_b = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_full_b.setText("")
        self.label_wages_full_b.setObjectName("label_wages_full_b")
        self.verticalLayout_5.addWidget(self.label_wages_full_b)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_5.addWidget(self.label_31)
        self.label_ndfl_b = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_ndfl_b.setText("")
        self.label_ndfl_b.setObjectName("label_ndfl_b")
        self.verticalLayout_5.addWidget(self.label_ndfl_b)
        self.label_66 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_66.setObjectName("label_66")
        self.verticalLayout_5.addWidget(self.label_66)
        self.label_fss_b = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_fss_b.setText("")
        self.label_fss_b.setObjectName("label_fss_b")
        self.verticalLayout_5.addWidget(self.label_fss_b)
        self.label_70 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_70.setObjectName("label_70")
        self.verticalLayout_5.addWidget(self.label_70)
        self.label_foms_b = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_foms_b.setText("")
        self.label_foms_b.setObjectName("label_foms_b")
        self.verticalLayout_5.addWidget(self.label_foms_b)
        self.label_60 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_60.setObjectName("label_60")
        self.verticalLayout_5.addWidget(self.label_60)
        self.label_pfr_b = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_pfr_b.setText("")
        self.label_pfr_b.setObjectName("label_pfr_b")
        self.verticalLayout_5.addWidget(self.label_pfr_b)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_5.addWidget(self.label_29)
        self.label_wages_out_b_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wages_out_b_2.setText("")
        self.label_wages_out_b_2.setObjectName("label_wages_out_b_2")
        self.verticalLayout_5.addWidget(self.label_wages_out_b_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 22, 0, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_57.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.gridLayout.addWidget(self.label_57, 19, 0, 1, 1)
        self.label_amort = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_amort.setText("")
        self.label_amort.setObjectName("label_amort")
        self.gridLayout.addWidget(self.label_amort, 10, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 23, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_6.addWidget(self.radioButton)
        self.label_procent = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_procent.setText("")
        self.label_procent.setObjectName("label_procent")
        self.horizontalLayout_6.addWidget(self.label_procent)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.label_cost = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_cost.setText("")
        self.label_cost.setObjectName("label_cost")
        self.horizontalLayout_4.addWidget(self.label_cost)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 9, 0, 1, 1)
        self.label_print = QtWidgets.QLabel(self.centralwidget)
        self.label_print.setGeometry(QtCore.QRect(20, 650, 251, 181))
        self.label_print.setText("")
        self.label_print.setObjectName("label_print")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 20, 160, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_list_product = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_list_product.setObjectName("pushButton_list_product")
        self.verticalLayout_3.addWidget(self.pushButton_list_product)
        self.pushButton_change_pol = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_change_pol.setObjectName("pushButton_change_pol")
        self.verticalLayout_3.addWidget(self.pushButton_change_pol)
        self.label_current_user = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_current_user.setText("")
        self.label_current_user.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_user.setObjectName("label_current_user")
        self.verticalLayout_3.addWidget(self.label_current_user)
        self.pushButton_show = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_show.setGeometry(QtCore.QRect(1060, 20, 121, 23))
        self.pushButton_show.setObjectName("pushButton_show")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1191, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Бухгалтерия в малом предприятии"))
        self.label_62.setText(_translate("mainWindow", "Суммарная зарплата"))
        self.label_51.setText(_translate("mainWindow", "Коммунальные расходы(1%)"))
        self.label.setText(_translate("mainWindow", "Выручка"))
        self.label_55.setText(_translate("mainWindow", "Расходы"))
        self.label_47.setText(_translate("mainWindow", "Хозяйственные расходы(1 %)"))
        self.label_val_cost.setText(_translate("mainWindow", "Валовая прибыль"))
        self.pushButton_count.setText(_translate("mainWindow", "Посчитать"))
        self.label_tovar.setText(_translate("mainWindow", "товар"))
        self.label_sotrud_1.setText(_translate("mainWindow", "Сотрудник 1"))
        self.label_9.setText(_translate("mainWindow", "Количество отработанных дней"))
        self.label_12.setText(_translate("mainWindow", "Зарплата общая"))
        self.label_24.setText(_translate("mainWindow", "Налог НДФЛ(13%)"))
        self.label_48.setText(_translate("mainWindow", "ФСС(2,9%)"))
        self.label_49.setText(_translate("mainWindow", "ФОМС(5,1%)"))
        self.label_50.setText(_translate("mainWindow", "ПФР(22%)"))
        self.label_18.setText(_translate("mainWindow", "Зарплата к выдаче"))
        self.label_7.setText(_translate("mainWindow", "Сотрудник 2"))
        self.label_10.setText(_translate("mainWindow", "Количество отработанных дней"))
        self.label_13.setText(_translate("mainWindow", "Зарплата общая"))
        self.label_26.setText(_translate("mainWindow", "Налог НДФЛ(13%)"))
        self.label_64.setText(_translate("mainWindow", "ФСС(2,9%)"))
        self.label_68.setText(_translate("mainWindow", "ФОМС(5,1%)"))
        self.label_58.setText(_translate("mainWindow", "ПФР(22%)"))
        self.label_19.setText(_translate("mainWindow", "Зарплата к выдаче"))
        self.label_15.setText(_translate("mainWindow", "Сотрудник 3"))
        self.label_16.setText(_translate("mainWindow", "Количество отработанных дней"))
        self.label_21.setText(_translate("mainWindow", "Зарплата общая"))
        self.label_30.setText(_translate("mainWindow", "Налог НДФЛ(13%)"))
        self.label_65.setText(_translate("mainWindow", "ФСС(2,9%)"))
        self.label_69.setText(_translate("mainWindow", "ФОМС(5,1%)"))
        self.label_59.setText(_translate("mainWindow", "ПФР(22%)"))
        self.label_22.setText(_translate("mainWindow", "Зарплата к выдаче"))
        self.label_20.setText(_translate("mainWindow", "Директор(10%)"))
        self.label_27.setText(_translate("mainWindow", "Зарплата общая"))
        self.label_32.setText(_translate("mainWindow", "Налог НДФЛ(13%)"))
        self.label_67.setText(_translate("mainWindow", "ФСС(2,9%)"))
        self.label_71.setText(_translate("mainWindow", "ФОМС(5,1%)"))
        self.label_61.setText(_translate("mainWindow", "ПФР(22%)"))
        self.label_28.setText(_translate("mainWindow", "Зарплата к выдаче"))
        self.label_17.setText(_translate("mainWindow", "Бухгалтер(7%)"))
        self.label_23.setText(_translate("mainWindow", "Зарплата общая"))
        self.label_31.setText(_translate("mainWindow", "Налог НДФЛ(13%)"))
        self.label_66.setText(_translate("mainWindow", "ФСС(2,9%)"))
        self.label_70.setText(_translate("mainWindow", "ФОМС(5,1%)"))
        self.label_60.setText(_translate("mainWindow", "ПФР(22%)"))
        self.label_29.setText(_translate("mainWindow", "Зарплата к выдаче"))
        self.pushButton_save.setText(_translate("mainWindow", "Сохранить"))
        self.label_57.setText(_translate("mainWindow", "Остаток прибыли для распределения акционерам"))
        self.pushButton_add.setText(_translate("mainWindow", "Добавить товар в базу данных"))
        self.radioButton.setText(_translate("mainWindow", "Сейчас сентябрь-февраль?"))
        self.label_3.setText(_translate("mainWindow", "Себестоимость"))
        self.label_44.setText(_translate("mainWindow", "Амортизация оборудования(1%)"))
        self.pushButton_list_product.setText(_translate("mainWindow", "Добавить товар в список"))
        self.pushButton_change_pol.setText(_translate("mainWindow", "Сменить пользователя"))
        self.pushButton_show.setText(_translate("mainWindow", "показать"))
