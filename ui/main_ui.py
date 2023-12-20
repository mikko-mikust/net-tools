# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerLSyMSt.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 700)
        f = QFont()
        f.setPointSize(11)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.b64_but = QPushButton(self.centralwidget)
        self.b64_but.setObjectName(u"b64_but")
        self.gridLayout_2.addWidget(self.b64_but, 0, 1, 1, 1)

        self.hash_but = QPushButton(self.centralwidget)
        self.hash_but.setObjectName('hash_but')
        self.gridLayout_2.addWidget(self.hash_but, 0, 3, 1, 1)

        self.port_ui_w = QWidget(MainWindow)
        self.port_ui = QGridLayout(self.port_ui_w)
        self.port_ui.setObjectName(u"port_ui")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.port_ui.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setEnabled(True)

        self.port_ui.addWidget(self.textBrowser, 2, 1, 1, 1)

        # self.gridLayout_2.addLayout(self.port_ui_w)
        self.gridLayout_2.addWidget(self.port_ui_w, 1, 0, 1, 4)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.port_but = QPushButton(self.centralwidget)
        self.port_but.setObjectName(u"port_but")
        self.gridLayout_2.addWidget(self.port_but, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 754, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.b64_ui_w = QWidget(MainWindow)
        self.b64_ui_layout = QGridLayout(self.b64_ui_w)
        self.b64_ui_layout.setObjectName(u"b64_ui_layout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.b64_ui_layout.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.b64_ui_layout.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.b64_ui_layout.addItem(self.horizontalSpacer_4, 1, 6, 1, 1)

        self.b64_dec_but = QPushButton(self.centralwidget)
        self.b64_dec_but.setObjectName(u"b64_dec_but")

        self.b64_ui_layout.addWidget(self.b64_dec_but, 1, 1, 1, 1)

        self.b64_swap_but = QPushButton(self.centralwidget)
        self.b64_swap_but.setObjectName(u"b64_swap_but")

        self.b64_ui_layout.addWidget(self.b64_swap_but, 1, 5, 1, 1)

        self.b64dec = QTextEdit(self.centralwidget)
        self.b64dec.setObjectName(u"b64dec")

        self.b64_ui_layout.addWidget(self.b64dec, 2, 0, 1, 7)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.b64_ui_layout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.b64_enc_but = QPushButton(self.centralwidget)
        self.b64_enc_but.setObjectName(u"b64_enc_but")

        self.b64_ui_layout.addWidget(self.b64_enc_but, 1, 3, 1, 1)

        self.b64src = QTextEdit(self.centralwidget)
        self.b64src.setObjectName(u"b64src")
        self.b64src.setFont(f)
        self.b64dec.setFont(f)
        self.b64_ui_layout.addWidget(self.b64src, 0, 0, 1, 7)

        self.gridLayout_2.addWidget(self.b64_ui_w, 1, 0, 1, 4)

        self.scan_for_ip = QWidget(self.centralwidget)
        self.scan_for_ip.setObjectName(u"scan_for_ip")
        self.gridLayout = QGridLayout(self.scan_for_ip)
        self.gridLayout.setObjectName(u"gridLayout")
        self.min_ip = QLineEdit(self.scan_for_ip)
        self.min_ip.setObjectName(u"min_ip")

        self.gridLayout.addWidget(self.min_ip, 0, 1, 1, 1)

        self.label_4 = QLabel(self.scan_for_ip)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.max_ip = QLineEdit(self.scan_for_ip)
        self.max_ip.setObjectName(u"max_ip")

        self.gridLayout.addWidget(self.max_ip, 0, 3, 1, 1)

        self.label_5 = QLabel(self.scan_for_ip)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.sc_ip = QPushButton(self.scan_for_ip)
        self.sc_ip.setObjectName(u"sc_ip")

        self.gridLayout.addWidget(self.sc_ip, 0, 4, 1, 1)

        self.ip_res = QTextBrowser(self.scan_for_ip)
        self.ip_res.setObjectName(u"ip_res")

        self.gridLayout.addWidget(self.ip_res, 1, 0, 1, 5)

        self.gridLayout_2.addWidget(self.scan_for_ip, 1, 0, 1, 4)

        self.hash_w = QWidget(self.centralwidget)
        self.hash_w.setObjectName(u"hash_w")
        self.gridLayout = QGridLayout(self.hash_w)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hash_file_path = QLineEdit(self.hash_w)
        self.hash_file_path.setObjectName(u"hash_file_path")

        self.gridLayout.addWidget(self.hash_file_path, 1, 0, 1, 1)

        self.hash_chose_file = QPushButton(self.hash_w)
        self.hash_chose_file.setObjectName(u"hash_chose_file")

        self.gridLayout.addWidget(self.hash_chose_file, 1, 1, 1, 1)

        self.hash_start = QPushButton(self.hash_w)
        self.hash_start.setObjectName(u"hash_start")

        self.gridLayout.addWidget(self.hash_start, 1, 2, 1, 1)

        self.hash_res_view = QTextBrowser(self.hash_w)
        self.hash_res_view.setObjectName(u"hash_res_view")
        self.hash_res_view.setFont(f)
        self.gridLayout.addWidget(self.hash_res_view, 2, 0, 1, 3)

        self.gridLayout_2.addWidget(self.hash_w, 2, 0, 1, 4)

        self.retranslateUi(MainWindow)
        # self.port_ui_w.hide()
        self.b64_ui_w.hide()
        self.scan_for_ip.hide()
        self.hash_w.hide()
        self.hash_w.setAcceptDrops(True)
        self.textBrowser.setFont(f)
        self.hash_w.dragEnterEvent = dragEnterEvent
        QMetaObject.connectSlotsByName(MainWindow)
        self.ip_res.setFont(f)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tools(rubbish)", None))
        self.b64_but.setText(QCoreApplication.translate("MainWindow", u"base64", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ip:", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"开始端口", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.b64_dec_but.setToolTip(QCoreApplication.translate("MainWindow",
                                                               "将下方文本框内容解码base64并写入上方文本框",
                                                               None))
        self.b64_swap_but.setToolTip(QCoreApplication.translate("MainWindow", '交换两个文本框内容', None))
        self.b64_enc_but.setToolTip(QCoreApplication.translate("MainWindow",
                                                               u"将上方文本框内容编码base64并写入下方文本框",
                                                               None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"结束端口", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"1024", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"开始检测", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ip段扫描", None))
        self.port_but.setText(QCoreApplication.translate("MainWindow", u"端口扫描", None))
        self.b64_dec_but.setText(QCoreApplication.translate("MainWindow", u"base64解码", None))
        self.hash_but.setText(QCoreApplication.translate("MainWindow", u"文件哈希", None))
        self.b64_swap_but.setText(QCoreApplication.translate("MainWindow", u"交换", None))
        self.b64_enc_but.setText(QCoreApplication.translate("MainWindow", u"base64编码", None))
        self.min_ip.setText(QCoreApplication.translate("MainWindow", u"192.168.1.1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"结束ip", None))
        self.max_ip.setText(QCoreApplication.translate("MainWindow", u"192.168.1.254", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"开始ip", None))
        self.sc_ip.setText(QCoreApplication.translate("MainWindow", u"开始扫描", None))
        self.hash_chose_file.setText(QCoreApplication.translate("MainWindow", u"选择文件", None))
        self.hash_start.setText(QCoreApplication.translate("MainWindow", u"计算", None))

    # retranslateUi


def dragEnterEvent(e) -> None:
    if e.mimeData().hasUrls():
        e.accept()
    else:
        e.ignore()

# def dro
