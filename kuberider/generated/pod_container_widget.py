# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/pod_container_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PodContainerWidget(object):
    def setupUi(self, PodContainerWidget):
        PodContainerWidget.setObjectName("PodContainerWidget")
        PodContainerWidget.resize(433, 92)
        PodContainerWidget.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(PodContainerWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_container_name = QtWidgets.QLabel(PodContainerWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_container_name.setFont(font)
        self.lbl_container_name.setObjectName("lbl_container_name")
        self.horizontalLayout_2.addWidget(self.lbl_container_name)
        self.lbl_container_started = QtWidgets.QLabel(PodContainerWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_container_started.setFont(font)
        self.lbl_container_started.setObjectName("lbl_container_started")
        self.horizontalLayout_2.addWidget(self.lbl_container_started)
        self.btn_open_logs = QtWidgets.QToolButton(PodContainerWidget)
        self.btn_open_logs.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btn_open_logs.setAutoRaise(True)
        self.btn_open_logs.setObjectName("btn_open_logs")
        self.horizontalLayout_2.addWidget(self.btn_open_logs)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lbl_container_image = QtWidgets.QLabel(PodContainerWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_container_image.setFont(font)
        self.lbl_container_image.setObjectName("lbl_container_image")
        self.verticalLayout.addWidget(self.lbl_container_image)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(PodContainerWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lbl_volumes = QtWidgets.QLabel(PodContainerWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_volumes.sizePolicy().hasHeightForWidth())
        self.lbl_volumes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_volumes.setFont(font)
        self.lbl_volumes.setObjectName("lbl_volumes")
        self.horizontalLayout.addWidget(self.lbl_volumes)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PodContainerWidget)
        QtCore.QMetaObject.connectSlotsByName(PodContainerWidget)

    def retranslateUi(self, PodContainerWidget):
        _translate = QtCore.QCoreApplication.translate
        PodContainerWidget.setWindowTitle(_translate("PodContainerWidget", "Form"))
        self.lbl_container_name.setText(_translate("PodContainerWidget", "TextLabel"))
        self.lbl_container_started.setText(_translate("PodContainerWidget", "TextLabel"))
        self.btn_open_logs.setText(_translate("PodContainerWidget", "Logs"))
        self.lbl_container_image.setText(_translate("PodContainerWidget", "image path"))
        self.label_2.setText(_translate("PodContainerWidget", "Volumes:"))
        self.lbl_volumes.setText(_translate("PodContainerWidget", "TextLabel"))


