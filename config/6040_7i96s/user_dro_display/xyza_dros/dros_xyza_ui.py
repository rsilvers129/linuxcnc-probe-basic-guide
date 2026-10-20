# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dros_xyza.ui'
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

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.input_widgets.dro_line_edit import DROLineEdit
import probe_basic_rc

class Ui_dros_xyza(object):
    def setupUi(self, dros_xyza):
        if not dros_xyza.objectName():
            dros_xyza.setObjectName(u"dros_xyza")
        dros_xyza.resize(469, 272)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dros_xyza.sizePolicy().hasHeightForWidth())
        dros_xyza.setSizePolicy(sizePolicy)
        dros_xyza.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout = QVBoxLayout(dros_xyza)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgets_xyza = QWidget(dros_xyza)
        self.widgets_xyza.setObjectName(u"widgets_xyza")
        self.verticalLayout_56 = QVBoxLayout(self.widgets_xyza)
        self.verticalLayout_56.setSpacing(4)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setSpacing(8)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(self.widgets_xyza)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u".QFrame{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179,172);\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    background-color: rgb(90, 90, 90);\n"
"    padding: -5px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_144 = QHBoxLayout(self.frame)
        self.horizontalLayout_144.setSpacing(8)
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalLayout_144.setContentsMargins(15, -1, 20, -1)
        self.axis_column_header = StatusLabel(self.frame)
        self.axis_column_header.setObjectName(u"axis_column_header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.axis_column_header.sizePolicy().hasHeightForWidth())
        self.axis_column_header.setSizePolicy(sizePolicy2)
        self.axis_column_header.setMinimumSize(QSize(60, 17))
        self.axis_column_header.setMaximumSize(QSize(60, 17))
        self.axis_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"    padding-left: 1px;\n"
"    padding-right: 20px;\n"
"}")
        self.axis_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_144.addWidget(self.axis_column_header)

        self.work_column_header = StatusLabel(self.frame)
        self.work_column_header.setObjectName(u"work_column_header")
        sizePolicy2.setHeightForWidth(self.work_column_header.sizePolicy().hasHeightForWidth())
        self.work_column_header.setSizePolicy(sizePolicy2)
        self.work_column_header.setMinimumSize(QSize(100, 17))
        self.work_column_header.setMaximumSize(QSize(100, 17))
        self.work_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"    padding-left: 6px;\n"
"}")
        self.work_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_144.addWidget(self.work_column_header)

        self.machine_column_header = QLabel(self.frame)
        self.machine_column_header.setObjectName(u"machine_column_header")
        self.machine_column_header.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.machine_column_header.sizePolicy().hasHeightForWidth())
        self.machine_column_header.setSizePolicy(sizePolicy2)
        self.machine_column_header.setMinimumSize(QSize(100, 17))
        self.machine_column_header.setMaximumSize(QSize(100, 17))
        self.machine_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_144.addWidget(self.machine_column_header)

        self.dtg_column_header = QLabel(self.frame)
        self.dtg_column_header.setObjectName(u"dtg_column_header")
        sizePolicy2.setHeightForWidth(self.dtg_column_header.sizePolicy().hasHeightForWidth())
        self.dtg_column_header.setSizePolicy(sizePolicy2)
        self.dtg_column_header.setMinimumSize(QSize(100, 17))
        self.dtg_column_header.setMaximumSize(QSize(100, 17))
        self.dtg_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.dtg_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_144.addWidget(self.dtg_column_header)

        self.ref_column_header = StatusLabel(self.frame)
        self.ref_column_header.setObjectName(u"ref_column_header")
        sizePolicy2.setHeightForWidth(self.ref_column_header.sizePolicy().hasHeightForWidth())
        self.ref_column_header.setSizePolicy(sizePolicy2)
        self.ref_column_header.setMinimumSize(QSize(40, 17))
        self.ref_column_header.setMaximumSize(QSize(40, 17))
        self.ref_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"    padding-left: 6px;\n"
