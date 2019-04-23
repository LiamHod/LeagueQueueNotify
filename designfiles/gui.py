# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LQNdesign.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 295)
        Form.setMinimumSize(QtCore.QSize(300, 295))
        Form.setMaximumSize(QtCore.QSize(300, 295))
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 281, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.template_img_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.template_img_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.template_img_label.setFont(font)
        self.template_img_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.template_img_label.setObjectName("template_img_label")
        self.horizontalLayout_4.addWidget(self.template_img_label)
        self.template_img_hover = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.template_img_hover.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.template_img_hover.setFont(font)
        self.template_img_hover.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.template_img_hover.setObjectName("template_img_hover")
        self.horizontalLayout_4.addWidget(self.template_img_hover)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.template_combo = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.template_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.template_combo.setObjectName("template_combo")
        self.verticalLayout_2.addWidget(self.template_combo)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.template_path_name = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.template_path_name.setReadOnly(True)
        self.template_path_name.setObjectName("template_path_name")
        self.horizontalLayout_2.addWidget(self.template_path_name)
        self.template_file_chooser = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.template_file_chooser.setFont(font)
        self.template_file_chooser.setObjectName("template_file_chooser")
        self.horizontalLayout_2.addWidget(self.template_file_chooser)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 140, 281, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.threshold_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.threshold_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.threshold_label.setFont(font)
        self.threshold_label.setObjectName("threshold_label")
        self.horizontalLayout_5.addWidget(self.threshold_label)
        self.threshhold_hover = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.threshhold_hover.setFont(font)
        self.threshhold_hover.setObjectName("threshhold_hover")
        self.horizontalLayout_5.addWidget(self.threshhold_hover)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.threshhold_combo = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.threshhold_combo.setObjectName("threshhold_combo")
        self.verticalLayout_3.addWidget(self.threshhold_combo)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(-23, 120, 341, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(-23, 220, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(129, 260, 161, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ok_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.ok_button.setMaximumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.ok_button.setFont(font)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout_6.addWidget(self.ok_button)
        self.cancel_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.cancel_button.setMaximumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.cancel_button.setFont(font)
        self.cancel_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cancel_button.setCheckable(False)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_6.addWidget(self.cancel_button)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 260, 81, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.defaults_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.defaults_button.setMaximumSize(QtCore.QSize(75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.defaults_button.setFont(font)
        self.defaults_button.setObjectName("defaults_button")
        self.horizontalLayout_7.addWidget(self.defaults_button)

        # self.tray_icon = QtWidgets.QSystemTrayIcon(Form)
        # self.tray_icon.setIcon(QtGui.QIcon('icons/sync.ico'))
        # show_action = QtWidgets.QAction("Show", Form)
        # quit_action = QtWidgets.QAction("Exit", Form)
        # hide_action = QtWidgets.QAction("Hide", Form)
        # show_action.triggered.connect(Form.show)
        # hide_action.triggered.connect(Form.hide)
        # quit_action.triggered.connect(QtWidgets.qApp.quit)
        # tray_menu = QtWidgets.QMenu()
        # tray_menu.addAction(show_action)
        # tray_menu.addAction(hide_action)
        # tray_menu.addAction(quit_action)
        # self.tray_icon.setContextMenu(tray_menu)
        # self.tray_icon.show()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.template_combo, self.template_path_name)
        Form.setTabOrder(self.template_path_name, self.template_file_chooser)
        Form.setTabOrder(self.template_file_chooser, self.threshhold_combo)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LQN Settings"))
        self.template_img_label.setText(_translate("Form", "Template Image Type"))
        self.template_img_hover.setToolTip(_translate("Form", "This is the image used to compare with League of Legends client, choose the proper type based on current event"))
        self.template_img_hover.setText(_translate("Form", "(?)"))
        self.template_file_chooser.setText(_translate("Form", "Choose File"))
        self.threshold_label.setText(_translate("Form", "Queue Detection Threshold"))
        self.threshhold_hover.setToolTip(_translate("Form", "This is the value used to detect the queue pop, if program is having problems detecting League queue lower this value. If the program is detecting thing that are not the queue raise this value"))
        self.threshhold_hover.setText(_translate("Form", "(?)"))
        self.ok_button.setText(_translate("Form", "OK"))
        self.cancel_button.setText(_translate("Form", "Cancel"))
        self.defaults_button.setText(_translate("Form", "Defaults"))

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtWidgets.QMenu(parent)
        settings_action = self.menu.addAction("Settings")
        exit_action = self.menu.addAction("Exit")
        exit_action.triggered.connect(QtWidgets.qApp.quit)
        settings_action.triggered.connect(self.handleSettings)
        self.setContextMenu(self.menu)

    def handleSettings(self):
        self.window = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(self.window)
        self.window.show()


def handleSettings():
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()


def runGui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    # Form = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon('icons/sync.ico'))
    # ui.setupUi(Form)
    trayIcon.show()
    # Form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())