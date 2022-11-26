# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileWidgetDesign.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(620, 94)
        self.horizontalLayout_3 = QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.edtOldName = QLineEdit(Form)
        self.edtOldName.setObjectName(u"edtOldName")
        self.edtOldName.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.edtOldName)

        self.btnUp = QPushButton(Form)
        self.btnUp.setObjectName(u"btnUp")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.btnUp.sizePolicy().hasHeightForWidth())
        self.btnUp.setSizePolicy(sizePolicy)
        self.btnUp.setMinimumSize(QSize(25, 25))
        self.btnUp.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btnUp)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 12)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.edtNewName = QLineEdit(Form)
        self.edtNewName.setObjectName(u"edtNewName")
        self.edtNewName.setReadOnly(True)

        self.horizontalLayout.addWidget(self.edtNewName)

        self.btnDown = QPushButton(Form)
        self.btnDown.setObjectName(u"btnDown")
        sizePolicy.setHeightForWidth(self.btnDown.sizePolicy().hasHeightForWidth())
        self.btnDown.setSizePolicy(sizePolicy)
        self.btnDown.setMinimumSize(QSize(25, 25))
        self.btnDown.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.btnDown)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 12)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.btnDelete = QPushButton(Form)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(60, 60))

        self.horizontalLayout_3.addWidget(self.btnDelete)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0440\u043e\u0435 \u0438\u043c\u044f:", None))
        self.btnUp.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u043e\u0435 \u0438\u043c\u044f:", None))
        self.btnDown.setText("")
        self.btnDelete.setText("")
    # retranslateUi

