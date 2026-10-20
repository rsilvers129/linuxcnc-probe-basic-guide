# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'offset_dros_xyza.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.status_label import StatusLabel
from qtpyvcp.widgets.input_widgets.dro_line_edit import DROLineEdit
import probe_basic_rc

class Ui_offset_dros_xyza(object):
    def setupUi(self, offset_dros_xyza):
        if not offset_dros_xyza.objectName():
            offset_dros_xyza.setObjectName(u"offset_dros_xyza")
        offset_dros_xyza.resize(493, 220)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(offset_dros_xyza.sizePolicy().hasHeightForWidth())
        offset_dros_xyza.setSizePolicy(sizePolicy)
        offset_dros_xyza.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout = QVBoxLayout(offset_dros_xyza)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.x_axis_dro_layout_6 = QHBoxLayout()
        self.x_axis_dro_layout_6.setSpacing(12)
        self.x_axis_dro_layout_6.setObjectName(u"x_axis_dro_layout_6")
        self.x_axis_dro_layout_6.setContentsMargins(-1, 4, -1, 4)
        self.zero_x_button_offset = MDIButton(offset_dros_xyza)
        self.zero_x_button_offset.setObjectName(u"zero_x_button_offset")
        self.zero_x_button_offset.setEnabled(False)
        self.zero_x_button_offset.setMinimumSize(QSize(55, 38))
        self.zero_x_button_offset.setMaximumSize(QSize(55, 38))
        self.zero_x_button_offset.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_x_button_offset.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.x_axis_dro_layout_6.addWidget(self.zero_x_button_offset)

        self.axis_label_x = QLabel(offset_dros_xyza)
        self.axis_label_x.setObjectName(u"axis_label_x")
        sizePolicy.setHeightForWidth(self.axis_label_x.sizePolicy().hasHeightForWidth())
        self.axis_label_x.setSizePolicy(sizePolicy)
        self.axis_label_x.setMinimumSize(QSize(45, 35))
        self.axis_label_x.setMaximumSize(QSize(45, 35))
        self.axis_label_x.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_label_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.x_axis_dro_layout_6.addWidget(self.axis_label_x)

        self.dro_entry_offset_x = DROLineEdit(offset_dros_xyza)
        self.dro_entry_offset_x.setObjectName(u"dro_entry_offset_x")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dro_entry_offset_x.sizePolicy().hasHeightForWidth())
        self.dro_entry_offset_x.setSizePolicy(sizePolicy1)
        self.dro_entry_offset_x.setMinimumSize(QSize(0, 38))
        self.dro_entry_offset_x.setMaximumSize(QSize(16777215, 38))
        font = QFont()
        font.setFamilies([u"Probe Basic Bebas Mono"])
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        self.dro_entry_offset_x.setFont(font)
        self.dro_entry_offset_x.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_offset_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.x_axis_dro_layout_6.addWidget(self.dro_entry_offset_x)

        self.drolabel_work_x = DROLabel(offset_dros_xyza)
        self.drolabel_work_x.setObjectName(u"drolabel_work_x")
        sizePolicy1.setHeightForWidth(self.drolabel_work_x.sizePolicy().hasHeightForWidth())
        self.drolabel_work_x.setSizePolicy(sizePolicy1)
        self.drolabel_work_x.setMinimumSize(QSize(0, 38))
        self.drolabel_work_x.setMaximumSize(QSize(16777215, 38))
        self.drolabel_work_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_work_x.setProperty(u"referenceType", 0)
        self.drolabel_work_x.setProperty(u"axisNumber", 0)
        self.drolabel_work_x.setProperty(u"latheMode", 0)

        self.x_axis_dro_layout_6.addWidget(self.drolabel_work_x)

        self.work_offset_x = StatusLabel(offset_dros_xyza)
        self.work_offset_x.setObjectName(u"work_offset_x")
        sizePolicy1.setHeightForWidth(self.work_offset_x.sizePolicy().hasHeightForWidth())
        self.work_offset_x.setSizePolicy(sizePolicy1)
        self.work_offset_x.setMinimumSize(QSize(0, 38))
        self.work_offset_x.setMaximumSize(QSize(16777215, 38))
        self.work_offset_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.x_axis_dro_layout_6.addWidget(self.work_offset_x)

        self.g52_g92_x = StatusLabel(offset_dros_xyza)
        self.g52_g92_x.setObjectName(u"g52_g92_x")
        sizePolicy1.setHeightForWidth(self.g52_g92_x.sizePolicy().hasHeightForWidth())
        self.g52_g92_x.setSizePolicy(sizePolicy1)
        self.g52_g92_x.setMinimumSize(QSize(0, 38))
        self.g52_g92_x.setMaximumSize(QSize(16777215, 38))
        self.g52_g92_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.x_axis_dro_layout_6.addWidget(self.g52_g92_x)

        self.tool_offset_x = StatusLabel(offset_dros_xyza)
        self.tool_offset_x.setObjectName(u"tool_offset_x")
        sizePolicy1.setHeightForWidth(self.tool_offset_x.sizePolicy().hasHeightForWidth())
        self.tool_offset_x.setSizePolicy(sizePolicy1)
        self.tool_offset_x.setMinimumSize(QSize(0, 38))
        self.tool_offset_x.setMaximumSize(QSize(16777215, 38))
        self.tool_offset_x.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.x_axis_dro_layout_6.addWidget(self.tool_offset_x)


        self.verticalLayout.addLayout(self.x_axis_dro_layout_6)

        self.y_axis_dro_layout_6 = QHBoxLayout()
        self.y_axis_dro_layout_6.setSpacing(12)
        self.y_axis_dro_layout_6.setObjectName(u"y_axis_dro_layout_6")
        self.y_axis_dro_layout_6.setContentsMargins(-1, 4, -1, 4)
        self.zero_y_button_offset = MDIButton(offset_dros_xyza)
        self.zero_y_button_offset.setObjectName(u"zero_y_button_offset")
        self.zero_y_button_offset.setEnabled(False)
        self.zero_y_button_offset.setMinimumSize(QSize(55, 38))
        self.zero_y_button_offset.setMaximumSize(QSize(55, 38))
        self.zero_y_button_offset.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_y_button_offset.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.y_axis_dro_layout_6.addWidget(self.zero_y_button_offset)

        self.axis_label_y = QLabel(offset_dros_xyza)
        self.axis_label_y.setObjectName(u"axis_label_y")
        self.axis_label_y.setMinimumSize(QSize(45, 35))
        self.axis_label_y.setMaximumSize(QSize(45, 35))
        self.axis_label_y.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_label_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.y_axis_dro_layout_6.addWidget(self.axis_label_y)

        self.dro_entry_offset_y = DROLineEdit(offset_dros_xyza)
        self.dro_entry_offset_y.setObjectName(u"dro_entry_offset_y")
        sizePolicy1.setHeightForWidth(self.dro_entry_offset_y.sizePolicy().hasHeightForWidth())
        self.dro_entry_offset_y.setSizePolicy(sizePolicy1)
        self.dro_entry_offset_y.setMinimumSize(QSize(0, 38))
        self.dro_entry_offset_y.setMaximumSize(QSize(16777215, 38))
        self.dro_entry_offset_y.setFont(font)
        self.dro_entry_offset_y.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_offset_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_offset_y.setProperty(u"axisNumber", 1)

        self.y_axis_dro_layout_6.addWidget(self.dro_entry_offset_y)

        self.drolabel_work_y = DROLabel(offset_dros_xyza)
        self.drolabel_work_y.setObjectName(u"drolabel_work_y")
        sizePolicy1.setHeightForWidth(self.drolabel_work_y.sizePolicy().hasHeightForWidth())
        self.drolabel_work_y.setSizePolicy(sizePolicy1)
        self.drolabel_work_y.setMinimumSize(QSize(0, 38))
        self.drolabel_work_y.setMaximumSize(QSize(16777215, 38))
        self.drolabel_work_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_work_y.setProperty(u"referenceType", 0)
        self.drolabel_work_y.setProperty(u"axisNumber", 1)
        self.drolabel_work_y.setProperty(u"latheMode", 0)

        self.y_axis_dro_layout_6.addWidget(self.drolabel_work_y)

        self.work_offset_y = StatusLabel(offset_dros_xyza)
        self.work_offset_y.setObjectName(u"work_offset_y")
        sizePolicy1.setHeightForWidth(self.work_offset_y.sizePolicy().hasHeightForWidth())
        self.work_offset_y.setSizePolicy(sizePolicy1)
        self.work_offset_y.setMinimumSize(QSize(0, 38))
        self.work_offset_y.setMaximumSize(QSize(16777215, 38))
        self.work_offset_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.y_axis_dro_layout_6.addWidget(self.work_offset_y)

        self.g52_g92_y = StatusLabel(offset_dros_xyza)
        self.g52_g92_y.setObjectName(u"g52_g92_y")
        sizePolicy1.setHeightForWidth(self.g52_g92_y.sizePolicy().hasHeightForWidth())
        self.g52_g92_y.setSizePolicy(sizePolicy1)
        self.g52_g92_y.setMinimumSize(QSize(0, 38))
        self.g52_g92_y.setMaximumSize(QSize(16777215, 38))
        self.g52_g92_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.y_axis_dro_layout_6.addWidget(self.g52_g92_y)

        self.tool_offset_y = StatusLabel(offset_dros_xyza)
        self.tool_offset_y.setObjectName(u"tool_offset_y")
        sizePolicy1.setHeightForWidth(self.tool_offset_y.sizePolicy().hasHeightForWidth())
        self.tool_offset_y.setSizePolicy(sizePolicy1)
        self.tool_offset_y.setMinimumSize(QSize(0, 38))
        self.tool_offset_y.setMaximumSize(QSize(16777215, 38))
        self.tool_offset_y.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.y_axis_dro_layout_6.addWidget(self.tool_offset_y)


        self.verticalLayout.addLayout(self.y_axis_dro_layout_6)

        self.z_axis_dro_layout_6 = QHBoxLayout()
        self.z_axis_dro_layout_6.setSpacing(12)
        self.z_axis_dro_layout_6.setObjectName(u"z_axis_dro_layout_6")
        self.z_axis_dro_layout_6.setContentsMargins(-1, 4, -1, 4)
        self.zero_z_button_offset = MDIButton(offset_dros_xyza)
        self.zero_z_button_offset.setObjectName(u"zero_z_button_offset")
        self.zero_z_button_offset.setEnabled(False)
        self.zero_z_button_offset.setMinimumSize(QSize(55, 38))
        self.zero_z_button_offset.setMaximumSize(QSize(55, 38))
        self.zero_z_button_offset.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_z_button_offset.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.z_axis_dro_layout_6.addWidget(self.zero_z_button_offset)

        self.axis_label_z = QLabel(offset_dros_xyza)
        self.axis_label_z.setObjectName(u"axis_label_z")
        self.axis_label_z.setMinimumSize(QSize(45, 35))
        self.axis_label_z.setMaximumSize(QSize(45, 35))
        self.axis_label_z.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_label_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.z_axis_dro_layout_6.addWidget(self.axis_label_z)

        self.dro_entry_offset_z = DROLineEdit(offset_dros_xyza)
        self.dro_entry_offset_z.setObjectName(u"dro_entry_offset_z")
        sizePolicy1.setHeightForWidth(self.dro_entry_offset_z.sizePolicy().hasHeightForWidth())
        self.dro_entry_offset_z.setSizePolicy(sizePolicy1)
        self.dro_entry_offset_z.setMinimumSize(QSize(0, 38))
        self.dro_entry_offset_z.setMaximumSize(QSize(16777215, 38))
        self.dro_entry_offset_z.setFont(font)
        self.dro_entry_offset_z.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_offset_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_offset_z.setProperty(u"axisNumber", 2)

        self.z_axis_dro_layout_6.addWidget(self.dro_entry_offset_z)

        self.drolabel_work_z = DROLabel(offset_dros_xyza)
        self.drolabel_work_z.setObjectName(u"drolabel_work_z")
        sizePolicy1.setHeightForWidth(self.drolabel_work_z.sizePolicy().hasHeightForWidth())
        self.drolabel_work_z.setSizePolicy(sizePolicy1)
        self.drolabel_work_z.setMinimumSize(QSize(0, 38))
        self.drolabel_work_z.setMaximumSize(QSize(16777215, 38))
        self.drolabel_work_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_work_z.setProperty(u"referenceType", 0)
        self.drolabel_work_z.setProperty(u"axisNumber", 2)
        self.drolabel_work_z.setProperty(u"latheMode", 0)

        self.z_axis_dro_layout_6.addWidget(self.drolabel_work_z)

        self.work_offset_z = StatusLabel(offset_dros_xyza)
        self.work_offset_z.setObjectName(u"work_offset_z")
        sizePolicy1.setHeightForWidth(self.work_offset_z.sizePolicy().hasHeightForWidth())
        self.work_offset_z.setSizePolicy(sizePolicy1)
        self.work_offset_z.setMinimumSize(QSize(0, 38))
        self.work_offset_z.setMaximumSize(QSize(16777215, 38))
        self.work_offset_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.z_axis_dro_layout_6.addWidget(self.work_offset_z)

        self.g52_g92_z = StatusLabel(offset_dros_xyza)
        self.g52_g92_z.setObjectName(u"g52_g92_z")
        sizePolicy1.setHeightForWidth(self.g52_g92_z.sizePolicy().hasHeightForWidth())
        self.g52_g92_z.setSizePolicy(sizePolicy1)
        self.g52_g92_z.setMinimumSize(QSize(0, 38))
        self.g52_g92_z.setMaximumSize(QSize(16777215, 38))
        self.g52_g92_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.z_axis_dro_layout_6.addWidget(self.g52_g92_z)

        self.tool_offset_z = StatusLabel(offset_dros_xyza)
        self.tool_offset_z.setObjectName(u"tool_offset_z")
        sizePolicy1.setHeightForWidth(self.tool_offset_z.sizePolicy().hasHeightForWidth())
        self.tool_offset_z.setSizePolicy(sizePolicy1)
        self.tool_offset_z.setMinimumSize(QSize(0, 38))
        self.tool_offset_z.setMaximumSize(QSize(16777215, 38))
        self.tool_offset_z.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.z_axis_dro_layout_6.addWidget(self.tool_offset_z)


        self.verticalLayout.addLayout(self.z_axis_dro_layout_6)

        self.a_axis_dro_layout_5 = QHBoxLayout()
        self.a_axis_dro_layout_5.setSpacing(12)
        self.a_axis_dro_layout_5.setObjectName(u"a_axis_dro_layout_5")
        self.a_axis_dro_layout_5.setContentsMargins(-1, 4, -1, 4)
        self.zero_a_button_offset = MDIButton(offset_dros_xyza)
        self.zero_a_button_offset.setObjectName(u"zero_a_button_offset")
        self.zero_a_button_offset.setEnabled(False)
        self.zero_a_button_offset.setMinimumSize(QSize(55, 38))
        self.zero_a_button_offset.setMaximumSize(QSize(55, 38))
        self.zero_a_button_offset.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.zero_a_button_offset.setStyleSheet(u"MDIButton {\n"
"   	font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")

        self.a_axis_dro_layout_5.addWidget(self.zero_a_button_offset)

        self.axis_label_a = QLabel(offset_dros_xyza)
        self.axis_label_a.setObjectName(u"axis_label_a")
        self.axis_label_a.setMinimumSize(QSize(45, 35))
        self.axis_label_a.setMaximumSize(QSize(45, 35))
        self.axis_label_a.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(235, 235, 235);\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: rgb(238, 238, 236);\n"
