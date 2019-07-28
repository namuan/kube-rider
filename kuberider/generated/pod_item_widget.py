# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/pod_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PodItemWidget(object):
    def setupUi(self, PodItemWidget):
        PodItemWidget.setObjectName("PodItemWidget")
        PodItemWidget.resize(431, 74)
        PodItemWidget.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(PodItemWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_pod_name = QtWidgets.QLabel(PodItemWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_pod_name.setFont(font)
        self.lbl_pod_name.setObjectName("lbl_pod_name")
        self.horizontalLayout.addWidget(self.lbl_pod_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lbl_pod_count = QtWidgets.QLabel(PodItemWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)
        self.lbl_pod_count.setFont(font)
        self.lbl_pod_count.setObjectName("lbl_pod_count")
        self.horizontalLayout.addWidget(self.lbl_pod_count)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_pod_status = QtWidgets.QLabel(PodItemWidget)
        self.lbl_pod_status.setObjectName("lbl_pod_status")
        self.horizontalLayout_2.addWidget(self.lbl_pod_status)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(PodItemWidget)
        QtCore.QMetaObject.connectSlotsByName(PodItemWidget)

    def retranslateUi(self, PodItemWidget):
        _translate = QtCore.QCoreApplication.translate
        PodItemWidget.setWindowTitle(_translate("PodItemWidget", "Form"))
        self.lbl_pod_name.setText(_translate("PodItemWidget", "TextLabel"))
        self.lbl_pod_count.setText(_translate("PodItemWidget", "1/1"))
        self.lbl_pod_status.setText(_translate("PodItemWidget", "ContainerCreating"))