"}")
        self.ref_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_144.addWidget(self.ref_column_header)


        self.horizontalLayout_77.addWidget(self.frame)


        self.verticalLayout_56.addLayout(self.horizontalLayout_77)

        self.x_axis_dro_layout_3 = QHBoxLayout()
        self.x_axis_dro_layout_3.setSpacing(7)
        self.x_axis_dro_layout_3.setObjectName(u"x_axis_dro_layout_3")
        self.x_axis_dro_layout_3.setContentsMargins(1, 1, 1, 1)
        self.zero_x_button = MDIButton(self.widgets_xyza)
        self.zero_x_button.setObjectName(u"zero_x_button")
        self.zero_x_button.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.zero_x_button.sizePolicy().hasHeightForWidth())
        self.zero_x_button.setSizePolicy(sizePolicy3)
        self.zero_x_button.setMinimumSize(QSize(60, 40))
        self.zero_x_button.setMaximumSize(QSize(60, 40))
        self.zero_x_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_x_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.zero_x_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/zero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zero_x_button.setIcon(icon)
        self.zero_x_button.setIconSize(QSize(20, 20))

        self.x_axis_dro_layout_3.addWidget(self.zero_x_button)

        self.drowidget_x = DROLineEdit(self.widgets_xyza)
        self.drowidget_x.setObjectName(u"drowidget_x")
        self.drowidget_x.setMinimumSize(QSize(100, 35))
        self.drowidget_x.setMaximumSize(QSize(100, 35))
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.drowidget_x.setFont(font)
        self.drowidget_x.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.drowidget_x.setCursorPosition(0)
        self.drowidget_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drowidget_x.setProperty(u"referenceType", 1)
        self.drowidget_x.setProperty(u"axisNumber", 0)
        self.drowidget_x.setProperty(u"latheMode", 0)

        self.x_axis_dro_layout_3.addWidget(self.drowidget_x)

        self.drolabel_machine_x = DROLabel(self.widgets_xyza)
        self.drolabel_machine_x.setObjectName(u"drolabel_machine_x")
        sizePolicy2.setHeightForWidth(self.drolabel_machine_x.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_x.setSizePolicy(sizePolicy2)
        self.drolabel_machine_x.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_x.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_x.setProperty(u"referenceType", 0)
        self.drolabel_machine_x.setProperty(u"axisNumber", 0)
        self.drolabel_machine_x.setProperty(u"latheMode", 0)

        self.x_axis_dro_layout_3.addWidget(self.drolabel_machine_x)

        self.drolabel_dtg_x = DROLabel(self.widgets_xyza)
        self.drolabel_dtg_x.setObjectName(u"drolabel_dtg_x")
        sizePolicy2.setHeightForWidth(self.drolabel_dtg_x.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_x.setSizePolicy(sizePolicy2)
        self.drolabel_dtg_x.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_x.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_x.setProperty(u"referenceType", 2)
        self.drolabel_dtg_x.setProperty(u"axisNumber", 0)
        self.drolabel_dtg_x.setProperty(u"latheMode", 0)

        self.x_axis_dro_layout_3.addWidget(self.drolabel_dtg_x)

        self.ref_x_button = ActionButton(self.widgets_xyza)
        self.ref_x_button.setObjectName(u"ref_x_button")
        sizePolicy1.setHeightForWidth(self.ref_x_button.sizePolicy().hasHeightForWidth())
        self.ref_x_button.setSizePolicy(sizePolicy1)
        self.ref_x_button.setMinimumSize(QSize(62, 40))
        self.ref_x_button.setMaximumSize(QSize(62, 40))
        self.ref_x_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_x_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.x_axis_dro_layout_3.addWidget(self.ref_x_button)


        self.verticalLayout_56.addLayout(self.x_axis_dro_layout_3)

        self.y_axis_dro_layout_3 = QHBoxLayout()
        self.y_axis_dro_layout_3.setSpacing(7)
        self.y_axis_dro_layout_3.setObjectName(u"y_axis_dro_layout_3")
        self.y_axis_dro_layout_3.setContentsMargins(1, 1, 1, 1)
        self.zero_y_button = MDIButton(self.widgets_xyza)
        self.zero_y_button.setObjectName(u"zero_y_button")
        self.zero_y_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.zero_y_button.sizePolicy().hasHeightForWidth())
        self.zero_y_button.setSizePolicy(sizePolicy3)
        self.zero_y_button.setMinimumSize(QSize(60, 40))
        self.zero_y_button.setMaximumSize(QSize(60, 40))
        self.zero_y_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_y_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_y_button.setIcon(icon)
        self.zero_y_button.setIconSize(QSize(20, 20))

        self.y_axis_dro_layout_3.addWidget(self.zero_y_button)

        self.drowidget_y = DROLineEdit(self.widgets_xyza)
        self.drowidget_y.setObjectName(u"drowidget_y")
        self.drowidget_y.setMinimumSize(QSize(100, 35))
        self.drowidget_y.setMaximumSize(QSize(100, 35))
        self.drowidget_y.setFont(font)
        self.drowidget_y.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.drowidget_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drowidget_y.setProperty(u"axisNumber", 1)

        self.y_axis_dro_layout_3.addWidget(self.drowidget_y)

        self.drolabel_machine_y = DROLabel(self.widgets_xyza)
        self.drolabel_machine_y.setObjectName(u"drolabel_machine_y")
        sizePolicy2.setHeightForWidth(self.drolabel_machine_y.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_y.setSizePolicy(sizePolicy2)
        self.drolabel_machine_y.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_y.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_y.setProperty(u"referenceType", 0)
        self.drolabel_machine_y.setProperty(u"axisNumber", 1)
        self.drolabel_machine_y.setProperty(u"latheMode", 0)

        self.y_axis_dro_layout_3.addWidget(self.drolabel_machine_y)

        self.drolabel_dtg_y = DROLabel(self.widgets_xyza)
        self.drolabel_dtg_y.setObjectName(u"drolabel_dtg_y")
        sizePolicy2.setHeightForWidth(self.drolabel_dtg_y.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_y.setSizePolicy(sizePolicy2)
        self.drolabel_dtg_y.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_y.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_y.setProperty(u"referenceType", 2)
        self.drolabel_dtg_y.setProperty(u"axisNumber", 1)
        self.drolabel_dtg_y.setProperty(u"latheMode", 0)

        self.y_axis_dro_layout_3.addWidget(self.drolabel_dtg_y)

        self.ref_y_button = ActionButton(self.widgets_xyza)
        self.ref_y_button.setObjectName(u"ref_y_button")
        sizePolicy1.setHeightForWidth(self.ref_y_button.sizePolicy().hasHeightForWidth())
        self.ref_y_button.setSizePolicy(sizePolicy1)
        self.ref_y_button.setMinimumSize(QSize(62, 40))
        self.ref_y_button.setMaximumSize(QSize(62, 40))
        self.ref_y_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_y_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.y_axis_dro_layout_3.addWidget(self.ref_y_button)


        self.verticalLayout_56.addLayout(self.y_axis_dro_layout_3)

        self.z_axis_dro_layout_3 = QHBoxLayout()
        self.z_axis_dro_layout_3.setSpacing(7)
        self.z_axis_dro_layout_3.setObjectName(u"z_axis_dro_layout_3")
        self.z_axis_dro_layout_3.setContentsMargins(1, 1, 1, 1)
        self.zero_z_button = MDIButton(self.widgets_xyza)
        self.zero_z_button.setObjectName(u"zero_z_button")
        self.zero_z_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.zero_z_button.sizePolicy().hasHeightForWidth())
        self.zero_z_button.setSizePolicy(sizePolicy3)
        self.zero_z_button.setMinimumSize(QSize(60, 40))
        self.zero_z_button.setMaximumSize(QSize(60, 40))
        self.zero_z_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_z_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_z_button.setIcon(icon)
        self.zero_z_button.setIconSize(QSize(20, 20))

        self.z_axis_dro_layout_3.addWidget(self.zero_z_button)

        self.drowidget_z = DROLineEdit(self.widgets_xyza)
        self.drowidget_z.setObjectName(u"drowidget_z")
        self.drowidget_z.setMinimumSize(QSize(100, 35))
        self.drowidget_z.setMaximumSize(QSize(100, 35))
        self.drowidget_z.setFont(font)
        self.drowidget_z.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.drowidget_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drowidget_z.setProperty(u"axisNumber", 2)

        self.z_axis_dro_layout_3.addWidget(self.drowidget_z)

        self.drolabel_machine_z = DROLabel(self.widgets_xyza)
        self.drolabel_machine_z.setObjectName(u"drolabel_machine_z")
        sizePolicy2.setHeightForWidth(self.drolabel_machine_z.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_z.setSizePolicy(sizePolicy2)
        self.drolabel_machine_z.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_z.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_z.setProperty(u"referenceType", 0)
        self.drolabel_machine_z.setProperty(u"axisNumber", 2)
        self.drolabel_machine_z.setProperty(u"latheMode", 0)

        self.z_axis_dro_layout_3.addWidget(self.drolabel_machine_z)

        self.drolabel_dtg_z = DROLabel(self.widgets_xyza)
        self.drolabel_dtg_z.setObjectName(u"drolabel_dtg_z")
        sizePolicy2.setHeightForWidth(self.drolabel_dtg_z.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_z.setSizePolicy(sizePolicy2)
        self.drolabel_dtg_z.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_z.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_z.setProperty(u"referenceType", 2)
        self.drolabel_dtg_z.setProperty(u"axisNumber", 2)
        self.drolabel_dtg_z.setProperty(u"latheMode", 0)

        self.z_axis_dro_layout_3.addWidget(self.drolabel_dtg_z)

        self.ref_z_button = ActionButton(self.widgets_xyza)
        self.ref_z_button.setObjectName(u"ref_z_button")
        sizePolicy1.setHeightForWidth(self.ref_z_button.sizePolicy().hasHeightForWidth())
        self.ref_z_button.setSizePolicy(sizePolicy1)
        self.ref_z_button.setMinimumSize(QSize(62, 40))
        self.ref_z_button.setMaximumSize(QSize(62, 40))
        self.ref_z_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_z_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.z_axis_dro_layout_3.addWidget(self.ref_z_button)


        self.verticalLayout_56.addLayout(self.z_axis_dro_layout_3)

        self.a_axis_dro_layout_2 = QHBoxLayout()
        self.a_axis_dro_layout_2.setSpacing(7)
        self.a_axis_dro_layout_2.setObjectName(u"a_axis_dro_layout_2")
        self.a_axis_dro_layout_2.setContentsMargins(1, 1, 1, 1)
        self.zero_a_button = MDIButton(self.widgets_xyza)
        self.zero_a_button.setObjectName(u"zero_a_button")
        self.zero_a_button.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.zero_a_button.sizePolicy().hasHeightForWidth())
        self.zero_a_button.setSizePolicy(sizePolicy3)
        self.zero_a_button.setMinimumSize(QSize(60, 40))
        self.zero_a_button.setMaximumSize(QSize(60, 40))
        self.zero_a_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_a_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_a_button.setIcon(icon)
        self.zero_a_button.setIconSize(QSize(20, 20))

        self.a_axis_dro_layout_2.addWidget(self.zero_a_button)

        self.drowidget_a = DROLineEdit(self.widgets_xyza)
        self.drowidget_a.setObjectName(u"drowidget_a")
        self.drowidget_a.setMinimumSize(QSize(100, 35))
        self.drowidget_a.setMaximumSize(QSize(100, 35))
        self.drowidget_a.setFont(font)
        self.drowidget_a.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.drowidget_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drowidget_a.setProperty(u"axisNumber", 3)

        self.a_axis_dro_layout_2.addWidget(self.drowidget_a)

        self.drolabel_machine_a = DROLabel(self.widgets_xyza)
        self.drolabel_machine_a.setObjectName(u"drolabel_machine_a")
        sizePolicy2.setHeightForWidth(self.drolabel_machine_a.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_a.setSizePolicy(sizePolicy2)
        self.drolabel_machine_a.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_a.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_a.setProperty(u"referenceType", 0)
        self.drolabel_machine_a.setProperty(u"axisNumber", 3)
        self.drolabel_machine_a.setProperty(u"latheMode", 0)

        self.a_axis_dro_layout_2.addWidget(self.drolabel_machine_a)

        self.drolabel_dtg_a = DROLabel(self.widgets_xyza)
        self.drolabel_dtg_a.setObjectName(u"drolabel_dtg_a")
        sizePolicy2.setHeightForWidth(self.drolabel_dtg_a.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_a.setSizePolicy(sizePolicy2)
        self.drolabel_dtg_a.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_a.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_a.setProperty(u"referenceType", 2)
        self.drolabel_dtg_a.setProperty(u"axisNumber", 3)
        self.drolabel_dtg_a.setProperty(u"latheMode", 0)

        self.a_axis_dro_layout_2.addWidget(self.drolabel_dtg_a)

        self.ref_a_button = ActionButton(self.widgets_xyza)
        self.ref_a_button.setObjectName(u"ref_a_button")
        sizePolicy1.setHeightForWidth(self.ref_a_button.sizePolicy().hasHeightForWidth())
        self.ref_a_button.setSizePolicy(sizePolicy1)
        self.ref_a_button.setMinimumSize(QSize(62, 40))
        self.ref_a_button.setMaximumSize(QSize(62, 40))
        self.ref_a_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_a_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.a_axis_dro_layout_2.addWidget(self.ref_a_button)


        self.verticalLayout_56.addLayout(self.a_axis_dro_layout_2)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setSpacing(20)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(3, 1, 3, 1)
        self.zero_all_button = MDIButton(self.widgets_xyza)
        self.zero_all_button.setObjectName(u"zero_all_button")
        self.zero_all_button.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.zero_all_button.sizePolicy().hasHeightForWidth())
        self.zero_all_button.setSizePolicy(sizePolicy4)
        self.zero_all_button.setMinimumSize(QSize(60, 40))
        self.zero_all_button.setMaximumSize(QSize(16777215, 40))
        self.zero_all_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_all_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.zero_all_button.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_all_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_104.addWidget(self.zero_all_button)

        self.ref_all_button = ActionButton(self.widgets_xyza)
        self.ref_all_button.setObjectName(u"ref_all_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(1)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ref_all_button.sizePolicy().hasHeightForWidth())
        self.ref_all_button.setSizePolicy(sizePolicy5)
        self.ref_all_button.setMinimumSize(QSize(62, 40))
        self.ref_all_button.setMaximumSize(QSize(16777215, 40))
        self.ref_all_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_all_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.horizontalLayout_104.addWidget(self.ref_all_button)


        self.verticalLayout_56.addLayout(self.horizontalLayout_104)


        self.verticalLayout.addWidget(self.widgets_xyza)


        self.retranslateUi(dros_xyza)

        QMetaObject.connectSlotsByName(dros_xyza)
    # setupUi

    def retranslateUi(self, dros_xyza):
        dros_xyza.setWindowTitle(QCoreApplication.translate("dros_xyza", u"dros_xyza", None))
        self.axis_column_header.setText(QCoreApplication.translate("dros_xyza", u"AXIS", None))
        self.axis_column_header.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[]", None))
        self.work_column_header.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[{\"channels\": [{\"url\": \"status:g5x_index?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + ' WORK'\\n\", \"name\": \"WCS Header\"}]", None))
        self.machine_column_header.setText(QCoreApplication.translate("dros_xyza", u"MACHINE", None))
        self.dtg_column_header.setText(QCoreApplication.translate("dros_xyza", u"DTG", None))
        self.ref_column_header.setText(QCoreApplication.translate("dros_xyza", u"REF", None))
        self.ref_column_header.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[]", None))
        self.zero_x_button.setText(QCoreApplication.translate("dros_xyza", u"X", None))
        self.zero_x_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_x_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyza", u"G10 L20 P{ch[0]} X0.0", None))
        self.drowidget_x.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drowidget_x.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drowidget_x.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drowidget_x.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_machine_x.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_machine_x.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_machine_x.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_machine_x.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_dtg_x.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_dtg_x.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_dtg_x.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_dtg_x.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.ref_x_button.setText(QCoreApplication.translate("dros_xyza", u"REF X", None))
        self.ref_x_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}]}]", None))
        self.ref_x_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyza", u"machine.home.axis:x", None))
        self.zero_y_button.setText(QCoreApplication.translate("dros_xyza", u"Y", None))
        self.zero_y_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_y_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyza", u"G10 L20 P{ch[0]} Y0.0", None))
        self.drowidget_y.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_machine_y.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_machine_y.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_machine_y.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_machine_y.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_dtg_y.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_dtg_y.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_dtg_y.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_dtg_y.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.ref_y_button.setText(QCoreApplication.translate("dros_xyza", u"REF Y", None))
        self.ref_y_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}]}]", None))
        self.ref_y_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyza", u"machine.home.axis:y", None))
        self.zero_z_button.setText(QCoreApplication.translate("dros_xyza", u"Z", None))
        self.zero_z_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_z_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyza", u"G10 L20 P{ch[0]} Z0.0", None))
        self.drowidget_z.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_machine_z.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_machine_z.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_machine_z.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_machine_z.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_dtg_z.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_dtg_z.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_dtg_z.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_dtg_z.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.ref_z_button.setText(QCoreApplication.translate("dros_xyza", u"REF Z", None))
        self.ref_z_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}]}]", None))
        self.ref_z_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyza", u"machine.home.axis:z", None))
        self.zero_a_button.setText(QCoreApplication.translate("dros_xyza", u"A", None))
        self.zero_a_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_a_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyza", u"G10 L20 P{ch[0]} A0.0", None))
        self.drowidget_a.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_machine_a.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_machine_a.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_machine_a.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_machine_a.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.drolabel_dtg_a.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyza", u"%9.4f", None))
        self.drolabel_dtg_a.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyza", u"%10.3f", None))
        self.drolabel_dtg_a.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyza", u"%10.2f", None))
        self.drolabel_dtg_a.setProperty(u"styleSet", QCoreApplication.translate("dros_xyza", u"dataField17", None))
        self.ref_a_button.setText(QCoreApplication.translate("dros_xyza", u"REF A", None))
        self.ref_a_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}]}]", None))
        self.ref_a_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyza", u"machine.home.axis:a", None))
        self.zero_all_button.setText(QCoreApplication.translate("dros_xyza", u"ZERO ALL", None))
        self.zero_all_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[\n"
"    {\n"
"        \"channels\": [\n"
"            {\n"
"                \"url\": \"status:g5x_index\",\n"
"                \"trigger\": true,\n"
"                \"type\": \"int\"\n"
"            }\n"
"        ],\n"
"        \"expression\": \"\",\n"
"        \"name\": \"G5x Index\",\n"
"        \"property\": \"None\"\n"
"    }\n"
"]", None))
        self.zero_all_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyza", u"G10 L20 P{ch[0]} X0.0 Y0.0 Z0.0", None))
        self.ref_all_button.setText(QCoreApplication.translate("dros_xyza", u"REF ALL", None))
        self.ref_all_button.setProperty(u"rules", QCoreApplication.translate("dros_xyza", u"[{\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'HOMED' if ch[0] else 'REF ALL'\", \"name\": \"reference_all\"}, {\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}]}]", None))
        self.ref_all_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyza", u"machine.home.all", None))
    # retranslateUi

