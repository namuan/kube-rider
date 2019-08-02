# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/pod_volume_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PodVolumeWidget(object):
    def setupUi(self, PodVolumeWidget):
        PodVolumeWidget.setObjectName("PodVolumeWidget")
        PodVolumeWidget.resize(423, 85)
        PodVolumeWidget.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(PodVolumeWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_volume_name = QtWidgets.QLabel(PodVolumeWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_volume_name.setFont(font)
        self.lbl_volume_name.setObjectName("lbl_volume_name")
        self.horizontalLayout_2.addWidget(self.lbl_volume_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.lbl_mount_path = QtWidgets.QLabel(PodVolumeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_mount_path.setFont(font)
        self.lbl_mount_path.setObjectName("lbl_mount_path")
        self.verticalLayout.addWidget(self.lbl_mount_path)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(PodVolumeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lbl_volumes = QtWidgets.QLabel(PodVolumeWidget)
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

        self.retranslateUi(PodVolumeWidget)
        QtCore.QMetaObject.connectSlotsByName(PodVolumeWidget)

    def retranslateUi(self, PodVolumeWidget):
        _translate = QtCore.QCoreApplication.translate
        PodVolumeWidget.setWindowTitle(_translate("PodVolumeWidget", "Form"))
        self.lbl_volume_name.setText(_translate("PodVolumeWidget", "TextLabel"))
        self.lbl_mount_path.setText(_translate("PodVolumeWidget", "image path"))
        self.label_2.setText(_translate("PodVolumeWidget", "Volumes:"))
        self.lbl_volumes.setText(_translate("PodVolumeWidget", "TextLabel"))


