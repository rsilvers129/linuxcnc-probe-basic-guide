# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_user_rack_atc_buttons.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton

class Ui_USER_ATC_BUTTONS(object):
    def setupUi(self, USER_ATC_BUTTONS):
        if not USER_ATC_BUTTONS.objectName():
            USER_ATC_BUTTONS.setObjectName(u"USER_ATC_BUTTONS")
        USER_ATC_BUTTONS.resize(300, 429)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(USER_ATC_BUTTONS.sizePolicy().hasHeightForWidth())
        USER_ATC_BUTTONS.setSizePolicy(sizePolicy)
        USER_ATC_BUTTONS.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(USER_ATC_BUTTONS)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(USER_ATC_BUTTONS)
        self.frame_64.setObjectName(u"frame_64")
        sizePolicy.setHeightForWidth(self.frame_64.sizePolicy().hasHeightForWidth())
        self.frame_64.setSizePolicy(sizePolicy)
        self.frame_64.setMaximumSize(QSize(300, 16777215))
        self.frame_64.setStyleSheet(u"")
        self.verticalLayout_66 = QVBoxLayout(self.frame_64)
        self.verticalLayout_66.setSpacing(16)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(20, 18, 20, 18)
        self.work_column_header_8 = QLabel(self.frame_64)
        self.work_column_header_8.setObjectName(u"work_column_header_8")
        self.work_column_header_8.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.work_column_header_8.sizePolicy().hasHeightForWidth())
        self.work_column_header_8.setSizePolicy(sizePolicy1)
        self.work_column_header_8.setMinimumSize(QSize(0, 38))
        self.work_column_header_8.setMaximumSize(QSize(16777215, 38))
        self.work_column_header_8.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.work_column_header_8.setFrameShape(QFrame.NoFrame)
        self.work_column_header_8.setAlignment(Qt.AlignCenter)
        self.work_column_header_8.setWordWrap(True)
        self.work_column_header_8.setIndent(0)

        self.verticalLayout_66.addWidget(self.work_column_header_8)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setSpacing(15)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(2, 2, 2, 2)
        self.reference_carousel_3 = MDIButton(self.frame_64)
        self.reference_carousel_3.setObjectName(u"reference_carousel_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.reference_carousel_3.sizePolicy().hasHeightForWidth())
        self.reference_carousel_3.setSizePolicy(sizePolicy2)
        self.reference_carousel_3.setMinimumSize(QSize(120, 45))
        self.reference_carousel_3.setMaximumSize(QSize(16777215, 45))
        self.reference_carousel_3.setFocusPolicy(Qt.NoFocus)
        self.reference_carousel_3.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.reference_carousel_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_119.addWidget(self.reference_carousel_3)

        self.reference_carousel_4 = MDIButton(self.frame_64)
        self.reference_carousel_4.setObjectName(u"reference_carousel_4")
        sizePolicy2.setHeightForWidth(self.reference_carousel_4.sizePolicy().hasHeightForWidth())
        self.reference_carousel_4.setSizePolicy(sizePolicy2)
        self.reference_carousel_4.setMinimumSize(QSize(120, 45))
        self.reference_carousel_4.setMaximumSize(QSize(16777215, 45))
        self.reference_carousel_4.setFocusPolicy(Qt.NoFocus)
        self.reference_carousel_4.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.reference_carousel_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_119.addWidget(self.reference_carousel_4)


        self.verticalLayout_66.addLayout(self.horizontalLayout_119)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setSpacing(15)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(2, 2, 2, 2)
        self.clamp_tool_button = SubCallButton(self.frame_64)
        self.clamp_tool_button.setObjectName(u"clamp_tool_button")
        sizePolicy2.setHeightForWidth(self.clamp_tool_button.sizePolicy().hasHeightForWidth())
        self.clamp_tool_button.setSizePolicy(sizePolicy2)
        self.clamp_tool_button.setMinimumSize(QSize(120, 45))
        self.clamp_tool_button.setMaximumSize(QSize(16777215, 45))
        self.clamp_tool_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_117.addWidget(self.clamp_tool_button)

        self.release_tool_button = SubCallButton(self.frame_64)
        self.release_tool_button.setObjectName(u"release_tool_button")
        self.release_tool_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.release_tool_button.sizePolicy().hasHeightForWidth())
        self.release_tool_button.setSizePolicy(sizePolicy2)
        self.release_tool_button.setMinimumSize(QSize(120, 45))
        self.release_tool_button.setMaximumSize(QSize(16777215, 45))
        self.release_tool_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_117.addWidget(self.release_tool_button)


        self.verticalLayout_66.addLayout(self.horizontalLayout_117)

        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setSpacing(15)
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.horizontalLayout_152.setContentsMargins(2, 2, 2, 2)
        self.spindle_orientation = SubCallButton(self.frame_64)
        self.spindle_orientation.setObjectName(u"spindle_orientation")
        sizePolicy2.setHeightForWidth(self.spindle_orientation.sizePolicy().hasHeightForWidth())
        self.spindle_orientation.setSizePolicy(sizePolicy2)
        self.spindle_orientation.setMinimumSize(QSize(120, 45))
        self.spindle_orientation.setMaximumSize(QSize(16777215, 45))
        self.spindle_orientation.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")
        self.spindle_orientation.setCheckable(True)

        self.horizontalLayout_152.addWidget(self.spindle_orientation)

        self.unlock_spindle = MDIButton(self.frame_64)
        self.unlock_spindle.setObjectName(u"unlock_spindle")
        sizePolicy2.setHeightForWidth(self.unlock_spindle.sizePolicy().hasHeightForWidth())
        self.unlock_spindle.setSizePolicy(sizePolicy2)
        self.unlock_spindle.setMinimumSize(QSize(120, 45))
        self.unlock_spindle.setMaximumSize(QSize(16777215, 45))
        self.unlock_spindle.setFocusPolicy(Qt.NoFocus)
        self.unlock_spindle.setLayoutDirection(Qt.RightToLeft)
        self.unlock_spindle.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.unlock_spindle.setIconSize(QSize(20, 20))

        self.horizontalLayout_152.addWidget(self.unlock_spindle)


        self.verticalLayout_66.addLayout(self.horizontalLayout_152)

        self.horizontalLayout_174 = QHBoxLayout()
        self.horizontalLayout_174.setSpacing(15)
        self.horizontalLayout_174.setObjectName(u"horizontalLayout_174")
        self.horizontalLayout_174.setContentsMargins(2, 2, 2, 2)
        self.move_head_above_carousel_button = SubCallButton(self.frame_64)
        self.move_head_above_carousel_button.setObjectName(u"move_head_above_carousel_button")
        sizePolicy2.setHeightForWidth(self.move_head_above_carousel_button.sizePolicy().hasHeightForWidth())
        self.move_head_above_carousel_button.setSizePolicy(sizePolicy2)
        self.move_head_above_carousel_button.setMinimumSize(QSize(120, 45))
        self.move_head_above_carousel_button.setMaximumSize(QSize(16777215, 45))
        self.move_head_above_carousel_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_174.addWidget(self.move_head_above_carousel_button)

        self.move_tool_to_carousel_height_button = SubCallButton(self.frame_64)
        self.move_tool_to_carousel_height_button.setObjectName(u"move_tool_to_carousel_height_button")
        sizePolicy2.setHeightForWidth(self.move_tool_to_carousel_height_button.sizePolicy().hasHeightForWidth())
        self.move_tool_to_carousel_height_button.setSizePolicy(sizePolicy2)
        self.move_tool_to_carousel_height_button.setMinimumSize(QSize(120, 45))
        self.move_tool_to_carousel_height_button.setMaximumSize(QSize(16777215, 45))
        self.move_tool_to_carousel_height_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.horizontalLayout_174.addWidget(self.move_tool_to_carousel_height_button)


        self.verticalLayout_66.addLayout(self.horizontalLayout_174)

        self.widget_10 = QWidget(self.frame_64)
        self.widget_10.setObjectName(u"widget_10")

        self.verticalLayout_66.addWidget(self.widget_10)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setSpacing(15)
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.horizontalLayout_159.setContentsMargins(2, 2, 2, 2)
        self.reference_carousel_2 = MDIButton(self.frame_64)
        self.reference_carousel_2.setObjectName(u"reference_carousel_2")
        sizePolicy2.setHeightForWidth(self.reference_carousel_2.sizePolicy().hasHeightForWidth())
        self.reference_carousel_2.setSizePolicy(sizePolicy2)
        self.reference_carousel_2.setMinimumSize(QSize(125, 45))
        self.reference_carousel_2.setMaximumSize(QSize(16777215, 45))
        self.reference_carousel_2.setFocusPolicy(Qt.NoFocus)
        self.reference_carousel_2.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.reference_carousel_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_159.addWidget(self.reference_carousel_2)


        self.verticalLayout_66.addLayout(self.horizontalLayout_159)


        self.verticalLayout.addWidget(self.frame_64)


        self.retranslateUi(USER_ATC_BUTTONS)

        QMetaObject.connectSlotsByName(USER_ATC_BUTTONS)
    # setupUi

    def retranslateUi(self, USER_ATC_BUTTONS):
        USER_ATC_BUTTONS.setWindowTitle(QCoreApplication.translate("USER_ATC_BUTTONS", u"User Atc Buttons", None))
        self.work_column_header_8.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"ATC MANUAL CONTROL PANEL", None))
