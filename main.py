#Developed By Sihab Sahariar

from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt ,QTime, QTimer, QPoint, QPointF, QRect, QSize
from PyQt5.QtWidgets import QMessageBox
from analoggaugewidget import AnalogGaugeWidget
from compass import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Sensor Dashboard v1.0")
        MainWindow.resize(1106, 811)
        MainWindow.setStyleSheet("\n"
"    background-color: rgb(27, 19, 57);\n"
"\n"
"    color: rgb(220, 220, 220);\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setLineWidth(4)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line, 0, QtCore.Qt.AlignVCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setContentsMargins(2, 0, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setStyleSheet("color:white")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignTop)
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.w1 =AnalogGaugeWidget(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w1.sizePolicy().hasHeightForWidth())
        self.w1.setSizePolicy(sizePolicy)
        self.w1.setStyleSheet("background-color: rgb(62,45,84)")
        self.w1.setObjectName("w1")
        self.verticalLayout_5.addWidget(self.w1)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.horizontalLayout.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setStyleSheet("")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.w2 = AnalogGaugeWidget(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w2.sizePolicy().hasHeightForWidth())
        self.w2.setSizePolicy(sizePolicy)
        self.w2.setStyleSheet("background-color: rgb(62,45,84)")
        self.w2.setObjectName("w2")
        self.verticalLayout_6.addWidget(self.w2)
        self.horizontalLayout.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_5)
        self.frame_8.setStyleSheet("")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setStyleSheet("color:white")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_11.addWidget(self.label_8, 0, QtCore.Qt.AlignTop)
        self.w3 = AnalogGaugeWidget(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w3.sizePolicy().hasHeightForWidth())
        self.w3.setSizePolicy(sizePolicy)
        self.w3.setStyleSheet("background-color: rgb(62,45,84)")
        self.w3.setObjectName("w3")
        self.verticalLayout_11.addWidget(self.w3)
        self.horizontalLayout.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_5)
        self.frame_9.setStyleSheet("")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_9 = QtWidgets.QLabel(self.frame_9)
        self.label_9.setStyleSheet("color:white")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.label_9, 0, QtCore.Qt.AlignTop)
        self.w4 = AnalogGaugeWidget(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w4.sizePolicy().hasHeightForWidth())
        self.w4.setSizePolicy(sizePolicy)
        self.w4.setStyleSheet("background-color: rgb(62,45,84)")
        self.w4.setObjectName("w4")
        self.verticalLayout_12.addWidget(self.w4)
        self.horizontalLayout.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        self.frame_12.setStyleSheet("")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_12)
        self.label_7.setStyleSheet("color:white")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7, 0, QtCore.Qt.AlignTop)
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.w5 = AnalogGaugeWidget(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w5.sizePolicy().hasHeightForWidth())
        self.w5.setSizePolicy(sizePolicy)
        self.w5.setStyleSheet("background-color: rgb(62,45,84)")
        self.w5.setObjectName("w5")
        self.verticalLayout_9.addWidget(self.w5)
        self.verticalLayout_8.addWidget(self.frame_13)
        self.horizontalLayout_2.addWidget(self.frame_12)
        self.frame_11 = QtWidgets.QFrame(self.frame_4)
        self.frame_11.setStyleSheet("")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6, 0, QtCore.Qt.AlignTop)
        self.compass = CompassWidget(self.frame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compass.sizePolicy().hasHeightForWidth())
        self.compass.setSizePolicy(sizePolicy)
        #self.compass.setStyleSheet("background-color: rgb(62,45,84)")
        self.compass.setObjectName("compass")
        self.verticalLayout_7.addWidget(self.compass)
        self.horizontalLayout_2.addWidget(self.frame_11)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_14 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet("background-color: rgb(29, 29, 33);")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 4)
        self.verticalLayout_10.setSpacing(7)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout.setContentsMargins(7, 0, 7, 7)
        self.gridLayout.setSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.sensor = PlotWidget(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sensor.sizePolicy().hasHeightForWidth())
        self.sensor.setSizePolicy(sizePolicy)
        self.sensor.setStyleSheet("background-color: rgb(62,45,84)")
        self.sensor.setObjectName("sensor")
        self.gridLayout.addWidget(self.sensor, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_16)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1, QtCore.Qt.AlignTop)
        self.verticalLayout_10.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_17.setBaseSize(QtCore.QSize(200, 50))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_4.setContentsMargins(7, 0, 7, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.control = QtWidgets.QPushButton(self.frame_17)
        self.control.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.control.setFont(font)
        self.control.setStyleSheet("QPushButton{\n"
"    color:#fff;\n"
"    background-color: rgb(0, 123, 210);\n"
"    border: 1px solid rgb(0,123,210);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 123, 210);\n"
"    border: 1px solid rgba(255,255,255,150);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(113, 113, 113);\n"
"    border: 1px solid rgb(113, 113, 113);\n"
"}")
        self.control.setFlat(True)
        self.control.setObjectName("control")
        self.horizontalLayout_4.addWidget(self.control)
        self.About = QtWidgets.QPushButton(self.frame_17)
        self.About.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.About.setFont(font)
        self.About.setStyleSheet("QPushButton{\n"
"    color:#fff;\n"
"    background-color: rgb(0, 123, 210);\n"
"    border: 1px solid rgb(0,123,210);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 123, 210);\n"
"    border: 1px solid rgba(255,255,255,150);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(113, 113, 113);\n"
"    border: 1px solid rgb(113, 113, 113);\n"
"}")
        self.About.setFlat(True)
        self.About.setObjectName("About")
        self.horizontalLayout_4.addWidget(self.About)
        self.Quit = QtWidgets.QPushButton(self.frame_17)
        self.Quit.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.Quit.setFont(font)
        self.Quit.setStyleSheet("QPushButton{\n"
"    color : #fff;\n"
"    background-color: rgb(0, 123, 210);\n"
"    border: 1px solid rgb(0,123,210);\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(0, 123, 210);\n"
"    border: 1px solid rgba(255,255,255,150);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(113, 113, 113);\n"
"    border: 1px solid rgb(113, 113, 113);\n"
"}")
        self.Quit.setFlat(True)
        self.Quit.setObjectName("Quit")
        self.horizontalLayout_4.addWidget(self.Quit)
        self.verticalLayout_10.addWidget(self.frame_17)
        self.horizontalLayout_3.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setStyleSheet("background-color: rgb(29, 29, 33);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.frame_18)
        self.label_12.setStyleSheet("color:white")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_5.addWidget(self.label_12)
        self.verticalLayout_13.addWidget(self.frame_18)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.p1 = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p1.sizePolicy().hasHeightForWidth())
        self.p1.setSizePolicy(sizePolicy)
        self.p1.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.p1.setProperty("value", 79)
        self.p1.setOrientation(QtCore.Qt.Vertical)
        self.p1.setObjectName("p1")
        self.horizontalLayout_6.addWidget(self.p1)
        self.p2 = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p2.sizePolicy().hasHeightForWidth())
        self.p2.setSizePolicy(sizePolicy)
        self.p2.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.p2.setProperty("value", 88)
        self.p2.setOrientation(QtCore.Qt.Vertical)
        self.p2.setObjectName("p2")
        self.horizontalLayout_6.addWidget(self.p2)
        self.p3 = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p3.sizePolicy().hasHeightForWidth())
        self.p3.setSizePolicy(sizePolicy)
        self.p3.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.p3.setProperty("value", 14)
        self.p3.setOrientation(QtCore.Qt.Vertical)
        self.p3.setObjectName("p3")
        self.horizontalLayout_6.addWidget(self.p3)
        self.p4 = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.p4.sizePolicy().hasHeightForWidth())
        self.p4.setSizePolicy(sizePolicy)
        self.p4.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.p4.setProperty("value", 69)
        self.p4.setOrientation(QtCore.Qt.Vertical)
        self.p4.setObjectName("p4")
        self.horizontalLayout_6.addWidget(self.p4)
        self.progressBar_6 = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_6.sizePolicy().hasHeightForWidth())
        self.progressBar_6.setSizePolicy(sizePolicy)
        self.progressBar_6.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.progressBar_6.setProperty("value", 12)
        self.progressBar_6.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_6.setObjectName("progressBar_6")
        self.horizontalLayout_6.addWidget(self.progressBar_6)
        self.progressBar = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.progressBar.setProperty("value", 56)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_6.addWidget(self.progressBar)
        self.progressBar_4 = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_4.sizePolicy().hasHeightForWidth())
        self.progressBar_4.setSizePolicy(sizePolicy)
        self.progressBar_4.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.progressBar_4.setMaximum(99)
        self.progressBar_4.setProperty("value", 32)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setObjectName("progressBar_4")
        self.horizontalLayout_6.addWidget(self.progressBar_4)
        self.progressBar_5 = QtWidgets.QProgressBar(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_5.sizePolicy().hasHeightForWidth())
        self.progressBar_5.setSizePolicy(sizePolicy)
        self.progressBar_5.setStyleSheet("QProgressBar::chunk{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(82, 64, 157);\n"
"    color: #fff;\n"
"    border-style: none;\n"
"    \n"
"    text-align: center;\n"
"    height: 50px;\n"
"}\n"
"\n"
"")
        self.progressBar_5.setProperty("value", 57)
        self.progressBar_5.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_5.setObjectName("progressBar_5")
        self.horizontalLayout_6.addWidget(self.progressBar_5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addWidget(self.frame_15)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "SENSOR DASHBOARD v1.0"))
        self.label_4.setText(_translate("MainWindow", "SENSOR 1"))
        self.label_5.setText(_translate("MainWindow", "SENSOR 2"))
        self.label_8.setText(_translate("MainWindow", "SENSOR3"))
        self.label_9.setText(_translate("MainWindow", "SENSOR4"))
        self.label_7.setText(_translate("MainWindow", "SENSOR 5"))
        self.label_6.setText(_translate("MainWindow", "COMPASS"))
        self.label_3.setText(_translate("MainWindow", "SENSOR GRAPH"))
        self.control.setText(_translate("MainWindow", "Refresh"))
        self.About.setText(_translate("MainWindow", "About Developer"))
        self.Quit.setText(_translate("MainWindow", "Quit"))
        self.label_12.setText(_translate("MainWindow", "REAL TIME DATA READ"))

        self.Quit.clicked.connect(self.close)
        self.About.clicked.connect(self.About_)
        self.control.clicked.connect(self.refresh)
        self.gauge()
        self.changeCompass()
        self.plot([1,2,3,4,5,5,5,6,9,10], [30,32,34,32,33,31,29,32,35,45])
        
    def refresh(self):
    	pass

    def About_(self):
        QMessageBox.about(MainWindow, "About", "This application is developed by Sihab Sahariar")    
    def close(self):
    	MainWindow.close()    
    def plot(self, hour, temperature):
        self.sensor.plot(hour, temperature)
        x = self.sensor.getViewBox()
        x.setBackgroundColor((62,45,84))

    def changeCompass(self):
        self.compass.setAngle(35)

    def gauge(self):
        self.w1.update_value(150)
        self.w2.update_value(50)
        self.w3.update_value(200)
        self.w4.update_value(650)
        self.w5.update_value(700)
        self.color(self.w1)
        self.color(self.w2)
        self.color(self.w3)
        self.color(self.w4)
        self.color(self.w5)
        self.w1.set_scale_polygon_colors([[.00, Qt.darkCyan]])
        self.w2.set_scale_polygon_colors([[.00, Qt.darkCyan]])
        self.w3.set_scale_polygon_colors([[.00, Qt.darkCyan]])
        self.w4.set_scale_polygon_colors([[.00, Qt.darkCyan]])
        self.w5.set_scale_polygon_colors([[.00, Qt.darkCyan]])
    def color(self,obj):
        obj.set_DisplayValueColor(255,255,255)
        obj.set_NeedleColor(255,255,255)
        obj.set_ScaleValueColor(255,255,255)
        obj.set_CenterPointColor(255,255,255)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
