# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_user_sb(object):
    def setupUi(self, user_sb):
        if not user_sb.objectName():
            user_sb.setObjectName(u"user_sb")
        user_sb.resize(179, 511)
        user_sb.setMaximumSize(QSize(179, 511))
        user_sb.setProperty(u"sidebar", True)

        self.retranslateUi(user_sb)

        QMetaObject.connectSlotsByName(user_sb)
    # setupUi

    def retranslateUi(self, user_sb):
        user_sb.setWindowTitle(QCoreApplication.translate("user_sb", u"Sidebar User Tab", None))
    # retranslateUi