#if QT_CONFIG(tooltip)
        self.reference_carousel_3.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.reference_carousel_3.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"AIR BLAST", None))
        self.reference_carousel_3.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M13", None))
#if QT_CONFIG(tooltip)
        self.reference_carousel_4.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.reference_carousel_4.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"RETR DUST BOOT", None))
        self.reference_carousel_4.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M13", None))
        self.clamp_tool_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"CLAMP TOOL", None))
        self.clamp_tool_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"clamptool.ngc", None))
        self.release_tool_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"RELEASE TOOL", None))
        self.release_tool_button.setProperty(u"rules", QCoreApplication.translate("USER_ATC_BUTTONS", u"[{\"name\": \"spindle safety\", \"property\": \"Enable\", \"expression\": \"not ch[0]\", \"channels\": [{\"url\": \"status:spindle.0.enabled\", \"trigger\": true}]}]", None))
        self.release_tool_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"unclamptool.ngc", None))
        self.spindle_orientation.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"ORIENT SPINDLE", None))
        self.spindle_orientation.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"orientspindle.ngc", None))
#if QT_CONFIG(tooltip)
        self.unlock_spindle.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M112 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.unlock_spindle.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"UNLOCK SPINDLE", None))
        self.unlock_spindle.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M5", None))
        self.move_head_above_carousel_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"HEAD UP", None))
        self.move_head_above_carousel_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"move_head_above_carousel.ngc", None))
        self.move_tool_to_carousel_height_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"HEAD DOWN", None))
        self.move_tool_to_carousel_height_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"move_tool_to_carousel_height.ngc", None))
#if QT_CONFIG(tooltip)
        self.reference_carousel_2.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.reference_carousel_2.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"REF RACK DATA", None))
        self.reference_carousel_2.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M13", None))
    # retranslateUi

