# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guiRocketConfig.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,)
from PySide6.QtWidgets import ( QLabel, QLineEdit,)

class Ui_widget(object):
    def setupUi(self, widget):
        if not widget.objectName():
            widget.setObjectName(u"widget")
        widget.resize(209, 129)
        self.labelRocketName = QLabel(widget)
        self.labelRocketName.setObjectName(u"labelRocketName")
        self.labelRocketName.setGeometry(QRect(0, 15, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.labelRocketName.setFont(font)
        self.editRocketMass = QLineEdit(widget)
        self.editRocketMass.setObjectName(u"editRocketMass")
        self.editRocketMass.setGeometry(QRect(100, 50, 100, 20))
        self.labelRocketMass = QLabel(widget)
        self.labelRocketMass.setObjectName(u"labelRocketMass")
        self.labelRocketMass.setGeometry(QRect(0, 50, 100, 16))
        self.labelCoeDrag = QLabel(widget)
        self.labelCoeDrag.setObjectName(u"labelCoeDrag")
        self.labelCoeDrag.setGeometry(QRect(0, 75, 100, 16))
        self.labelDiameter = QLabel(widget)
        self.labelDiameter.setObjectName(u"labelDiameter")
        self.labelDiameter.setGeometry(QRect(0, 100, 100, 16))
        self.editCoeDrag = QLineEdit(widget)
        self.editCoeDrag.setObjectName(u"editCoeDrag")
        self.editCoeDrag.setGeometry(QRect(100, 75, 100, 20))
        self.editDiameter = QLineEdit(widget)
        self.editDiameter.setObjectName(u"editDiameter")
        self.editDiameter.setGeometry(QRect(100, 100, 100, 20))

        self.retranslateUi(widget)

        QMetaObject.connectSlotsByName(widget)
    # setupUi

    def retranslateUi(self, widget):
        widget.setWindowTitle(QCoreApplication.translate("widget", u"Form", None))
        self.labelRocketName.setText(QCoreApplication.translate("widget", u"Rocket Name:", None))
        self.labelRocketMass.setText(QCoreApplication.translate("widget", u"Rocket Mass (kg)", None))
        self.labelCoeDrag.setText(QCoreApplication.translate("widget", u"Cd", None))
        self.labelDiameter.setText(QCoreApplication.translate("widget", u"Diameter (m)", None))
    # retranslateUi

