# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/pod_logs_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PodLogsDialog(object):
    def setupUi(self, PodLogsDialog):
        PodLogsDialog.setObjectName("PodLogsDialog")
        PodLogsDialog.setWindowModality(QtCore.Qt.WindowModal)
        PodLogsDialog.setEnabled(True)
        PodLogsDialog.resize(622, 345)
        PodLogsDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        PodLogsDialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(PodLogsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_pod_logs = QtWidgets.QPlainTextEdit(PodLogsDialog)
        self.txt_pod_logs.setObjectName("txt_pod_logs")
        self.verticalLayout.addWidget(self.txt_pod_logs)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.chk_follow_logs = QtWidgets.QCheckBox(PodLogsDialog)
        self.chk_follow_logs.setObjectName("chk_follow_logs")
        self.horizontalLayout.addWidget(self.chk_follow_logs)
        self.btn_close_logs = QtWidgets.QPushButton(PodLogsDialog)
        self.btn_close_logs.setObjectName("btn_close_logs")
        self.horizontalLayout.addWidget(self.btn_close_logs)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PodLogsDialog)
        QtCore.QMetaObject.connectSlotsByName(PodLogsDialog)

    def retranslateUi(self, PodLogsDialog):
        _translate = QtCore.QCoreApplication.translate
        PodLogsDialog.setWindowTitle(_translate("PodLogsDialog", "Logs ..."))
        self.chk_follow_logs.setText(_translate("PodLogsDialog", "Follow"))
        self.btn_close_logs.setText(_translate("PodLogsDialog", "Close"))


