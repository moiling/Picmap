# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolbar = QtWidgets.QWidget(self.centralwidget)
        self.toolbar.setMinimumSize(QtCore.QSize(0, 30))
        self.toolbar.setObjectName("toolbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.toolbar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sortLabel = QtWidgets.QLabel(self.toolbar)
        self.sortLabel.setObjectName("sortLabel")
        self.horizontalLayout.addWidget(self.sortLabel)
        self.sortComboBox = QtWidgets.QComboBox(self.toolbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortComboBox.sizePolicy().hasHeightForWidth())
        self.sortComboBox.setSizePolicy(sizePolicy)
        self.sortComboBox.setObjectName("sortComboBox")
        self.sortComboBox.addItem("")
        self.sortComboBox.addItem("")
        self.horizontalLayout.addWidget(self.sortComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.multiRouteButton = QtWidgets.QPushButton(self.toolbar)
        self.multiRouteButton.setEnabled(False)
        self.multiRouteButton.setObjectName("multiRouteButton")
        self.horizontalLayout.addWidget(self.multiRouteButton)
        self.verticalLayout.addWidget(self.toolbar)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 750, 357))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.hintFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hintFrame.sizePolicy().hasHeightForWidth())
        self.hintFrame.setSizePolicy(sizePolicy)
        self.hintFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hintFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hintFrame.setObjectName("hintFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.hintFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.hintLabel = QtWidgets.QLabel(self.hintFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hintLabel.sizePolicy().hasHeightForWidth())
        self.hintLabel.setSizePolicy(sizePolicy)
        self.hintLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hintLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hintLabel.setTextFormat(QtCore.Qt.AutoText)
        self.hintLabel.setScaledContents(False)
        self.hintLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hintLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.hintLabel.setObjectName("hintLabel")
        self.verticalLayout_4.addWidget(self.hintLabel)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.hintFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.detailWidget = QtWidgets.QWidget(self.centralwidget)
        self.detailWidget.setEnabled(True)
        self.detailWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.detailWidget.setObjectName("detailWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.detailWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.detailWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nameText = QtWidgets.QLabel(self.frame_3)
        self.nameText.setObjectName("nameText")
        self.verticalLayout_3.addWidget(self.nameText)
        self.urlText = QtWidgets.QLabel(self.frame_3)
        self.urlText.setObjectName("urlText")
        self.verticalLayout_3.addWidget(self.urlText)
        self.locationText = QtWidgets.QLabel(self.frame_3)
        self.locationText.setObjectName("locationText")
        self.verticalLayout_3.addWidget(self.locationText)
        self.timeText = QtWidgets.QLabel(self.frame_3)
        self.timeText.setObjectName("timeText")
        self.verticalLayout_3.addWidget(self.timeText)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.horizontalLayout_2.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.hiddenButton = QtWidgets.QToolButton(self.detailWidget)
        self.hiddenButton.setObjectName("hiddenButton")
        self.horizontalLayout_2.addWidget(self.hiddenButton)
        self.verticalLayout.addWidget(self.detailWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Picmap"))
        self.sortLabel.setText(_translate("MainWindow", "排序方式"))
        self.sortComboBox.setItemText(0, _translate("MainWindow", "时间"))
        self.sortComboBox.setItemText(1, _translate("MainWindow", "地点"))
        self.multiRouteButton.setText(_translate("MainWindow", "多点导航"))
        self.hintLabel.setText(_translate("MainWindow", "请拖入图片"))
        self.label.setText(_translate("MainWindow", "名称"))
        self.label_2.setText(_translate("MainWindow", "路径"))
        self.label_3.setText(_translate("MainWindow", "地址"))
        self.label_4.setText(_translate("MainWindow", "时间"))
        self.nameText.setText(_translate("MainWindow", "图片名"))
        self.urlText.setText(_translate("MainWindow", "C:/moi/图片名"))
        self.locationText.setText(_translate("MainWindow", "重庆"))
        self.timeText.setText(_translate("MainWindow", "2019/05/19"))
        self.hiddenButton.setText(_translate("MainWindow", "X"))