"	font: 18pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.axis_label_a.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.a_axis_dro_layout_5.addWidget(self.axis_label_a)

        self.dro_entry_offset_a = DROLineEdit(offset_dros_xyza)
        self.dro_entry_offset_a.setObjectName(u"dro_entry_offset_a")
        sizePolicy1.setHeightForWidth(self.dro_entry_offset_a.sizePolicy().hasHeightForWidth())
        self.dro_entry_offset_a.setSizePolicy(sizePolicy1)
        self.dro_entry_offset_a.setMinimumSize(QSize(0, 38))
        self.dro_entry_offset_a.setMaximumSize(QSize(16777215, 38))
        self.dro_entry_offset_a.setFont(font)
        self.dro_entry_offset_a.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.dro_entry_offset_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.dro_entry_offset_a.setProperty(u"axisNumber", 3)

        self.a_axis_dro_layout_5.addWidget(self.dro_entry_offset_a)

        self.drolabel_work_a = DROLabel(offset_dros_xyza)
        self.drolabel_work_a.setObjectName(u"drolabel_work_a")
        sizePolicy1.setHeightForWidth(self.drolabel_work_a.sizePolicy().hasHeightForWidth())
        self.drolabel_work_a.setSizePolicy(sizePolicy1)
        self.drolabel_work_a.setMinimumSize(QSize(0, 38))
        self.drolabel_work_a.setMaximumSize(QSize(16777215, 38))
        self.drolabel_work_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.drolabel_work_a.setProperty(u"referenceType", 0)
        self.drolabel_work_a.setProperty(u"axisNumber", 3)
        self.drolabel_work_a.setProperty(u"latheMode", 0)

        self.a_axis_dro_layout_5.addWidget(self.drolabel_work_a)

        self.work_offset_a = StatusLabel(offset_dros_xyza)
        self.work_offset_a.setObjectName(u"work_offset_a")
        sizePolicy1.setHeightForWidth(self.work_offset_a.sizePolicy().hasHeightForWidth())
        self.work_offset_a.setSizePolicy(sizePolicy1)
        self.work_offset_a.setMinimumSize(QSize(0, 38))
        self.work_offset_a.setMaximumSize(QSize(16777215, 38))
        self.work_offset_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.a_axis_dro_layout_5.addWidget(self.work_offset_a)

        self.g52_g92_a = StatusLabel(offset_dros_xyza)
        self.g52_g92_a.setObjectName(u"g52_g92_a")
        sizePolicy1.setHeightForWidth(self.g52_g92_a.sizePolicy().hasHeightForWidth())
        self.g52_g92_a.setSizePolicy(sizePolicy1)
        self.g52_g92_a.setMinimumSize(QSize(0, 38))
        self.g52_g92_a.setMaximumSize(QSize(16777215, 38))
        self.g52_g92_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.a_axis_dro_layout_5.addWidget(self.g52_g92_a)

        self.tool_offset_a = StatusLabel(offset_dros_xyza)
        self.tool_offset_a.setObjectName(u"tool_offset_a")
        sizePolicy1.setHeightForWidth(self.tool_offset_a.sizePolicy().hasHeightForWidth())
        self.tool_offset_a.setSizePolicy(sizePolicy1)
        self.tool_offset_a.setMinimumSize(QSize(0, 38))
        self.tool_offset_a.setMaximumSize(QSize(16777215, 38))
        self.tool_offset_a.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.a_axis_dro_layout_5.addWidget(self.tool_offset_a)


        self.verticalLayout.addLayout(self.a_axis_dro_layout_5)


        self.retranslateUi(offset_dros_xyza)

        QMetaObject.connectSlotsByName(offset_dros_xyza)
    # setupUi

    def retranslateUi(self, offset_dros_xyza):
        offset_dros_xyza.setWindowTitle(QCoreApplication.translate("offset_dros_xyza", u"offset_dros_xyza", None))
        self.zero_x_button_offset.setText(QCoreApplication.translate("offset_dros_xyza", u"ZERO", None))
        self.zero_x_button_offset.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[\n"
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
        self.zero_x_button_offset.setProperty(u"MDICommand", QCoreApplication.translate("offset_dros_xyza", u"G10 L20 P{ch[0]} X0.0", None))
        self.axis_label_x.setText(QCoreApplication.translate("offset_dros_xyza", u"X", None))
        self.dro_entry_offset_x.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.drolabel_work_x.setProperty(u"inchFormat", QCoreApplication.translate("offset_dros_xyza", u"%9.4f", None))
        self.drolabel_work_x.setProperty(u"millimeterFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.3f", None))
        self.drolabel_work_x.setProperty(u"degreeFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.2f", None))
        self.drolabel_work_x.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.work_offset_x.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.work_offset_x.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.g52_g92_x.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.g52_g92_x.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.tool_offset_x.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][0])\", \"name\": \"New Rule\"}]", None))
        self.tool_offset_x.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.zero_y_button_offset.setText(QCoreApplication.translate("offset_dros_xyza", u"ZERO", None))
        self.zero_y_button_offset.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[\n"
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
        self.zero_y_button_offset.setProperty(u"MDICommand", QCoreApplication.translate("offset_dros_xyza", u"G10 L20 P{ch[0]} Y0.0", None))
        self.axis_label_y.setText(QCoreApplication.translate("offset_dros_xyza", u"Y", None))
        self.dro_entry_offset_y.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.drolabel_work_y.setProperty(u"inchFormat", QCoreApplication.translate("offset_dros_xyza", u"%9.4f", None))
        self.drolabel_work_y.setProperty(u"millimeterFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.3f", None))
        self.drolabel_work_y.setProperty(u"degreeFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.2f", None))
        self.drolabel_work_y.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.work_offset_y.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.work_offset_y.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.g52_g92_y.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.g52_g92_y.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.tool_offset_y.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][1])\", \"name\": \"New Rule\"}]", None))
        self.tool_offset_y.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.zero_z_button_offset.setText(QCoreApplication.translate("offset_dros_xyza", u"ZERO", None))
        self.zero_z_button_offset.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[\n"
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
        self.zero_z_button_offset.setProperty(u"MDICommand", QCoreApplication.translate("offset_dros_xyza", u"G10 L20 P{ch[0]} Z0.0", None))
        self.axis_label_z.setText(QCoreApplication.translate("offset_dros_xyza", u"Z", None))
        self.dro_entry_offset_z.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.drolabel_work_z.setProperty(u"inchFormat", QCoreApplication.translate("offset_dros_xyza", u"%9.4f", None))
        self.drolabel_work_z.setProperty(u"millimeterFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.3f", None))
        self.drolabel_work_z.setProperty(u"degreeFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.2f", None))
        self.drolabel_work_z.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.work_offset_z.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]", None))
        self.work_offset_z.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.g52_g92_z.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"New Rule\"}]", None))
        self.g52_g92_z.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.tool_offset_z.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"url\": \"status:tool_offset\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][2])\", \"name\": \"tool offset\"}]", None))
        self.tool_offset_z.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.zero_a_button_offset.setText(QCoreApplication.translate("offset_dros_xyza", u"ZERO", None))
        self.zero_a_button_offset.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[\n"
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
        self.zero_a_button_offset.setProperty(u"MDICommand", QCoreApplication.translate("offset_dros_xyza", u"G10 L20 P{ch[0]} A0.0", None))
        self.axis_label_a.setText(QCoreApplication.translate("offset_dros_xyza", u"A", None))
        self.dro_entry_offset_a.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.drolabel_work_a.setProperty(u"inchFormat", QCoreApplication.translate("offset_dros_xyza", u"%9.4f", None))
        self.drolabel_work_a.setProperty(u"millimeterFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.3f", None))
        self.drolabel_work_a.setProperty(u"degreeFormat", QCoreApplication.translate("offset_dros_xyza", u"%10.2f", None))
        self.drolabel_work_a.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.work_offset_a.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g92_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.work_offset_a.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.g52_g92_a.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:g5x_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.g52_g92_a.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
        self.tool_offset_a.setProperty(u"rules", QCoreApplication.translate("offset_dros_xyza", u"[{\"channels\": [{\"trigger\": true, \"type\": \"tuple\", \"url\": \"status:tool_offset\"}], \"property\": \"Text\", \"expression\": \"\\\"{:.4f}\\\".format(ch[0][3])\", \"name\": \"New Rule\"}]", None))
        self.tool_offset_a.setProperty(u"styleSet", QCoreApplication.translate("offset_dros_xyza", u"dataField17", None))
    # retranslateUi

