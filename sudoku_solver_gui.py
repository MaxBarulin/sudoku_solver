import re
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 294)
        Form.setMinimumSize(QtCore.QSize(482, 294))
        Form.setMaximumSize(QtCore.QSize(482, 294))
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(158, 245, 81, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(200, 268, 81, 23))
        self.pushButton_1.setObjectName("pushButton_1")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(242, 245, 81, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 230))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.lineEdit_1 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit('6' ,self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 2, 1, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 3, 1, 1)
        
        self.lineEdit_5 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 0, 4, 1, 1)

        self.lineEdit_6 = QtWidgets.QLineEdit('5' ,self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 0, 5, 1, 1)

        self.lineEdit_7 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 0, 6, 1, 1)

        self.lineEdit_8 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 0, 7, 1, 1)

        self.lineEdit_9 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 0, 8, 1, 1)

        self.lineEdit_10 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 1, 0, 1, 1)

        self.lineEdit_11 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 1, 1, 1, 1)

        self.lineEdit_12 = QtWidgets.QLineEdit('2' ,self.gridLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 1, 2, 1, 1)

        self.lineEdit_13 = QtWidgets.QLineEdit('1' ,self.gridLayoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 1, 3, 1, 1)

        self.lineEdit_14 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 1, 4, 1, 1)

        self.lineEdit_15 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 1, 5, 1, 1)

        self.lineEdit_16 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 1, 6, 1, 1)

        self.lineEdit_17 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 1, 7, 1, 1)

        self.lineEdit_18 = QtWidgets.QLineEdit('6' ,self.gridLayoutWidget)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout.addWidget(self.lineEdit_18, 1, 8, 1, 1)

        self.lineEdit_19 = QtWidgets.QLineEdit('8' ,self.gridLayoutWidget)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout.addWidget(self.lineEdit_19, 2, 0, 1, 1)

        self.lineEdit_20 = QtWidgets.QLineEdit('1' ,self.gridLayoutWidget)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout.addWidget(self.lineEdit_20, 2, 1, 1, 1)

        self.lineEdit_21 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout.addWidget(self.lineEdit_21, 2, 2, 1, 1)

        self.lineEdit_22 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout.addWidget(self.lineEdit_22, 2, 3, 1, 1)

        self.lineEdit_23 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout.addWidget(self.lineEdit_23, 2, 4, 1, 1)

        self.lineEdit_24 = QtWidgets.QLineEdit('6' ,self.gridLayoutWidget)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout.addWidget(self.lineEdit_24, 2, 5, 1, 1)

        self.lineEdit_25 = QtWidgets.QLineEdit('3' ,self.gridLayoutWidget)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout.addWidget(self.lineEdit_25, 2, 6, 1, 1)

        self.lineEdit_26 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout.addWidget(self.lineEdit_26, 2, 7, 1, 1)
        
        self.lineEdit_27 = QtWidgets.QLineEdit('5' ,self.gridLayoutWidget)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout.addWidget(self.lineEdit_27, 2, 8, 1, 1)
        
        self.lineEdit_28 = QtWidgets.QLineEdit('4' ,self.gridLayoutWidget)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout.addWidget(self.lineEdit_28, 3, 0, 1, 1)

        self.lineEdit_29 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout.addWidget(self.lineEdit_29, 3, 1, 1, 1)

        self.lineEdit_30 = QtWidgets.QLineEdit('1' ,self.gridLayoutWidget)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout.addWidget(self.lineEdit_30, 3, 2, 1, 1)

        self.lineEdit_31 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout.addWidget(self.lineEdit_31, 3, 3, 1, 1)

        self.lineEdit_32 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout.addWidget(self.lineEdit_32, 3, 4, 1, 1)

        self.lineEdit_33 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout.addWidget(self.lineEdit_33, 3, 5, 1, 1)

        self.lineEdit_34 = QtWidgets.QLineEdit('5' ,self.gridLayoutWidget)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout.addWidget(self.lineEdit_34, 3, 6, 1, 1)

        self.lineEdit_35 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout.addWidget(self.lineEdit_35, 3, 7, 1, 1)

        self.lineEdit_36 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout.addWidget(self.lineEdit_36, 3, 8, 1, 1)

        self.lineEdit_37 = QtWidgets.QLineEdit('3' ,self.gridLayoutWidget)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout.addWidget(self.lineEdit_37, 4, 0, 1, 1)

        self.lineEdit_38 = QtWidgets.QLineEdit('2' ,self.gridLayoutWidget)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout.addWidget(self.lineEdit_38, 4, 1, 1, 1)

        self.lineEdit_39 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout.addWidget(self.lineEdit_39, 4, 2, 1, 1)

        self.lineEdit_40 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout.addWidget(self.lineEdit_40, 4, 3, 1, 1)

        self.lineEdit_41 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout.addWidget(self.lineEdit_41, 4, 4, 1, 1)

        self.lineEdit_42 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout.addWidget(self.lineEdit_42, 4, 5, 1, 1)

        self.lineEdit_43 = QtWidgets.QLineEdit('4' ,self.gridLayoutWidget)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout.addWidget(self.lineEdit_43, 4, 6, 1, 1)

        self.lineEdit_44 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.gridLayout.addWidget(self.lineEdit_44, 4, 7, 1, 1)

        self.lineEdit_45 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.gridLayout.addWidget(self.lineEdit_45, 4, 8, 1, 1)

        self.lineEdit_46 = QtWidgets.QLineEdit('9' ,self.gridLayoutWidget)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.gridLayout.addWidget(self.lineEdit_46, 5, 0, 1, 1)

        self.lineEdit_47 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.gridLayout.addWidget(self.lineEdit_47, 5, 1, 1, 1)

        self.lineEdit_48 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.gridLayout.addWidget(self.lineEdit_48, 5, 2, 1, 1)

        self.lineEdit_49 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.gridLayout.addWidget(self.lineEdit_49, 5, 3, 1, 1)

        self.lineEdit_50 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.gridLayout.addWidget(self.lineEdit_50, 5, 4, 1, 1)

        self.lineEdit_51 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.gridLayout.addWidget(self.lineEdit_51, 5, 5, 1, 1)

        self.lineEdit_52 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.gridLayout.addWidget(self.lineEdit_52, 5, 6, 1, 1)

        self.lineEdit_53 = QtWidgets.QLineEdit('2' ,self.gridLayoutWidget)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.gridLayout.addWidget(self.lineEdit_53, 5, 7, 1, 1)

        self.lineEdit_54 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.gridLayout.addWidget(self.lineEdit_54, 5, 8, 1, 1)

        self.lineEdit_55 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.gridLayout.addWidget(self.lineEdit_55, 6, 0, 1, 1)

        self.lineEdit_56 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.gridLayout.addWidget(self.lineEdit_56, 6, 1, 1, 1)

        self.lineEdit_57 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.gridLayout.addWidget(self.lineEdit_57, 6, 2, 1, 1)

        self.lineEdit_58 = QtWidgets.QLineEdit('2' ,self.gridLayoutWidget)
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.gridLayout.addWidget(self.lineEdit_58, 6, 3, 1, 1)

        self.lineEdit_59 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.gridLayout.addWidget(self.lineEdit_59, 6, 4, 1, 1)

        self.lineEdit_60 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_60.setObjectName("lineEdit_60")
        self.gridLayout.addWidget(self.lineEdit_60, 6, 5, 1, 1)

        self.lineEdit_61 = QtWidgets.QLineEdit('8' ,self.gridLayoutWidget)
        self.lineEdit_61.setObjectName("lineEdit_61")
        self.gridLayout.addWidget(self.lineEdit_61, 6, 6, 1, 1)

        self.lineEdit_62 = QtWidgets.QLineEdit('4' ,self.gridLayoutWidget)
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.gridLayout.addWidget(self.lineEdit_62, 6, 7, 1, 1)

        self.lineEdit_63 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_63.setObjectName("lineEdit_63")
        self.gridLayout.addWidget(self.lineEdit_63, 6, 8, 1, 1)
        
        self.lineEdit_64 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_64.setObjectName("lineEdit_64")
        self.gridLayout.addWidget(self.lineEdit_64, 7, 0, 1, 1)

        self.lineEdit_65 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_65.setObjectName("lineEdit_65")
        self.gridLayout.addWidget(self.lineEdit_65, 7, 1, 1, 1)

        self.lineEdit_66 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_66.setObjectName("lineEdit_66")
        self.gridLayout.addWidget(self.lineEdit_66, 7, 2, 1, 1)

        self.lineEdit_67 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_67.setObjectName("lineEdit_67")
        self.gridLayout.addWidget(self.lineEdit_67, 7, 3, 1, 1)
        
        self.lineEdit_68 = QtWidgets.QLineEdit('4' ,self.gridLayoutWidget)
        self.lineEdit_68.setObjectName("lineEdit_68")
        self.gridLayout.addWidget(self.lineEdit_68, 7, 4, 1, 1)

        self.lineEdit_69 = QtWidgets.QLineEdit('1' ,self.gridLayoutWidget)
        self.lineEdit_69.setObjectName("lineEdit_69")
        self.gridLayout.addWidget(self.lineEdit_69, 7, 5, 1, 1)

        self.lineEdit_70 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_70.setObjectName("lineEdit_70")
        self.gridLayout.addWidget(self.lineEdit_70, 7, 6, 1, 1)
        
        self.lineEdit_71 = QtWidgets.QLineEdit('3' ,self.gridLayoutWidget)
        self.lineEdit_71.setObjectName("lineEdit_71")
        self.gridLayout.addWidget(self.lineEdit_71, 7, 7, 1, 1)

        self.lineEdit_72 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.gridLayout.addWidget(self.lineEdit_72, 7, 8, 1, 1)
        
        self.lineEdit_73 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.gridLayout.addWidget(self.lineEdit_73, 8, 0, 1, 1)
        
        self.lineEdit_74 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.gridLayout.addWidget(self.lineEdit_74, 8, 1, 1, 1)
        
        self.lineEdit_75 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.gridLayout.addWidget(self.lineEdit_75, 8, 2, 1, 1)
        
        self.lineEdit_76 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.gridLayout.addWidget(self.lineEdit_76, 8, 3, 1, 1)
        
        self.lineEdit_77 = QtWidgets.QLineEdit('8' ,self.gridLayoutWidget)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.gridLayout.addWidget(self.lineEdit_77, 8, 4, 1, 1)
        
        self.lineEdit_78 = QtWidgets.QLineEdit('3' ,self.gridLayoutWidget)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.gridLayout.addWidget(self.lineEdit_78, 8, 5, 1, 1)
        
        self.lineEdit_79 = QtWidgets.QLineEdit('6' ,self.gridLayoutWidget)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.gridLayout.addWidget(self.lineEdit_79, 8, 6, 1, 1)
        
        self.lineEdit_80 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_80.setObjectName("lineEdit_80")
        self.gridLayout.addWidget(self.lineEdit_80, 8, 7, 1, 1)
        
        self.lineEdit_81 = QtWidgets.QLineEdit('' ,self.gridLayoutWidget)
        self.lineEdit_81.setObjectName("lineEdit_81")
        self.gridLayout.addWidget(self.lineEdit_81, 8, 8, 1, 1)
        
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(250, 10, 221, 231))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 7, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.gridLayout_2.addWidget(self.label_53, 5, 7, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_62.setAlignment(QtCore.Qt.AlignCenter)
        self.label_62.setObjectName("label_62")
        self.gridLayout_2.addWidget(self.label_62, 6, 7, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 4, 2, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        self.gridLayout_2.addWidget(self.label_63, 6, 8, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.gridLayout_2.addWidget(self.label_55, 6, 0, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_74.setAlignment(QtCore.Qt.AlignCenter)
        self.label_74.setObjectName("label_74")
        self.gridLayout_2.addWidget(self.label_74, 8, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 2, 2, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.gridLayout_2.addWidget(self.label_68, 7, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 8, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 4, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 3, 5, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 4, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 2, 4, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 3, 8, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_77.setAlignment(QtCore.Qt.AlignCenter)
        self.label_77.setObjectName("label_77")
        self.gridLayout_2.addWidget(self.label_77, 8, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 3, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_81.setAlignment(QtCore.Qt.AlignCenter)
        self.label_81.setObjectName("label_81")
        self.gridLayout_2.addWidget(self.label_81, 8, 8, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_78.setAlignment(QtCore.Qt.AlignCenter)
        self.label_78.setObjectName("label_78")
        self.gridLayout_2.addWidget(self.label_78, 8, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 8, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 2, 1, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.gridLayout_2.addWidget(self.label_49, 5, 3, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 4, 4, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_76.setAlignment(QtCore.Qt.AlignCenter)
        self.label_76.setObjectName("label_76")
        self.gridLayout_2.addWidget(self.label_76, 8, 3, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_72.setAlignment(QtCore.Qt.AlignCenter)
        self.label_72.setObjectName("label_72")
        self.gridLayout_2.addWidget(self.label_72, 7, 8, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.gridLayout_2.addWidget(self.label_54, 5, 8, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_56.setAlignment(QtCore.Qt.AlignCenter)
        self.label_56.setObjectName("label_56")
        self.gridLayout_2.addWidget(self.label_56, 6, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 4, 3, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_65.setAlignment(QtCore.Qt.AlignCenter)
        self.label_65.setObjectName("label_65")
        self.gridLayout_2.addWidget(self.label_65, 7, 1, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.gridLayout_2.addWidget(self.label_52, 5, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 6, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_79.setAlignment(QtCore.Qt.AlignCenter)
        self.label_79.setObjectName("label_79")
        self.gridLayout_2.addWidget(self.label_79, 8, 6, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout_2.addWidget(self.label_51, 5, 5, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.gridLayout_2.addWidget(self.label_48, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.gridLayout_2.addWidget(self.label_46, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 3, 3, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 4, 5, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_80.setAlignment(QtCore.Qt.AlignCenter)
        self.label_80.setObjectName("label_80")
        self.gridLayout_2.addWidget(self.label_80, 8, 7, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 2, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_64.setAlignment(QtCore.Qt.AlignCenter)
        self.label_64.setObjectName("label_64")
        self.gridLayout_2.addWidget(self.label_64, 7, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 4, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_2.addWidget(self.label_44, 4, 7, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 2, 7, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_67.setAlignment(QtCore.Qt.AlignCenter)
        self.label_67.setObjectName("label_67")
        self.gridLayout_2.addWidget(self.label_67, 7, 3, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_59.setAlignment(QtCore.Qt.AlignCenter)
        self.label_59.setObjectName("label_59")
        self.gridLayout_2.addWidget(self.label_59, 6, 4, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 3, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 1, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_71.setAlignment(QtCore.Qt.AlignCenter)
        self.label_71.setObjectName("label_71")
        self.gridLayout_2.addWidget(self.label_71, 7, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.gridLayout_2.addWidget(self.label_69, 7, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_73.setAlignment(QtCore.Qt.AlignCenter)
        self.label_73.setObjectName("label_73")
        self.gridLayout_2.addWidget(self.label_73, 8, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 5, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_57.setAlignment(QtCore.Qt.AlignCenter)
        self.label_57.setObjectName("label_57")
        self.gridLayout_2.addWidget(self.label_57, 6, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 0, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_60.setAlignment(QtCore.Qt.AlignCenter)
        self.label_60.setObjectName("label_60")
        self.gridLayout_2.addWidget(self.label_60, 6, 5, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 6, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_66.setAlignment(QtCore.Qt.AlignCenter)
        self.label_66.setObjectName("label_66")
        self.gridLayout_2.addWidget(self.label_66, 7, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_61.setAlignment(QtCore.Qt.AlignCenter)
        self.label_61.setObjectName("label_61")
        self.gridLayout_2.addWidget(self.label_61, 6, 6, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName("label_45")
        self.gridLayout_2.addWidget(self.label_45, 4, 8, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_58.setAlignment(QtCore.Qt.AlignCenter)
        self.label_58.setObjectName("label_58")
        self.gridLayout_2.addWidget(self.label_58, 6, 3, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_75.setAlignment(QtCore.Qt.AlignCenter)
        self.label_75.setObjectName("label_75")
        self.gridLayout_2.addWidget(self.label_75, 8, 2, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 2, 5, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.gridLayout_2.addWidget(self.label_50, 5, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 2, 8, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 2, 6, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 3, 4, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 3, 6, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.gridLayout_2.addWidget(self.label_70, 7, 6, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 3, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 2, 3, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.gridLayout_2.addWidget(self.label_47, 5, 1, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 4, 6, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 3, 7, 1, 1)
###
        self.pushButton.clicked.connect(self.call)
        self.pushButton_1.clicked.connect(self.call_1)
        self.pushButton_2.clicked.connect(self.call_2)
        
###
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Basuso"))
        
        self.pushButton.setText(_translate("Form", "Решение"))
        self.pushButton_1.setText(_translate("Form", "Очистить"))
        self.pushButton_2.setText(_translate("Form", "Пример"))
        
        self.label_1.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "0"))
        self.label_8.setText(_translate("Form", "0"))
        self.label_9.setText(_translate("Form", "0"))
        self.label_10.setText(_translate("Form", "0"))
        self.label_11.setText(_translate("Form", "0"))
        self.label_12.setText(_translate("Form", "0"))
        self.label_13.setText(_translate("Form", "0"))
        self.label_14.setText(_translate("Form", "0"))
        self.label_15.setText(_translate("Form", "0"))
        self.label_16.setText(_translate("Form", "0"))
        self.label_17.setText(_translate("Form", "0"))
        self.label_18.setText(_translate("Form", "0"))
        self.label_19.setText(_translate("Form", "0"))
        self.label_20.setText(_translate("Form", "0"))
        self.label_21.setText(_translate("Form", "0"))
        self.label_22.setText(_translate("Form", "0"))
        self.label_23.setText(_translate("Form", "0"))
        self.label_24.setText(_translate("Form", "0"))
        self.label_25.setText(_translate("Form", "0"))
        self.label_26.setText(_translate("Form", "0"))
        self.label_27.setText(_translate("Form", "0"))
        self.label_28.setText(_translate("Form", "0"))
        self.label_29.setText(_translate("Form", "0"))
        self.label_30.setText(_translate("Form", "0"))
        self.label_31.setText(_translate("Form", "0"))
        self.label_32.setText(_translate("Form", "0"))
        self.label_33.setText(_translate("Form", "0"))
        self.label_34.setText(_translate("Form", "0"))
        self.label_35.setText(_translate("Form", "0"))
        self.label_36.setText(_translate("Form", "0"))
        self.label_37.setText(_translate("Form", "0"))
        self.label_38.setText(_translate("Form", "0"))
        self.label_39.setText(_translate("Form", "0"))
        self.label_40.setText(_translate("Form", "0"))
        self.label_41.setText(_translate("Form", "0"))
        self.label_42.setText(_translate("Form", "0"))
        self.label_43.setText(_translate("Form", "0"))
        self.label_44.setText(_translate("Form", "0"))
        self.label_45.setText(_translate("Form", "0"))
        self.label_46.setText(_translate("Form", "0"))
        self.label_47.setText(_translate("Form", "0"))
        self.label_48.setText(_translate("Form", "0"))
        self.label_49.setText(_translate("Form", "0"))
        self.label_50.setText(_translate("Form", "0"))
        self.label_51.setText(_translate("Form", "0"))
        self.label_52.setText(_translate("Form", "0"))
        self.label_53.setText(_translate("Form", "0"))
        self.label_54.setText(_translate("Form", "0"))
        self.label_55.setText(_translate("Form", "0"))
        self.label_56.setText(_translate("Form", "0"))
        self.label_57.setText(_translate("Form", "0"))
        self.label_58.setText(_translate("Form", "0"))
        self.label_59.setText(_translate("Form", "0"))
        self.label_60.setText(_translate("Form", "0"))
        self.label_61.setText(_translate("Form", "0"))
        self.label_62.setText(_translate("Form", "0"))
        self.label_63.setText(_translate("Form", "0"))
        self.label_64.setText(_translate("Form", "0"))
        self.label_65.setText(_translate("Form", "0"))
        self.label_66.setText(_translate("Form", "0"))
        self.label_67.setText(_translate("Form", "0"))
        self.label_68.setText(_translate("Form", "0"))
        self.label_69.setText(_translate("Form", "0"))
        self.label_70.setText(_translate("Form", "0"))
        self.label_71.setText(_translate("Form", "0"))
        self.label_72.setText(_translate("Form", "0"))
        self.label_73.setText(_translate("Form", "0"))
        self.label_74.setText(_translate("Form", "0"))
        self.label_75.setText(_translate("Form", "0"))
        self.label_76.setText(_translate("Form", "0"))
        self.label_77.setText(_translate("Form", "0"))
        self.label_78.setText(_translate("Form", "0"))
        self.label_79.setText(_translate("Form", "0"))
        self.label_80.setText(_translate("Form", "0"))
        self.label_81.setText(_translate("Form", "0"))

    def call_2(self):
        self.lineEdit_3.setText('6')
        self.lineEdit_6.setText('5')
        self.lineEdit_12.setText('2')
        self.lineEdit_13.setText('1')
        self.lineEdit_18.setText('6')
        self.lineEdit_19.setText('8')
        self.lineEdit_20.setText('1')
        self.lineEdit_24.setText('6')
        self.lineEdit_25.setText('3')
        self.lineEdit_27.setText('5')
        self.lineEdit_28.setText('4')
        self.lineEdit_30.setText('1')
        self.lineEdit_34.setText('5')
        self.lineEdit_37.setText('3')
        self.lineEdit_38.setText('2')
        self.lineEdit_43.setText('4')
        self.lineEdit_46.setText('9')
        self.lineEdit_53.setText('2')
        self.lineEdit_58.setText('2')
        self.lineEdit_61.setText('8')
        self.lineEdit_62.setText('4')
        self.lineEdit_68.setText('4')
        self.lineEdit_69.setText('1')
        self.lineEdit_71.setText('3')
        self.lineEdit_77.setText('8')
        self.lineEdit_78.setText('3')
        self.lineEdit_79.setText('6')

    def call_1(self):
        self.lineEdit_3.setText('')
        su = 0
        while su <= 80:
            su += 1
            #print(su)
            eval(f'self.lineEdit_{su}.clear()')
            #d1 = eval(f'self.label_{i}.setText('')')#выполняем команду прописаную в скобках и получаем значение которое присваеваем переменной d1


    def call(self):
        sf = []
        strok_1 = []
        strok_2 = []
        strok_3 = []
        strok_4 = []
        strok_5 = []
        strok_6 = []
        strok_7 = []
        strok_8 = []
        strok_9 = []
        i = 0
        while i <= 80:
            i += 1
            self.label_1.setText('')
            #ris = eval(f'self.lineEdit_{i}.text()')
            d1 = eval(f'self.lineEdit_{i}.text()')#выполняем команду прописаную в скобках и получаем значение которое присваеваем переменной d1
            if d1 == "":
                d1 = 0
                sf.append(d1)
            else:
                sf.append(d1)
            

        re_sf = str(sf).replace("'", '').replace("[", '').replace("]", '').replace(",", '')
        ree_sf = re.sub('[^0-9]', '', re_sf).strip()
        sfD = len(list(ree_sf))
        #print(sfD)

        if sfD == 81:
            #print('go') 

            for n in range(0,9):
                strok_1.append(int(sf[n]))

            for g in range(9,18):
                strok_2.append(int(sf[g]))

            for j in range(18,27):
                strok_3.append(int(sf[j]))

            for w in range(27,36):
                strok_4.append(int(sf[w]))

            for cx in range(36,45):
                strok_5.append(int(sf[cx]))

            for xv in range(45,54):
                strok_6.append(int(sf[xv]))

            for xvi in range(54,63):
                strok_7.append(int(sf[xvi]))

            for xmi in range(63,72):
                strok_8.append(int(sf[xmi]))

            for xdi in range(72,81):
                strok_9.append(int(sf[xdi]))

            Lgrid = (strok_1,strok_2,strok_3,strok_4,strok_5,strok_6,strok_7,strok_8,strok_9)
            grid = list(Lgrid)

            M = 9
            def puzzleee(a):
                self.label_1.setText(str(a[0][0]))
                self.label_2.setText(str(a[0][1]))
                self.label_3.setText(str(a[0][2]))
                self.label_4.setText(str(a[0][3]))
                self.label_5.setText(str(a[0][4]))
                self.label_6.setText(str(a[0][5]))
                self.label_7.setText(str(a[0][6]))
                self.label_8.setText(str(a[0][7]))
                self.label_9.setText(str(a[0][8]))

                self.label_10.setText(str(a[1][0]))
                self.label_11.setText(str(a[1][1]))
                self.label_12.setText(str(a[1][2]))
                self.label_13.setText(str(a[1][3]))
                self.label_14.setText(str(a[1][4]))
                self.label_15.setText(str(a[1][5]))
                self.label_16.setText(str(a[1][6]))
                self.label_17.setText(str(a[1][7]))
                self.label_18.setText(str(a[1][8]))

                self.label_19.setText(str(a[2][0]))
                self.label_20.setText(str(a[2][1]))
                self.label_21.setText(str(a[2][2]))
                self.label_22.setText(str(a[2][3]))
                self.label_23.setText(str(a[2][4]))
                self.label_24.setText(str(a[2][5]))
                self.label_25.setText(str(a[2][6]))
                self.label_26.setText(str(a[2][7]))
                self.label_27.setText(str(a[2][8]))

                self.label_28.setText(str(a[3][0]))
                self.label_29.setText(str(a[3][1]))
                self.label_30.setText(str(a[3][2]))
                self.label_31.setText(str(a[3][3]))
                self.label_32.setText(str(a[3][4]))
                self.label_33.setText(str(a[3][5]))
                self.label_34.setText(str(a[3][6]))
                self.label_35.setText(str(a[3][7]))
                self.label_36.setText(str(a[3][8]))

                self.label_37.setText(str(a[4][0]))
                self.label_38.setText(str(a[4][1]))
                self.label_39.setText(str(a[4][2]))
                self.label_40.setText(str(a[4][3]))
                self.label_41.setText(str(a[4][4]))
                self.label_42.setText(str(a[4][5]))
                self.label_43.setText(str(a[4][6]))
                self.label_44.setText(str(a[4][7]))
                self.label_45.setText(str(a[4][8]))

                self.label_46.setText(str(a[5][0]))
                self.label_47.setText(str(a[5][1]))
                self.label_48.setText(str(a[5][2]))
                self.label_49.setText(str(a[5][3]))
                self.label_50.setText(str(a[5][4]))
                self.label_51.setText(str(a[5][5]))
                self.label_52.setText(str(a[5][6]))
                self.label_53.setText(str(a[5][7]))
                self.label_54.setText(str(a[5][8]))

                self.label_55.setText(str(a[6][0]))
                self.label_56.setText(str(a[6][1]))
                self.label_57.setText(str(a[6][2]))
                self.label_58.setText(str(a[6][3]))
                self.label_59.setText(str(a[6][4]))
                self.label_60.setText(str(a[6][5]))
                self.label_61.setText(str(a[6][6]))
                self.label_62.setText(str(a[6][7]))
                self.label_63.setText(str(a[6][8]))

                self.label_64.setText(str(a[7][0]))
                self.label_65.setText(str(a[7][1]))
                self.label_66.setText(str(a[7][2]))
                self.label_67.setText(str(a[7][3]))
                self.label_68.setText(str(a[7][4]))
                self.label_69.setText(str(a[7][5]))
                self.label_70.setText(str(a[7][6]))
                self.label_71.setText(str(a[7][7]))
                self.label_72.setText(str(a[7][8]))

                self.label_73.setText(str(a[8][0]))
                self.label_74.setText(str(a[8][1]))
                self.label_75.setText(str(a[8][2]))
                self.label_76.setText(str(a[8][3]))
                self.label_77.setText(str(a[8][4]))
                self.label_78.setText(str(a[8][5]))
                self.label_79.setText(str(a[8][6]))
                self.label_80.setText(str(a[8][7]))
                self.label_81.setText(str(a[8][8]))
                
            def puzzle(a):
                global list_2
                for i in range(M):
                    for j in range(M):
                        print(a[i][j],end = " ")
                    print()
            def solve(grid, row, col, num):
                for x in range(9):
                    if grid[row][x] == num:
                        return False
                         
                for x in range(9):
                    if grid[x][col] == num:
                        return False
             
                startRow = row - row % 3
                startCol = col - col % 3
                for i in range(3):
                    for j in range(3):
                        if grid[i + startRow][j + startCol] == num:
                            return False
                return True
             
            def Suduko(grid, row, col):
             
                if (row == M - 1 and col == M):
                    return True
                if col == M:
                    row += 1
                    col = 0
                if grid[row][col] > 0:
                    return Suduko(grid, row, col + 1)
                for num in range(1, M + 1, 1):
                    #print(f'{num}')
                 
                    if solve(grid, row, col, num):
                     
                        grid[row][col] = num
                        if Suduko(grid, row, col + 1):
                            return True
                    grid[row][col] = 0
                return False

            if (Suduko(grid, 0, 0)):
                puzzleee(grid)

            #else:
                #print('no')
        #else:
            #print('no1')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
