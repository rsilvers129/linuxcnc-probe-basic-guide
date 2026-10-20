# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_user_buttons.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

from qtpyvcp.widgets.button_widgets.action_button import ActionButton

class Ui_USER_BUTTONS(object):
    def setupUi(self, USER_BUTTONS):
        if not USER_BUTTONS.objectName():
            USER_BUTTONS.setObjectName(u"USER_BUTTONS")
        USER_BUTTONS.resize(285, 196)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(USER_BUTTONS.sizePolicy().hasHeightForWidth())
        USER_BUTTONS.setSizePolicy(sizePolicy)
        USER_BUTTONS.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout = QGridLayout(USER_BUTTONS)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(1, 3, 1, 1)
        self.block_delete_button = ActionButton(USER_BUTTONS)
        self.block_delete_button.setObjectName(u"block_delete_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.block_delete_button.sizePolicy().hasHeightForWidth())
        self.block_delete_button.setSizePolicy(sizePolicy1)
        self.block_delete_button.setMinimumSize(QSize(135, 42))
        self.block_delete_button.setMaximumSize(QSize(16777215, 42))
        self.block_delete_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.block_delete_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.block_delete_button.setCheckable(True)

        self.gridLayout.addWidget(self.block_delete_button, 2, 2, 1, 1)

        self.m01_break_button = ActionButton(USER_BUTTONS)
        self.m01_break_button.setObjectName(u"m01_break_button")
        sizePolicy1.setHeightForWidth(self.m01_break_button.sizePolicy().hasHeightForWidth())
        self.m01_break_button.setSizePolicy(sizePolicy1)
        self.m01_break_button.setMinimumSize(QSize(135, 42))
        self.m01_break_button.setMaximumSize(QSize(16777215, 42))
        self.m01_break_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.m01_break_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.m01_break_button.setCheckable(True)

        self.gridLayout.addWidget(self.m01_break_button, 3, 2, 1, 1)

        self.flood_button = ActionButton(USER_BUTTONS)
        self.flood_button.setObjectName(u"flood_button")
        sizePolicy1.setHeightForWidth(self.flood_button.sizePolicy().hasHeightForWidth())
        self.flood_button.setSizePolicy(sizePolicy1)
        self.flood_button.setMinimumSize(QSize(135, 42))
        self.flood_button.setMaximumSize(QSize(16777215, 42))
        self.flood_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.flood_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.flood_button.setCheckable(True)

        self.gridLayout.addWidget(self.flood_button, 2, 0, 1, 1)

        self.single_block_button = ActionButton(USER_BUTTONS)
        self.single_block_button.setObjectName(u"single_block_button")
        sizePolicy1.setHeightForWidth(self.single_block_button.sizePolicy().hasHeightForWidth())
        self.single_block_button.setSizePolicy(sizePolicy1)
        self.single_block_button.setMinimumSize(QSize(135, 42))
        self.single_block_button.setMaximumSize(QSize(16777215, 42))
        self.single_block_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.single_block_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.gridLayout.addWidget(self.single_block_button, 1, 2, 1, 1)

        self.mist_button = ActionButton(USER_BUTTONS)
        self.mist_button.setObjectName(u"mist_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mist_button.sizePolicy().hasHeightForWidth())
        self.mist_button.setSizePolicy(sizePolicy2)
        self.mist_button.setMinimumSize(QSize(135, 42))
        self.mist_button.setMaximumSize(QSize(16777215, 42))
        self.mist_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.mist_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.mist_button.setCheckable(True)

        self.gridLayout.addWidget(self.mist_button, 3, 0, 1, 1)

        self.feed_hold_button = ActionButton(USER_BUTTONS)
        self.feed_hold_button.setObjectName(u"feed_hold_button")
        sizePolicy1.setHeightForWidth(self.feed_hold_button.sizePolicy().hasHeightForWidth())
        self.feed_hold_button.setSizePolicy(sizePolicy1)
        self.feed_hold_button.setMinimumSize(QSize(135, 42))
        self.feed_hold_button.setMaximumSize(QSize(16777215, 42))
        self.feed_hold_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.feed_hold_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.feed_hold_button.setCheckable(True)

        self.gridLayout.addWidget(self.feed_hold_button, 0, 2, 1, 1)

        self.clear_program_button = ActionButton(USER_BUTTONS)
        self.clear_program_button.setObjectName(u"clear_program_button")
        sizePolicy1.setHeightForWidth(self.clear_program_button.sizePolicy().hasHeightForWidth())
        self.clear_program_button.setSizePolicy(sizePolicy1)
        self.clear_program_button.setMinimumSize(QSize(135, 42))
        self.clear_program_button.setMaximumSize(QSize(16777215, 42))
        self.clear_program_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.clear_program_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.clear_program_button.setCheckable(False)

        self.gridLayout.addWidget(self.clear_program_button, 1, 0, 1, 1)

        self.reload_program_button = ActionButton(USER_BUTTONS)
        self.reload_program_button.setObjectName(u"reload_program_button")
        sizePolicy1.setHeightForWidth(self.reload_program_button.sizePolicy().hasHeightForWidth())
        self.reload_program_button.setSizePolicy(sizePolicy1)
        self.reload_program_button.setMinimumSize(QSize(135, 42))
        self.reload_program_button.setMaximumSize(QSize(16777215, 42))
        self.reload_program_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.reload_program_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.reload_program_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.reload_program_button.setCheckable(False)

        self.gridLayout.addWidget(self.reload_program_button, 0, 0, 1, 1)

        self.label = QLabel(USER_BUTTONS)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(USER_BUTTONS)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(USER_BUTTONS)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_4 = QLabel(USER_BUTTONS)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)


        self.retranslateUi(USER_BUTTONS)

        QMetaObject.connectSlotsByName(USER_BUTTONS)
    # setupUi

    def retranslateUi(self, USER_BUTTONS):
        USER_BUTTONS.setWindowTitle(QCoreApplication.translate("USER_BUTTONS", u"User Buttons", None))
        self.block_delete_button.setText(QCoreApplication.translate("USER_BUTTONS", u"BLOCK DELETE", None))
        self.block_delete_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"program.block-delete.toggle", None))
        self.m01_break_button.setText(QCoreApplication.translate("USER_BUTTONS", u"M01 BREAK", None))
        self.m01_break_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"program.optional-stop.toggle", None))
        self.flood_button.setText(QCoreApplication.translate("USER_BUTTONS", u"FLOOD", None))
        self.flood_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"coolant.flood.toggle", None))
        self.single_block_button.setText(QCoreApplication.translate("USER_BUTTONS", u"SINGLE BLOCK", None))
        self.single_block_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"program.step", None))
        self.mist_button.setText(QCoreApplication.translate("USER_BUTTONS", u"MIST", None))
        self.mist_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"coolant.mist.toggle", None))
        self.feed_hold_button.setText(QCoreApplication.translate("USER_BUTTONS", u"FEED HOLD", None))
        self.feed_hold_button.setProperty(u"rules", QCoreApplication.translate("USER_BUTTONS", u"[{\"channels\": [{\"url\": \"status:interp_state?text\", \"trigger\": true}], \"property\": \"Checked\", \"expression\": \"ch[0] == 'Paused'\", \"name\": \"check when paused\"}]", None))
        self.feed_hold_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"program.pause", None))
        self.clear_program_button.setText(QCoreApplication.translate("USER_BUTTONS", u"CLEAR PGM", None))
        self.clear_program_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"program.clear", None))
        self.reload_program_button.setText(QCoreApplication.translate("USER_BUTTONS", u"RELOAD PGM", None))
        self.reload_program_button.setProperty(u"actionName", QCoreApplication.translate("USER_BUTTONS", u"program.reload", None))
    # retranslateUi

