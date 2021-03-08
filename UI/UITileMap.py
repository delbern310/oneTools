# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UITileMap.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1255, 750)
        self.splitter = CollapsibleSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 10, 841, 721))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 548, 690))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(20, -1, 10, -1)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.rbtn_onlyHandle = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.rbtn_onlyHandle.setFont(font)
        self.rbtn_onlyHandle.setObjectName("rbtn_onlyHandle")
        self.horizontalLayout_1.addWidget(self.rbtn_onlyHandle)
        self.rbtn_spiderAndHandle = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.rbtn_spiderAndHandle.setFont(font)
        self.rbtn_spiderAndHandle.setObjectName("rbtn_spiderAndHandle")
        self.horizontalLayout_1.addWidget(self.rbtn_spiderAndHandle)
        self.rbtn_onlySpider = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.rbtn_onlySpider.setFont(font)
        self.rbtn_onlySpider.setObjectName("rbtn_onlySpider")
        self.horizontalLayout_1.addWidget(self.rbtn_onlySpider)
        self.verticalLayout_4.addLayout(self.horizontalLayout_1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.txt_addressFile = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.txt_addressFile.setObjectName("txt_addressFile")
        self.horizontalLayout_4.addWidget(self.txt_addressFile)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.btn_addressFile = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addressFile.sizePolicy().hasHeightForWidth())
        self.btn_addressFile.setSizePolicy(sizePolicy)
        self.btn_addressFile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/GenericOpen32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addressFile.setIcon(icon)
        self.btn_addressFile.setObjectName("btn_addressFile")
        self.horizontalLayout_4.addWidget(self.btn_addressFile)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_addRow = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_addRow.sizePolicy().hasHeightForWidth())
        self.btn_addRow.setSizePolicy(sizePolicy)
        self.btn_addRow.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_addRow.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_addRow.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/GenericBlackAdd32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_addRow.setIcon(icon1)
        self.btn_addRow.setIconSize(QtCore.QSize(32, 32))
        self.btn_addRow.setObjectName("btn_addRow")
        self.gridLayout.addWidget(self.btn_addRow, 0, 1, 1, 1)
        self.tbl_address = QtWidgets.QTableView(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_address.sizePolicy().hasHeightForWidth())
        self.tbl_address.setSizePolicy(sizePolicy)
        self.tbl_address.setObjectName("tbl_address")
        self.gridLayout.addWidget(self.tbl_address, 0, 0, 3, 1)
        self.btn_removeRow = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_removeRow.sizePolicy().hasHeightForWidth())
        self.btn_removeRow.setSizePolicy(sizePolicy)
        self.btn_removeRow.setMinimumSize(QtCore.QSize(32, 32))
        self.btn_removeRow.setMaximumSize(QtCore.QSize(32, 32))
        self.btn_removeRow.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/GenericBlackSubtract32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_removeRow.setIcon(icon2)
        self.btn_removeRow.setIconSize(QtCore.QSize(32, 32))
        self.btn_removeRow.setObjectName("btn_removeRow")
        self.gridLayout.addWidget(self.btn_removeRow, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.txt_infoPath = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.txt_infoPath.setFont(font)
        self.txt_infoPath.setObjectName("txt_infoPath")
        self.horizontalLayout_5.addWidget(self.txt_infoPath)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.btn_infoDialog = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_infoDialog.sizePolicy().hasHeightForWidth())
        self.btn_infoDialog.setSizePolicy(sizePolicy)
        self.btn_infoDialog.setText("")
        self.btn_infoDialog.setIcon(icon)
        self.btn_infoDialog.setIconSize(QtCore.QSize(20, 20))
        self.btn_infoDialog.setObjectName("btn_infoDialog")
        self.horizontalLayout_5.addWidget(self.btn_infoDialog)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_3.addWidget(self.label_22)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.txt_imageFolderPath = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.txt_imageFolderPath.setFont(font)
        self.txt_imageFolderPath.setObjectName("txt_imageFolderPath")
        self.horizontalLayout_6.addWidget(self.txt_imageFolderPath)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.btn_tilesDialog = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tilesDialog.sizePolicy().hasHeightForWidth())
        self.btn_tilesDialog.setSizePolicy(sizePolicy)
        self.btn_tilesDialog.setText("")
        self.btn_tilesDialog.setIcon(icon)
        self.btn_tilesDialog.setIconSize(QtCore.QSize(20, 20))
        self.btn_tilesDialog.setObjectName("btn_tilesDialog")
        self.horizontalLayout_6.addWidget(self.btn_tilesDialog)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_10.addWidget(self.label_23)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.cmb_level = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_level.sizePolicy().hasHeightForWidth())
        self.cmb_level.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.cmb_level.setFont(font)
        self.cmb_level.setObjectName("cmb_level")
        self.horizontalLayout_10.addWidget(self.cmb_level)
        spacerItem4 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.txt_originX = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_originX.sizePolicy().hasHeightForWidth())
        self.txt_originX.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.txt_originX.setFont(font)
        self.txt_originX.setObjectName("txt_originX")
        self.horizontalLayout_12.addWidget(self.txt_originX)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_12.addWidget(self.label_20)
        self.txt_originY = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_originY.sizePolicy().hasHeightForWidth())
        self.txt_originY.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.txt_originY.setFont(font)
        self.txt_originY.setObjectName("txt_originY")
        self.horizontalLayout_12.addWidget(self.txt_originY)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_8.addWidget(self.label_26)
        spacerItem7 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.txt_ymax = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ymax.sizePolicy().hasHeightForWidth())
        self.txt_ymax.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.txt_ymax.setFont(font)
        self.txt_ymax.setReadOnly(False)
        self.txt_ymax.setObjectName("txt_ymax")
        self.horizontalLayout_8.addWidget(self.txt_ymax)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_25 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_2.addWidget(self.label_25)
        spacerItem9 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.txt_xmin = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_xmin.sizePolicy().hasHeightForWidth())
        self.txt_xmin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.txt_xmin.setFont(font)
        self.txt_xmin.setObjectName("txt_xmin")
        self.horizontalLayout_2.addWidget(self.txt_xmin)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem10)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout.addWidget(self.label_24)
        spacerItem11 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.txt_xmax = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_xmax.sizePolicy().hasHeightForWidth())
        self.txt_xmax.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.txt_xmax.setFont(font)
        self.txt_xmax.setObjectName("txt_xmax")
        self.horizontalLayout.addWidget(self.txt_xmax)
        self.horizontalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_3.addWidget(self.label_27)
        spacerItem13 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.txt_ymin = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ymin.sizePolicy().hasHeightForWidth())
        self.txt_ymin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.txt_ymin.setFont(font)
        self.txt_ymin.setObjectName("txt_ymin")
        self.horizontalLayout_3.addWidget(self.txt_ymin)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_11.addWidget(self.label_28)
        self.txt_resolution = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_resolution.sizePolicy().hasHeightForWidth())
        self.txt_resolution.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.txt_resolution.setFont(font)
        self.txt_resolution.setObjectName("txt_resolution")
        self.horizontalLayout_11.addWidget(self.txt_resolution)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.label_29 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_11.addWidget(self.label_29)
        self.txt_tilesize = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_tilesize.sizePolicy().hasHeightForWidth())
        self.txt_tilesize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.txt_tilesize.setFont(font)
        self.txt_tilesize.setObjectName("txt_tilesize")
        self.horizontalLayout_11.addWidget(self.txt_tilesize)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem16)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scrollArea)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_6.addWidget(self.buttonBox)
        self.txt_log = QtWidgets.QPlainTextEdit(self.splitter)
        self.txt_log.setObjectName("txt_log")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.rbtn_onlyHandle.setText(_translate("Dialog", "仅预处理"))
        self.rbtn_spiderAndHandle.setText(_translate("Dialog", "既抓取又预处理"))
        self.rbtn_onlySpider.setText(_translate("Dialog", "仅抓取"))
        self.label_1.setText(_translate("Dialog", "加载影像服务地址文件"))
        self.label_2.setText(_translate("Dialog", "离线的瓦片信息json文件"))
        self.label_22.setText(_translate("Dialog", "瓦片文件夹"))
        self.label_23.setText(_translate("Dialog", "瓦片等级:"))
        self.label_19.setText(_translate("Dialog", "初始x坐标:"))
        self.label_20.setText(_translate("Dialog", "初始y坐标:"))
        self.label.setText(_translate("Dialog", "获取坐标范围"))
        self.label_26.setText(_translate("Dialog", "ymax:"))
        self.label_25.setText(_translate("Dialog", "xmin:"))
        self.label_24.setText(_translate("Dialog", "xmax:"))
        self.label_27.setText(_translate("Dialog", "ymin:"))
        self.label_28.setText(_translate("Dialog", "分辨率:"))
        self.label_29.setText(_translate("Dialog", "瓦片尺寸:"))
from widgets.CollapsibleSplitter import CollapsibleSplitter
import icons_rc
