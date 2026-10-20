# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dros_xyzac.ui'
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
    QLayout, QSizePolicy, QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.input_widgets.dro_line_edit import DROLineEdit
import probe_basic_rc

class Ui_dros_xyzac(object):
    def setupUi(self, dros_xyzac):
        if not dros_xyzac.objectName():
            dros_xyzac.setObjectName(u"dros_xyzac")
        dros_xyzac.resize(458, 272)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dros_xyzac.sizePolicy().hasHeightForWidth())
        dros_xyzac.setSizePolicy(sizePolicy)
        dros_xyzac.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.y_axis_dro_layout_2 = QVBoxLayout(dros_xyzac)
        self.y_axis_dro_layout_2.setSpacing(0)
        self.y_axis_dro_layout_2.setObjectName(u"y_axis_dro_layout_2")
        self.y_axis_dro_layout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_xyzac = QWidget(dros_xyzac)
        self.widget_xyzac.setObjectName(u"widget_xyzac")
        self._2 = QVBoxLayout(self.widget_xyzac)
        self._2.setSpacing(4)
        self._2.setObjectName(u"_2")
        self._2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self._2.setContentsMargins(0, 0, 0, 0)
        self.header_layout = QHBoxLayout()
        self.header_layout.setSpacing(7)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setContentsMargins(1, 1, 1, 1)
        self.zero_all_button = MDIButton(self.widget_xyzac)
        self.zero_all_button.setObjectName(u"zero_all_button")
        self.zero_all_button.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.zero_all_button.sizePolicy().hasHeightForWidth())
        self.zero_all_button.setSizePolicy(sizePolicy1)
        self.zero_all_button.setMinimumSize(QSize(60, 40))
        self.zero_all_button.setMaximumSize(QSize(60, 40))
        self.zero_all_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_all_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.zero_all_button.setStyleSheet(u"MDIButton {\n"
"   	font: 14pt \"Probe Basic Bebas Mono\";\n"
"}")
        icon = QIcon()
        icon.addFile(u":/images/zero.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.zero_all_button.setIcon(icon)
        self.zero_all_button.setIconSize(QSize(20, 20))

        self.header_layout.addWidget(self.zero_all_button)

        self.frame = QFrame(self.widget_xyzac)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
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
        self.horizontalLayout_131 = QHBoxLayout(self.frame)
        self.horizontalLayout_131.setSpacing(8)
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalLayout_131.setContentsMargins(5, -1, 7, -1)
        self.work_column_header = StatusLabel(self.frame)
        self.work_column_header.setObjectName(u"work_column_header")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.work_column_header.sizePolicy().hasHeightForWidth())
        self.work_column_header.setSizePolicy(sizePolicy3)
        self.work_column_header.setMinimumSize(QSize(100, 17))
        self.work_column_header.setMaximumSize(QSize(100, 17))
        self.work_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"    padding-left: 6px;\n"
