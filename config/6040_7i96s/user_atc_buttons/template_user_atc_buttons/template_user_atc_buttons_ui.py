# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_user_atc_buttons.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton
import probe_basic_rc

class Ui_USER_ATC_BUTTONS(object):
    def setupUi(self, USER_ATC_BUTTONS):
        if not USER_ATC_BUTTONS.objectName():
            USER_ATC_BUTTONS.setObjectName(u"USER_ATC_BUTTONS")
        USER_ATC_BUTTONS.resize(300, 478)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(USER_ATC_BUTTONS.sizePolicy().hasHeightForWidth())
        USER_ATC_BUTTONS.setSizePolicy(sizePolicy)
        USER_ATC_BUTTONS.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout = QVBoxLayout(USER_ATC_BUTTONS)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_64 = QWidget(USER_ATC_BUTTONS)
        self.widget_64.setObjectName(u"widget_64")
        sizePolicy.setHeightForWidth(self.widget_64.sizePolicy().hasHeightForWidth())
        self.widget_64.setSizePolicy(sizePolicy)
        self.widget_64.setMinimumSize(QSize(300, 0))
        self.widget_64.setMaximumSize(QSize(300, 16777215))
        self.widget_64.setStyleSheet(u".QWidget {\n"
"    background-color: rgb(51, 57, 59);\n"
"    border-style: solid;\n"
"    border-color: rgb(186, 189, 182);\n"
"    border-width: 2px;\n"
"    border-radius: 6px;\n"
"}")
        self.verticalLayout_66 = QVBoxLayout(self.widget_64)
        self.verticalLayout_66.setSpacing(16)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(20, 18, 20, 21)
        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setSpacing(15)
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.horizontalLayout_115.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_115.setContentsMargins(2, 2, 2, 2)
        self.atc_rev_button = MDIButton(self.widget_64)
        self.atc_rev_button.setObjectName(u"atc_rev_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.atc_rev_button.sizePolicy().hasHeightForWidth())
        self.atc_rev_button.setSizePolicy(sizePolicy1)
        self.atc_rev_button.setMinimumSize(QSize(120, 45))
        self.atc_rev_button.setMaximumSize(QSize(16777215, 45))
        self.atc_rev_button.setMouseTracking(True)
        self.atc_rev_button.setTabletTracking(False)
        self.atc_rev_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.atc_rev_button.setToolTipDuration(-1)
        self.atc_rev_button.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/ccw_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.atc_rev_button.setIcon(icon)
        self.atc_rev_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_115.addWidget(self.atc_rev_button)

        self.atc_fwd_button = MDIButton(self.widget_64)
        self.atc_fwd_button.setObjectName(u"atc_fwd_button")
        sizePolicy1.setHeightForWidth(self.atc_fwd_button.sizePolicy().hasHeightForWidth())
        self.atc_fwd_button.setSizePolicy(sizePolicy1)
        self.atc_fwd_button.setMinimumSize(QSize(120, 45))
        self.atc_fwd_button.setMaximumSize(QSize(16777215, 45))
        self.atc_fwd_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.atc_fwd_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.atc_fwd_button.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/cw_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.atc_fwd_button.setIcon(icon1)
        self.atc_fwd_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_115.addWidget(self.atc_fwd_button)


        self.verticalLayout_66.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setSpacing(15)
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.horizontalLayout_116.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_116.setContentsMargins(2, 2, 2, 2)
        self.atc_retract_button = SubCallButton(self.widget_64)
        self.atc_retract_button.setObjectName(u"atc_retract_button")
        sizePolicy1.setHeightForWidth(self.atc_retract_button.sizePolicy().hasHeightForWidth())
        self.atc_retract_button.setSizePolicy(sizePolicy1)
        self.atc_retract_button.setMinimumSize(QSize(120, 45))
        self.atc_retract_button.setMaximumSize(QSize(16777215, 45))
        self.atc_retract_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.atc_retract_button.setStyleSheet(u"SubCallButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/images/left_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.atc_retract_button.setIcon(icon2)
        self.atc_retract_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_116.addWidget(self.atc_retract_button)

        self.atc_extend_button = SubCallButton(self.widget_64)
        self.atc_extend_button.setObjectName(u"atc_extend_button")
        sizePolicy1.setHeightForWidth(self.atc_extend_button.sizePolicy().hasHeightForWidth())
        self.atc_extend_button.setSizePolicy(sizePolicy1)
        self.atc_extend_button.setMinimumSize(QSize(120, 45))
        self.atc_extend_button.setMaximumSize(QSize(16777215, 45))
        self.atc_extend_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.atc_extend_button.setStyleSheet(u"SubCallButton {\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/images/right_arrow.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.atc_extend_button.setIcon(icon3)
        self.atc_extend_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_116.addWidget(self.atc_extend_button)


        self.verticalLayout_66.addLayout(self.horizontalLayout_116)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setSpacing(15)
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalLayout_117.setContentsMargins(2, 2, 2, 2)
        self.clamp_tool_button = SubCallButton(self.widget_64)
        self.clamp_tool_button.setObjectName(u"clamp_tool_button")
        sizePolicy1.setHeightForWidth(self.clamp_tool_button.sizePolicy().hasHeightForWidth())
        self.clamp_tool_button.setSizePolicy(sizePolicy1)
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

        self.release_tool_button = SubCallButton(self.widget_64)
        self.release_tool_button.setObjectName(u"release_tool_button")
        self.release_tool_button.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.release_tool_button.sizePolicy().hasHeightForWidth())
        self.release_tool_button.setSizePolicy(sizePolicy1)
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
        self.spindle_orientation = SubCallButton(self.widget_64)
        self.spindle_orientation.setObjectName(u"spindle_orientation")
        sizePolicy1.setHeightForWidth(self.spindle_orientation.sizePolicy().hasHeightForWidth())
        self.spindle_orientation.setSizePolicy(sizePolicy1)
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

        self.unlock_spindle = MDIButton(self.widget_64)
        self.unlock_spindle.setObjectName(u"unlock_spindle")
        sizePolicy1.setHeightForWidth(self.unlock_spindle.sizePolicy().hasHeightForWidth())
        self.unlock_spindle.setSizePolicy(sizePolicy1)
        self.unlock_spindle.setMinimumSize(QSize(120, 45))
        self.unlock_spindle.setMaximumSize(QSize(16777215, 45))
        self.unlock_spindle.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.unlock_spindle.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
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
        self.move_head_above_carousel_button = SubCallButton(self.widget_64)
        self.move_head_above_carousel_button.setObjectName(u"move_head_above_carousel_button")
        sizePolicy1.setHeightForWidth(self.move_head_above_carousel_button.sizePolicy().hasHeightForWidth())
        self.move_head_above_carousel_button.setSizePolicy(sizePolicy1)
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


        self.verticalLayout_66.addLayout(self.horizontalLayout_174)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setSpacing(15)
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.horizontalLayout_118.setContentsMargins(2, 2, 2, 2)
        self.move_tool_to_carousel_height_button = SubCallButton(self.widget_64)
        self.move_tool_to_carousel_height_button.setObjectName(u"move_tool_to_carousel_height_button")
        sizePolicy1.setHeightForWidth(self.move_tool_to_carousel_height_button.sizePolicy().hasHeightForWidth())
        self.move_tool_to_carousel_height_button.setSizePolicy(sizePolicy1)
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

        self.horizontalLayout_118.addWidget(self.move_tool_to_carousel_height_button)


        self.verticalLayout_66.addLayout(self.horizontalLayout_118)

        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setSpacing(15)
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalLayout_119.setContentsMargins(2, 2, 2, 2)
        self.reference_carousel = MDIButton(self.widget_64)
        self.reference_carousel.setObjectName(u"reference_carousel")
        sizePolicy1.setHeightForWidth(self.reference_carousel.sizePolicy().hasHeightForWidth())
        self.reference_carousel.setSizePolicy(sizePolicy1)
        self.reference_carousel.setMinimumSize(QSize(125, 45))
        self.reference_carousel.setMaximumSize(QSize(16777215, 45))
        self.reference_carousel.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.reference_carousel.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.reference_carousel.setIconSize(QSize(20, 20))

        self.horizontalLayout_119.addWidget(self.reference_carousel)


        self.verticalLayout_66.addLayout(self.horizontalLayout_119)


        self.verticalLayout.addWidget(self.widget_64)


        self.retranslateUi(USER_ATC_BUTTONS)

        QMetaObject.connectSlotsByName(USER_ATC_BUTTONS)
    # setupUi

    def retranslateUi(self, USER_ATC_BUTTONS):
        USER_ATC_BUTTONS.setWindowTitle(QCoreApplication.translate("USER_ATC_BUTTONS", u"User Atc Buttons", None))
#if QT_CONFIG(tooltip)
        self.atc_rev_button.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M11P1 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.atc_rev_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u" ATC REV", None))
        self.atc_rev_button.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M12P1", None))
