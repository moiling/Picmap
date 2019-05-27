# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiRouteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout.addWidget(self.webEngineView)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.optionFrame = QtWidgets.QFrame(self.frame)
        self.optionFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.optionFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.optionFrame.setObjectName("optionFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.optionFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startInfoLabel = QtWidgets.QLabel(self.optionFrame)
        self.startInfoLabel.setObjectName("startInfoLabel")
        self.horizontalLayout_2.addWidget(self.startInfoLabel)
        self.line = QtWidgets.QFrame(self.optionFrame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.optionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.startTimeEdit = QtWidgets.QLineEdit(self.optionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startTimeEdit.sizePolicy().hasHeightForWidth())
        self.startTimeEdit.setSizePolicy(sizePolicy)
        self.startTimeEdit.setObjectName("startTimeEdit")
        self.horizontalLayout_2.addWidget(self.startTimeEdit)
        self.line_2 = QtWidgets.QFrame(self.optionFrame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.selectStartFromMap = QtWidgets.QPushButton(self.optionFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectStartFromMap.sizePolicy().hasHeightForWidth())
        self.selectStartFromMap.setSizePolicy(sizePolicy)
        self.selectStartFromMap.setObjectName("selectStartFromMap")
        self.horizontalLayout_2.addWidget(self.selectStartFromMap)
        self.selectStartPic = QtWidgets.QPushButton(self.optionFrame)
        self.selectStartPic.setObjectName("selectStartPic")
        self.horizontalLayout_2.addWidget(self.selectStartPic)
        self.line_3 = QtWidgets.QFrame(self.optionFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.routeButton = QtWidgets.QPushButton(self.optionFrame)
        self.routeButton.setObjectName("routeButton")
        self.horizontalLayout_2.addWidget(self.routeButton)
        self.verticalLayout_2.addWidget(self.optionFrame)
        self.hintFrame = QtWidgets.QFrame(self.frame)
        self.hintFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hintFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hintFrame.setObjectName("hintFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.hintFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hintLabel = QtWidgets.QLabel(self.hintFrame)
        self.hintLabel.setObjectName("hintLabel")
        self.horizontalLayout.addWidget(self.hintLabel)
        self.okButton = QtWidgets.QPushButton(self.hintFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.hintFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout_2.addWidget(self.hintFrame)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "多点导航"))
        self.startInfoLabel.setText(_translate("MainWindow", "未选择出发点"))
        self.label_2.setText(_translate("MainWindow", "出发时间"))
        self.selectStartFromMap.setText(_translate("MainWindow", "从地图上选择出发点"))
        self.selectStartPic.setText(_translate("MainWindow", "第一张图片为出发点"))
        self.routeButton.setText(_translate("MainWindow", "规划"))
        self.hintLabel.setText(_translate("MainWindow", "TextLabel"))
        self.okButton.setText(_translate("MainWindow", "确定"))
        self.cancelButton.setText(_translate("MainWindow", "返回"))

from PyQt5 import QtWebEngineWidgets