"}")
        self.work_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_131.addWidget(self.work_column_header)

        self.machine_column_header = QLabel(self.frame)
        self.machine_column_header.setObjectName(u"machine_column_header")
        self.machine_column_header.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.machine_column_header.sizePolicy().hasHeightForWidth())
        self.machine_column_header.setSizePolicy(sizePolicy3)
        self.machine_column_header.setMinimumSize(QSize(100, 17))
        self.machine_column_header.setMaximumSize(QSize(100, 17))
        self.machine_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.machine_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_131.addWidget(self.machine_column_header)

        self.dtg_column_header = QLabel(self.frame)
        self.dtg_column_header.setObjectName(u"dtg_column_header")
        sizePolicy3.setHeightForWidth(self.dtg_column_header.sizePolicy().hasHeightForWidth())
        self.dtg_column_header.setSizePolicy(sizePolicy3)
        self.dtg_column_header.setMinimumSize(QSize(100, 17))
        self.dtg_column_header.setMaximumSize(QSize(100, 17))
        self.dtg_column_header.setStyleSheet(u"QLabel{\n"
"    color: rgb(238, 238, 236);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.dtg_column_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_131.addWidget(self.dtg_column_header)


        self.header_layout.addWidget(self.frame)

        self.ref_all_button = ActionButton(self.widget_xyzac)
        self.ref_all_button.setObjectName(u"ref_all_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ref_all_button.sizePolicy().hasHeightForWidth())
        self.ref_all_button.setSizePolicy(sizePolicy4)
        self.ref_all_button.setMinimumSize(QSize(62, 40))
        self.ref_all_button.setMaximumSize(QSize(62, 40))
        self.ref_all_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_all_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.header_layout.addWidget(self.ref_all_button)


        self._2.addLayout(self.header_layout)

        self.x_axis_dro_layout = QHBoxLayout()
        self.x_axis_dro_layout.setSpacing(7)
        self.x_axis_dro_layout.setObjectName(u"x_axis_dro_layout")
        self.x_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.zero_x_button = MDIButton(self.widget_xyzac)
        self.zero_x_button.setObjectName(u"zero_x_button")
        self.zero_x_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_x_button.sizePolicy().hasHeightForWidth())
        self.zero_x_button.setSizePolicy(sizePolicy1)
        self.zero_x_button.setMinimumSize(QSize(60, 40))
        self.zero_x_button.setMaximumSize(QSize(60, 40))
        self.zero_x_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_x_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.zero_x_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_x_button.setIcon(icon)
        self.zero_x_button.setIconSize(QSize(20, 20))

        self.x_axis_dro_layout.addWidget(self.zero_x_button)

        self.dro_entry_main_x = DROLineEdit(self.widget_xyzac)
        self.dro_entry_main_x.setObjectName(u"dro_entry_main_x")
        self.dro_entry_main_x.setMinimumSize(QSize(100, 35))
        self.dro_entry_main_x.setMaximumSize(QSize(100, 35))
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.dro_entry_main_x.setFont(font)
        self.dro_entry_main_x.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_main_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_main_x.setProperty(u"referenceType", 1)
        self.dro_entry_main_x.setProperty(u"axisNumber", 0)
        self.dro_entry_main_x.setProperty(u"latheMode", 0)

        self.x_axis_dro_layout.addWidget(self.dro_entry_main_x)

        self.drolabel_machine_x = DROLabel(self.widget_xyzac)
        self.drolabel_machine_x.setObjectName(u"drolabel_machine_x")
        sizePolicy3.setHeightForWidth(self.drolabel_machine_x.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_x.setSizePolicy(sizePolicy3)
        self.drolabel_machine_x.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_x.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_x.setProperty(u"referenceType", 0)
        self.drolabel_machine_x.setProperty(u"axisNumber", 0)
        self.drolabel_machine_x.setProperty(u"latheMode", 0)

        self.x_axis_dro_layout.addWidget(self.drolabel_machine_x)

        self.drolabel_dtg_x = DROLabel(self.widget_xyzac)
        self.drolabel_dtg_x.setObjectName(u"drolabel_dtg_x")
        sizePolicy3.setHeightForWidth(self.drolabel_dtg_x.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_x.setSizePolicy(sizePolicy3)
        self.drolabel_dtg_x.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_x.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_x.setProperty(u"referenceType", 2)
        self.drolabel_dtg_x.setProperty(u"axisNumber", 0)
        self.drolabel_dtg_x.setProperty(u"latheMode", 0)

        self.x_axis_dro_layout.addWidget(self.drolabel_dtg_x)

        self.ref_x_button_3 = ActionButton(self.widget_xyzac)
        self.ref_x_button_3.setObjectName(u"ref_x_button_3")
        sizePolicy2.setHeightForWidth(self.ref_x_button_3.sizePolicy().hasHeightForWidth())
        self.ref_x_button_3.setSizePolicy(sizePolicy2)
        self.ref_x_button_3.setMinimumSize(QSize(62, 40))
        self.ref_x_button_3.setMaximumSize(QSize(62, 40))
        self.ref_x_button_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_x_button_3.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.x_axis_dro_layout.addWidget(self.ref_x_button_3)


        self._2.addLayout(self.x_axis_dro_layout)

        self.y_axis_dro_layout = QHBoxLayout()
        self.y_axis_dro_layout.setSpacing(7)
        self.y_axis_dro_layout.setObjectName(u"y_axis_dro_layout")
        self.y_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.zero_y_button = MDIButton(self.widget_xyzac)
        self.zero_y_button.setObjectName(u"zero_y_button")
        self.zero_y_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_y_button.sizePolicy().hasHeightForWidth())
        self.zero_y_button.setSizePolicy(sizePolicy1)
        self.zero_y_button.setMinimumSize(QSize(60, 40))
        self.zero_y_button.setMaximumSize(QSize(60, 40))
        self.zero_y_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_y_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_y_button.setIcon(icon)
        self.zero_y_button.setIconSize(QSize(20, 20))

        self.y_axis_dro_layout.addWidget(self.zero_y_button)

        self.dro_entry_main_y = DROLineEdit(self.widget_xyzac)
        self.dro_entry_main_y.setObjectName(u"dro_entry_main_y")
        self.dro_entry_main_y.setMinimumSize(QSize(100, 35))
        self.dro_entry_main_y.setMaximumSize(QSize(100, 35))
        self.dro_entry_main_y.setFont(font)
        self.dro_entry_main_y.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_main_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_main_y.setProperty(u"axisNumber", 1)

        self.y_axis_dro_layout.addWidget(self.dro_entry_main_y)

        self.drolabel_machine_y = DROLabel(self.widget_xyzac)
        self.drolabel_machine_y.setObjectName(u"drolabel_machine_y")
        sizePolicy3.setHeightForWidth(self.drolabel_machine_y.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_y.setSizePolicy(sizePolicy3)
        self.drolabel_machine_y.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_y.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_y.setProperty(u"referenceType", 0)
        self.drolabel_machine_y.setProperty(u"axisNumber", 1)
        self.drolabel_machine_y.setProperty(u"latheMode", 0)

        self.y_axis_dro_layout.addWidget(self.drolabel_machine_y)

        self.drolabel_dtg_y = DROLabel(self.widget_xyzac)
        self.drolabel_dtg_y.setObjectName(u"drolabel_dtg_y")
        sizePolicy3.setHeightForWidth(self.drolabel_dtg_y.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_y.setSizePolicy(sizePolicy3)
        self.drolabel_dtg_y.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_y.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_y.setProperty(u"referenceType", 2)
        self.drolabel_dtg_y.setProperty(u"axisNumber", 1)
        self.drolabel_dtg_y.setProperty(u"latheMode", 0)

        self.y_axis_dro_layout.addWidget(self.drolabel_dtg_y)

        self.ref_y_button = ActionButton(self.widget_xyzac)
        self.ref_y_button.setObjectName(u"ref_y_button")
        sizePolicy2.setHeightForWidth(self.ref_y_button.sizePolicy().hasHeightForWidth())
        self.ref_y_button.setSizePolicy(sizePolicy2)
        self.ref_y_button.setMinimumSize(QSize(62, 40))
        self.ref_y_button.setMaximumSize(QSize(62, 40))
        self.ref_y_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_y_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.y_axis_dro_layout.addWidget(self.ref_y_button)


        self._2.addLayout(self.y_axis_dro_layout)

        self.z_axis_dro_layout = QHBoxLayout()
        self.z_axis_dro_layout.setSpacing(7)
        self.z_axis_dro_layout.setObjectName(u"z_axis_dro_layout")
        self.z_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.zero_z_button = MDIButton(self.widget_xyzac)
        self.zero_z_button.setObjectName(u"zero_z_button")
        self.zero_z_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_z_button.sizePolicy().hasHeightForWidth())
        self.zero_z_button.setSizePolicy(sizePolicy1)
        self.zero_z_button.setMinimumSize(QSize(60, 40))
        self.zero_z_button.setMaximumSize(QSize(60, 40))
        self.zero_z_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_z_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_z_button.setIcon(icon)
        self.zero_z_button.setIconSize(QSize(20, 20))

        self.z_axis_dro_layout.addWidget(self.zero_z_button)

        self.dro_entry_main_z = DROLineEdit(self.widget_xyzac)
        self.dro_entry_main_z.setObjectName(u"dro_entry_main_z")
        self.dro_entry_main_z.setMinimumSize(QSize(100, 35))
        self.dro_entry_main_z.setMaximumSize(QSize(100, 35))
        self.dro_entry_main_z.setFont(font)
        self.dro_entry_main_z.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_main_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_main_z.setProperty(u"axisNumber", 2)

        self.z_axis_dro_layout.addWidget(self.dro_entry_main_z)

        self.drolabel_machine_z = DROLabel(self.widget_xyzac)
        self.drolabel_machine_z.setObjectName(u"drolabel_machine_z")
        sizePolicy3.setHeightForWidth(self.drolabel_machine_z.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_z.setSizePolicy(sizePolicy3)
        self.drolabel_machine_z.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_z.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_z.setProperty(u"referenceType", 0)
        self.drolabel_machine_z.setProperty(u"axisNumber", 2)
        self.drolabel_machine_z.setProperty(u"latheMode", 0)

        self.z_axis_dro_layout.addWidget(self.drolabel_machine_z)

        self.drolabel_dtg_z = DROLabel(self.widget_xyzac)
        self.drolabel_dtg_z.setObjectName(u"drolabel_dtg_z")
        sizePolicy3.setHeightForWidth(self.drolabel_dtg_z.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_z.setSizePolicy(sizePolicy3)
        self.drolabel_dtg_z.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_z.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_z.setProperty(u"referenceType", 2)
        self.drolabel_dtg_z.setProperty(u"axisNumber", 2)
        self.drolabel_dtg_z.setProperty(u"latheMode", 0)

        self.z_axis_dro_layout.addWidget(self.drolabel_dtg_z)

        self.ref_z_button = ActionButton(self.widget_xyzac)
        self.ref_z_button.setObjectName(u"ref_z_button")
        sizePolicy2.setHeightForWidth(self.ref_z_button.sizePolicy().hasHeightForWidth())
        self.ref_z_button.setSizePolicy(sizePolicy2)
        self.ref_z_button.setMinimumSize(QSize(62, 40))
        self.ref_z_button.setMaximumSize(QSize(62, 40))
        self.ref_z_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_z_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.z_axis_dro_layout.addWidget(self.ref_z_button)


        self._2.addLayout(self.z_axis_dro_layout)

        self.a_axis_dro_layout = QHBoxLayout()
        self.a_axis_dro_layout.setSpacing(7)
        self.a_axis_dro_layout.setObjectName(u"a_axis_dro_layout")
        self.a_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.zero_a_button = MDIButton(self.widget_xyzac)
        self.zero_a_button.setObjectName(u"zero_a_button")
        self.zero_a_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_a_button.sizePolicy().hasHeightForWidth())
        self.zero_a_button.setSizePolicy(sizePolicy1)
        self.zero_a_button.setMinimumSize(QSize(60, 40))
        self.zero_a_button.setMaximumSize(QSize(60, 40))
        self.zero_a_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_a_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_a_button.setIcon(icon)
        self.zero_a_button.setIconSize(QSize(20, 20))

        self.a_axis_dro_layout.addWidget(self.zero_a_button)

        self.dro_entry_main_a = DROLineEdit(self.widget_xyzac)
        self.dro_entry_main_a.setObjectName(u"dro_entry_main_a")
        self.dro_entry_main_a.setMinimumSize(QSize(100, 35))
        self.dro_entry_main_a.setMaximumSize(QSize(100, 35))
        self.dro_entry_main_a.setFont(font)
        self.dro_entry_main_a.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_main_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_main_a.setProperty(u"axisNumber", 3)

        self.a_axis_dro_layout.addWidget(self.dro_entry_main_a)

        self.drolabel_machine_a = DROLabel(self.widget_xyzac)
        self.drolabel_machine_a.setObjectName(u"drolabel_machine_a")
        sizePolicy3.setHeightForWidth(self.drolabel_machine_a.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_a.setSizePolicy(sizePolicy3)
        self.drolabel_machine_a.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_a.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_a.setProperty(u"referenceType", 0)
        self.drolabel_machine_a.setProperty(u"axisNumber", 3)
        self.drolabel_machine_a.setProperty(u"latheMode", 0)

        self.a_axis_dro_layout.addWidget(self.drolabel_machine_a)

        self.drolabel_dtg_a = DROLabel(self.widget_xyzac)
        self.drolabel_dtg_a.setObjectName(u"drolabel_dtg_a")
        sizePolicy3.setHeightForWidth(self.drolabel_dtg_a.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_a.setSizePolicy(sizePolicy3)
        self.drolabel_dtg_a.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_a.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_a.setProperty(u"referenceType", 2)
        self.drolabel_dtg_a.setProperty(u"axisNumber", 3)
        self.drolabel_dtg_a.setProperty(u"latheMode", 0)

        self.a_axis_dro_layout.addWidget(self.drolabel_dtg_a)

        self.ref_a_button = ActionButton(self.widget_xyzac)
        self.ref_a_button.setObjectName(u"ref_a_button")
        sizePolicy2.setHeightForWidth(self.ref_a_button.sizePolicy().hasHeightForWidth())
        self.ref_a_button.setSizePolicy(sizePolicy2)
        self.ref_a_button.setMinimumSize(QSize(62, 40))
        self.ref_a_button.setMaximumSize(QSize(62, 40))
        self.ref_a_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_a_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.a_axis_dro_layout.addWidget(self.ref_a_button)


        self._2.addLayout(self.a_axis_dro_layout)

        self.c_axis_dro_layout = QHBoxLayout()
        self.c_axis_dro_layout.setSpacing(7)
        self.c_axis_dro_layout.setObjectName(u"c_axis_dro_layout")
        self.c_axis_dro_layout.setContentsMargins(1, 1, 1, 1)
        self.zero_c_button = MDIButton(self.widget_xyzac)
        self.zero_c_button.setObjectName(u"zero_c_button")
        self.zero_c_button.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.zero_c_button.sizePolicy().hasHeightForWidth())
        self.zero_c_button.setSizePolicy(sizePolicy1)
        self.zero_c_button.setMinimumSize(QSize(60, 40))
        self.zero_c_button.setMaximumSize(QSize(60, 40))
        self.zero_c_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_c_button.setStyleSheet(u"MDIButton {\n"
"   	font: 17pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.zero_c_button.setIcon(icon)
        self.zero_c_button.setIconSize(QSize(20, 20))

        self.c_axis_dro_layout.addWidget(self.zero_c_button)

        self.dro_entry_main_c = DROLineEdit(self.widget_xyzac)
        self.dro_entry_main_c.setObjectName(u"dro_entry_main_c")
        self.dro_entry_main_c.setMinimumSize(QSize(100, 35))
        self.dro_entry_main_c.setMaximumSize(QSize(100, 35))
        self.dro_entry_main_c.setFont(font)
        self.dro_entry_main_c.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_main_c.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_main_c.setProperty(u"referenceType", 1)
        self.dro_entry_main_c.setProperty(u"axisNumber", 5)
        self.dro_entry_main_c.setProperty(u"latheMode", 0)

        self.c_axis_dro_layout.addWidget(self.dro_entry_main_c)

        self.drolabel_machine_c = DROLabel(self.widget_xyzac)
        self.drolabel_machine_c.setObjectName(u"drolabel_machine_c")
        sizePolicy3.setHeightForWidth(self.drolabel_machine_c.sizePolicy().hasHeightForWidth())
        self.drolabel_machine_c.setSizePolicy(sizePolicy3)
        self.drolabel_machine_c.setMinimumSize(QSize(100, 35))
        self.drolabel_machine_c.setMaximumSize(QSize(100, 35))
        self.drolabel_machine_c.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_machine_c.setProperty(u"referenceType", 0)
        self.drolabel_machine_c.setProperty(u"axisNumber", 5)
        self.drolabel_machine_c.setProperty(u"latheMode", 0)

        self.c_axis_dro_layout.addWidget(self.drolabel_machine_c)

        self.drolabel_dtg_c = DROLabel(self.widget_xyzac)
        self.drolabel_dtg_c.setObjectName(u"drolabel_dtg_c")
        sizePolicy3.setHeightForWidth(self.drolabel_dtg_c.sizePolicy().hasHeightForWidth())
        self.drolabel_dtg_c.setSizePolicy(sizePolicy3)
        self.drolabel_dtg_c.setMinimumSize(QSize(100, 35))
        self.drolabel_dtg_c.setMaximumSize(QSize(100, 35))
        self.drolabel_dtg_c.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_dtg_c.setProperty(u"referenceType", 2)
        self.drolabel_dtg_c.setProperty(u"axisNumber", 5)
        self.drolabel_dtg_c.setProperty(u"latheMode", 0)

        self.c_axis_dro_layout.addWidget(self.drolabel_dtg_c)

        self.ref_c_button = ActionButton(self.widget_xyzac)
        self.ref_c_button.setObjectName(u"ref_c_button")
        sizePolicy2.setHeightForWidth(self.ref_c_button.sizePolicy().hasHeightForWidth())
        self.ref_c_button.setSizePolicy(sizePolicy2)
        self.ref_c_button.setMinimumSize(QSize(62, 40))
        self.ref_c_button.setMaximumSize(QSize(62, 40))
        self.ref_c_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.ref_c_button.setStyleSheet(u"QPushButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.c_axis_dro_layout.addWidget(self.ref_c_button)


        self._2.addLayout(self.c_axis_dro_layout)


        self.y_axis_dro_layout_2.addWidget(self.widget_xyzac)


        self.retranslateUi(dros_xyzac)

        QMetaObject.connectSlotsByName(dros_xyzac)
    # setupUi

    def retranslateUi(self, dros_xyzac):
        dros_xyzac.setWindowTitle(QCoreApplication.translate("dros_xyzac", u"dros_xyzac", None))
        self.zero_all_button.setText(QCoreApplication.translate("dros_xyzac", u"ALL", None))
        self.zero_all_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[\n"
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
        self.zero_all_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyzac", u"G10 L20 P{ch[0]} X0.0 Y0.0 Z0.0 A0.0 C0.0", None))
        self.work_column_header.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[{\"channels\": [{\"url\": \"status:g5x_index?text\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"ch[0] + ' WORK'\\n\", \"name\": \"WCS Header\"}]", None))
        self.machine_column_header.setText(QCoreApplication.translate("dros_xyzac", u"MACHINE", None))
        self.dtg_column_header.setText(QCoreApplication.translate("dros_xyzac", u"DTG", None))
        self.ref_all_button.setText(QCoreApplication.translate("dros_xyzac", u"REF ALL", None))
        self.ref_all_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[{\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"'HOMED' if ch[0] else 'REF ALL'\", \"name\": \"reference_all\"}, {\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3] or ch[4])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}, {\"url\": \"status:joint.4.homing\", \"trigger\": true}]}]", None))
        self.ref_all_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyzac", u"machine.home.all", None))
        self.zero_x_button.setText(QCoreApplication.translate("dros_xyzac", u"X", None))
        self.zero_x_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[\n"
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
        self.zero_x_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyzac", u"G10 L20 P{ch[0]} X0.0", None))
        self.dro_entry_main_x.setText("")
        self.dro_entry_main_x.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.dro_entry_main_x.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.dro_entry_main_x.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.dro_entry_main_x.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_machine_x.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_machine_x.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_machine_x.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_machine_x.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_dtg_x.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_dtg_x.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_dtg_x.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_dtg_x.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.ref_x_button_3.setText(QCoreApplication.translate("dros_xyzac", u"REF X", None))
        self.ref_x_button_3.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3] or ch[4])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}, {\"url\": \"status:joint.4.homing\", \"trigger\": true}]}]", None))
        self.ref_x_button_3.setProperty(u"actionName", QCoreApplication.translate("dros_xyzac", u"machine.home.axis:x", None))
        self.zero_y_button.setText(QCoreApplication.translate("dros_xyzac", u"Y", None))
        self.zero_y_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[\n"
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
        self.zero_y_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyzac", u"G10 L20 P{ch[0]} Y0.0", None))
        self.dro_entry_main_y.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_machine_y.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_machine_y.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_machine_y.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_machine_y.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_dtg_y.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_dtg_y.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_dtg_y.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_dtg_y.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.ref_y_button.setText(QCoreApplication.translate("dros_xyzac", u"REF Y", None))
        self.ref_y_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3] or ch[4])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}, {\"url\": \"status:joint.4.homing\", \"trigger\": true}]}]", None))
        self.ref_y_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyzac", u"machine.home.axis:y", None))
        self.zero_z_button.setText(QCoreApplication.translate("dros_xyzac", u"Z", None))
        self.zero_z_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[\n"
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
        self.zero_z_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyzac", u"G10 L20 P{ch[0]} Z0.0", None))
        self.dro_entry_main_z.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_machine_z.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_machine_z.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_machine_z.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_machine_z.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_dtg_z.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_dtg_z.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_dtg_z.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_dtg_z.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.ref_z_button.setText(QCoreApplication.translate("dros_xyzac", u"REF Z", None))
        self.ref_z_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3] or ch[4])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}, {\"url\": \"status:joint.4.homing\", \"trigger\": true}]}]", None))
        self.ref_z_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyzac", u"machine.home.axis:z", None))
        self.zero_a_button.setText(QCoreApplication.translate("dros_xyzac", u"A", None))
        self.zero_a_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[\n"
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
        self.zero_a_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyzac", u"G10 L20 P{ch[0]} A0.0", None))
        self.dro_entry_main_a.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_machine_a.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_machine_a.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_machine_a.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_machine_a.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_dtg_a.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_dtg_a.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_dtg_a.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_dtg_a.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.ref_a_button.setText(QCoreApplication.translate("dros_xyzac", u"REF A", None))
        self.ref_a_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3] or ch[4])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}, {\"url\": \"status:joint.4.homing\", \"trigger\": true}]}]", None))
        self.ref_a_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyzac", u"machine.home.axis:a", None))
        self.zero_c_button.setText(QCoreApplication.translate("dros_xyzac", u"C", None))
        self.zero_c_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[\n"
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
        self.zero_c_button.setProperty(u"MDICommand", QCoreApplication.translate("dros_xyzac", u"G10 L20 P{ch[0]} C0.0", None))
        self.dro_entry_main_c.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.dro_entry_main_c.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.dro_entry_main_c.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.dro_entry_main_c.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_machine_c.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_machine_c.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_machine_c.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_machine_c.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.drolabel_dtg_c.setProperty(u"inchFormat", QCoreApplication.translate("dros_xyzac", u"%9.4f", None))
        self.drolabel_dtg_c.setProperty(u"millimeterFormat", QCoreApplication.translate("dros_xyzac", u"%10.3f", None))
        self.drolabel_dtg_c.setProperty(u"degreeFormat", QCoreApplication.translate("dros_xyzac", u"%10.2f", None))
        self.drolabel_dtg_c.setProperty(u"styleSet", QCoreApplication.translate("dros_xyzac", u"dataField17", None))
        self.ref_c_button.setText(QCoreApplication.translate("dros_xyzac", u"REF C", None))
        self.ref_c_button.setProperty(u"rules", QCoreApplication.translate("dros_xyzac", u"[{\"name\": \"home_prohibit\", \"property\": \"Enable\", \"expression\": \"not (ch[0] or ch[1] or ch[2] or ch[3] or ch[4])\", \"channels\": [{\"url\": \"status:joint.0.homing\", \"trigger\": true}, {\"url\": \"status:joint.1.homing\", \"trigger\": true}, {\"url\": \"status:joint.2.homing\", \"trigger\": true}, {\"url\": \"status:joint.3.homing\", \"trigger\": true}, {\"url\": \"status:joint.4.homing\", \"trigger\": true}]}]", None))
        self.ref_c_button.setProperty(u"actionName", QCoreApplication.translate("dros_xyzac", u"machine.home.axis:c", None))
    # retranslateUi

