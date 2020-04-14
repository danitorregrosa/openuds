# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup-dialog-unmanaged.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UdsActorSetupDialog(object):
    def setupUi(self, UdsActorSetupDialog):
        UdsActorSetupDialog.setObjectName("UdsActorSetupDialog")
        UdsActorSetupDialog.setWindowModality(QtCore.Qt.WindowModal)
        UdsActorSetupDialog.resize(595, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UdsActorSetupDialog.sizePolicy().hasHeightForWidth())
        UdsActorSetupDialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        UdsActorSetupDialog.setFont(font)
        UdsActorSetupDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/uds-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UdsActorSetupDialog.setWindowIcon(icon)
        UdsActorSetupDialog.setAutoFillBackground(False)
        UdsActorSetupDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        UdsActorSetupDialog.setSizeGripEnabled(False)
        UdsActorSetupDialog.setModal(True)
        self.saveButton = QtWidgets.QPushButton(UdsActorSetupDialog)
        self.saveButton.setEnabled(True)
        self.saveButton.setGeometry(QtCore.QRect(10, 180, 181, 23))
        self.saveButton.setMinimumSize(QtCore.QSize(181, 0))
        self.saveButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.saveButton.setObjectName("saveButton")
        self.closeButton = QtWidgets.QPushButton(UdsActorSetupDialog)
        self.closeButton.setGeometry(QtCore.QRect(410, 180, 171, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(171, 0))
        self.closeButton.setObjectName("closeButton")
        self.testButton = QtWidgets.QPushButton(UdsActorSetupDialog)
        self.testButton.setEnabled(False)
        self.testButton.setGeometry(QtCore.QRect(210, 180, 181, 23))
        self.testButton.setMinimumSize(QtCore.QSize(181, 0))
        self.testButton.setObjectName("testButton")
        self.layoutWidget = QtWidgets.QWidget(UdsActorSetupDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(16)
        self.formLayout.setObjectName("formLayout")
        self.label_security = QtWidgets.QLabel(self.layoutWidget)
        self.label_security.setObjectName("label_security")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_security)
        self.validateCertificate = QtWidgets.QComboBox(self.layoutWidget)
        self.validateCertificate.setObjectName("validateCertificate")
        self.validateCertificate.addItem("")
        self.validateCertificate.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.validateCertificate)
        self.label_host = QtWidgets.QLabel(self.layoutWidget)
        self.label_host.setObjectName("label_host")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_host)
        self.host = QtWidgets.QLineEdit(self.layoutWidget)
        self.host.setAcceptDrops(False)
        self.host.setObjectName("host")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.host)
        self.label_serviceToken = QtWidgets.QLabel(self.layoutWidget)
        self.label_serviceToken.setObjectName("label_serviceToken")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_serviceToken)
        self.serviceToken = QtWidgets.QLineEdit(self.layoutWidget)
        self.serviceToken.setObjectName("serviceToken")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.serviceToken)
        self.label_loglevel = QtWidgets.QLabel(self.layoutWidget)
        self.label_loglevel.setObjectName("label_loglevel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_loglevel)
        self.logLevelComboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.logLevelComboBox.setFrame(True)
        self.logLevelComboBox.setObjectName("logLevelComboBox")
        self.logLevelComboBox.addItem("")
        self.logLevelComboBox.setItemText(0, "DEBUG")
        self.logLevelComboBox.addItem("")
        self.logLevelComboBox.setItemText(1, "INFO")
        self.logLevelComboBox.addItem("")
        self.logLevelComboBox.setItemText(2, "ERROR")
        self.logLevelComboBox.addItem("")
        self.logLevelComboBox.setItemText(3, "FATAL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.logLevelComboBox)
        self.label_host.raise_()
        self.host.raise_()
        self.label_serviceToken.raise_()
        self.serviceToken.raise_()
        self.validateCertificate.raise_()
        self.label_security.raise_()
        self.label_loglevel.raise_()
        self.logLevelComboBox.raise_()

        self.retranslateUi(UdsActorSetupDialog)
        self.logLevelComboBox.setCurrentIndex(1)
        self.closeButton.clicked.connect(UdsActorSetupDialog.finish)
        self.testButton.clicked.connect(UdsActorSetupDialog.testUDSServer)
        self.saveButton.clicked.connect(UdsActorSetupDialog.saveConfig)
        self.host.textChanged['QString'].connect(UdsActorSetupDialog.configChanged)
        self.serviceToken.textChanged['QString'].connect(UdsActorSetupDialog.configChanged)
        QtCore.QMetaObject.connectSlotsByName(UdsActorSetupDialog)

    def retranslateUi(self, UdsActorSetupDialog):
        _translate = QtCore.QCoreApplication.translate
        UdsActorSetupDialog.setWindowTitle(_translate("UdsActorSetupDialog", "UDS Actor Configuration Tool"))
        self.saveButton.setToolTip(_translate("UdsActorSetupDialog", "Click to register Actor with UDS Broker"))
        self.saveButton.setWhatsThis(_translate("UdsActorSetupDialog", "<html><head/><body><p>Click on this button to register Actor with UDS Broker.</p></body></html>"))
        self.saveButton.setText(_translate("UdsActorSetupDialog", "Save Configuration"))
        self.closeButton.setToolTip(_translate("UdsActorSetupDialog", "Closes UDS Actor Configuration (discard pending changes if any)"))
        self.closeButton.setWhatsThis(_translate("UdsActorSetupDialog", "<html><head/><body><p>Exits the UDS Actor Configuration Tool</p></body></html>"))
        self.closeButton.setText(_translate("UdsActorSetupDialog", "Close"))
        self.testButton.setToolTip(_translate("UdsActorSetupDialog", "Click to test existing configuration (disabled if no config found)"))
        self.testButton.setWhatsThis(_translate("UdsActorSetupDialog", "<html><head/><body><p>Click on this button to test the server host and assigned toen.</p></body></html>"))
        self.testButton.setText(_translate("UdsActorSetupDialog", "Test configuration"))
        self.label_security.setText(_translate("UdsActorSetupDialog", "SSL Validation"))
        self.validateCertificate.setToolTip(_translate("UdsActorSetupDialog", "Select communication security with broker"))
        self.validateCertificate.setWhatsThis(_translate("UdsActorSetupDialog", "<html><head/><body><p>Select the security for communications with UDS Broker.</p><p>The recommended method of communication is <span style=\" font-weight:600;\">Use SSL</span>, but selection needs to be acording to your broker configuration.</p></body></html>"))
        self.validateCertificate.setItemText(0, _translate("UdsActorSetupDialog", "Ignore certificate"))
        self.validateCertificate.setItemText(1, _translate("UdsActorSetupDialog", "Verify certificate"))
        self.label_host.setText(_translate("UdsActorSetupDialog", "UDS Server"))
        self.host.setToolTip(_translate("UdsActorSetupDialog", "Uds Broker Server Addres. Use IP or FQDN"))
        self.host.setWhatsThis(_translate("UdsActorSetupDialog", "Enter here the UDS Broker Addres using either its IP address or its FQDN address"))
        self.label_serviceToken.setText(_translate("UdsActorSetupDialog", "Service Token"))
        self.serviceToken.setToolTip(_translate("UdsActorSetupDialog", "UDS user with administration rights (Will not be stored on template)"))
        self.serviceToken.setWhatsThis(_translate("UdsActorSetupDialog", "<html><head/><body><p>Administrator user on UDS Server.</p><p>Note: This credential will not be stored on client. Will be used to obtain an unique token for this image.</p></body></html>"))
        self.label_loglevel.setText(_translate("UdsActorSetupDialog", "Log Level"))
from ui import uds_rc