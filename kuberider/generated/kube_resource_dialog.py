# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/kube_resource_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KubeResourceDialog(object):
    def setupUi(self, KubeResourceDialog):
        KubeResourceDialog.setObjectName("KubeResourceDialog")
        KubeResourceDialog.setWindowModality(QtCore.Qt.WindowModal)
        KubeResourceDialog.setEnabled(True)
        KubeResourceDialog.resize(746, 640)
        KubeResourceDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        KubeResourceDialog.setModal(True)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(KubeResourceDialog)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_resource_definition = QtWidgets.QPlainTextEdit(KubeResourceDialog)
        self.txt_resource_definition.setObjectName("txt_resource_definition")
        self.verticalLayout_2.addWidget(self.txt_resource_definition)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_command_output = QtWidgets.QLabel(KubeResourceDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_command_output.sizePolicy().hasHeightForWidth())
        self.lbl_command_output.setSizePolicy(sizePolicy)
        self.lbl_command_output.setObjectName("lbl_command_output")
        self.horizontalLayout.addWidget(self.lbl_command_output)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_apply_resource = QtWidgets.QPushButton(KubeResourceDialog)
        self.btn_apply_resource.setObjectName("btn_apply_resource")
        self.verticalLayout.addWidget(self.btn_apply_resource)
        self.btn_close_dialog = QtWidgets.QPushButton(KubeResourceDialog)
        self.btn_close_dialog.setObjectName("btn_close_dialog")
        self.verticalLayout.addWidget(self.btn_close_dialog)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(KubeResourceDialog)
        QtCore.QMetaObject.connectSlotsByName(KubeResourceDialog)

    def retranslateUi(self, KubeResourceDialog):
        _translate = QtCore.QCoreApplication.translate
        KubeResourceDialog.setWindowTitle(_translate("KubeResourceDialog", "Progress ..."))
        self.txt_resource_definition.setPlainText(_translate("KubeResourceDialog", "<< Kube definition >>"))
        self.lbl_command_output.setText(_translate("KubeResourceDialog", "<< Status >>"))
        self.btn_apply_resource.setText(_translate("KubeResourceDialog", "Apply"))
        self.btn_close_dialog.setText(_translate("KubeResourceDialog", "Close"))