#if QT_CONFIG(tooltip)
        self.atc_fwd_button.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M12 P1 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.atc_fwd_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u" ATC FWD ", None))
        self.atc_fwd_button.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M11P1", None))
        self.atc_retract_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"  ATC RETRACT", None))
        self.atc_retract_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"retractatc.ngc", None))
        self.atc_extend_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"ATC EXTEND  ", None))
        self.atc_extend_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"extendatc.ngc", None))
        self.clamp_tool_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"CLAMP TOOL", None))
        self.clamp_tool_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"clamptool.ngc", None))
        self.release_tool_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"RELEASE TOOL", None))
        self.release_tool_button.setProperty(u"rules", QCoreApplication.translate("USER_ATC_BUTTONS", u"[{\"name\": \"New Rule\", \"property\": \"Enable\", \"expression\": \"not ch[0]\", \"channels\": [{\"url\": \"status:spindle.0.enabled\", \"trigger\": true}]}]", None))
        self.release_tool_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"unclamptool.ngc", None))
        self.spindle_orientation.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"ORIENT SPINDLE", None))
        self.spindle_orientation.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"orientspindle.ngc", None))
#if QT_CONFIG(tooltip)
        self.unlock_spindle.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M112 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.unlock_spindle.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"UNLOCK SPINDLE", None))
        self.unlock_spindle.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M5", None))
        self.move_head_above_carousel_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"MOVE HEAD ABOVE CAROUSEL", None))
        self.move_head_above_carousel_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"move_head_above_carousel.ngc", None))
        self.move_tool_to_carousel_height_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"MOVE TOOL TO CAROUSEL HEIGHT", None))
        self.move_tool_to_carousel_height_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"move_tool_to_carousel_height.ngc", None))
#if QT_CONFIG(tooltip)
        self.reference_carousel.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.reference_carousel.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"REF CAROUSEL", None))
        self.reference_carousel.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M13", None))
    # retranslateUi

