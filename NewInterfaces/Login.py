

from PyQt5 import QtCore, QtGui, QtWidgets
from Crud.CRUD_Usuario import CrudEmpleado

import mysql.connector

class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(956, 674)
                MainWindow.setStyleSheet("#MainWindow {\n"
        "background-image:url(../img/inicioDeSesion.png);\n"
        "background-repeat: no-repeat;\n"
        "background-size: cover;\n"
        "background-position: center;\n"
        "}")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setStyleSheet("#centralwidget{\n"
        "    text-align: center;\n"
        "}")
                self.centralwidget.setObjectName("centralwidget")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
                self.verticalLayout.setObjectName("verticalLayout")
                self.frame = QtWidgets.QFrame(self.centralwidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
                self.frame.setSizePolicy(sizePolicy)
                self.frame.setMinimumSize(QtCore.QSize(502, 600))
                self.frame.setStyleSheet("#frame{\n"
        "    padding: 80px 140px;\n"
        "    text-align: center;\n"
        "}")
                self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame.setObjectName("frame")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
                self.verticalLayout_2.setObjectName("verticalLayout_2")
                self.widget = QtWidgets.QWidget(self.frame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
                self.widget.setSizePolicy(sizePolicy)
                self.widget.setMinimumSize(QtCore.QSize(500, 0))
                self.widget.setMaximumSize(QtCore.QSize(900, 700))
                self.widget.setMouseTracking(False)
                self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
                self.widget.setStyleSheet("#widget{\n"
        "    background-color: rgb(240, 240, 240);\n"
        "    border-radius: 12px;\n"
        "}")
                self.widget.setObjectName("widget")
                self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
                self.verticalLayout_3.setSpacing(0)
                self.verticalLayout_3.setObjectName("verticalLayout_3")
                self.label_2 = QtWidgets.QLabel(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
                self.label_2.setSizePolicy(sizePolicy)
                self.label_2.setMaximumSize(QtCore.QSize(150, 150))
                self.label_2.setStyleSheet("#label_2{\n"
        "    height: 50px;\n"
        "}")
                self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
                self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
                self.label_2.setLineWidth(0)
                self.label_2.setText("")
                self.label_2.setPixmap(QtGui.QPixmap("../img/logo.ico"))
                self.label_2.setScaledContents(True)
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                self.label_2.setWordWrap(True)
                self.label_2.setObjectName("label_2")
                self.verticalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
                self.widget_2 = QtWidgets.QWidget(self.widget)
                self.widget_2.setObjectName("widget_2")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
                self.horizontalLayout.setContentsMargins(-1, 0, -1, 17)
                self.horizontalLayout.setSpacing(6)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.label = QtWidgets.QLabel(self.widget_2)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(20)
                font.setBold(True)
                font.setItalic(False)
                self.label.setFont(font)
                self.label.setStyleSheet("#label{\n"
        "    \n"
        "    font-weight: bold;\n"
        "}")
                self.label.setScaledContents(False)
                self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.label.setObjectName("label")
                self.horizontalLayout.addWidget(self.label)
                self.label_3 = QtWidgets.QLabel(self.widget_2)
                font = QtGui.QFont()
                font.setFamily("Segoe UI")
                font.setPointSize(20)
                font.setBold(False)
                font.setItalic(False)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("")
                self.label_3.setObjectName("label_3")
                self.horizontalLayout.addWidget(self.label_3)
                self.verticalLayout_3.addWidget(self.widget_2, 0, QtCore.Qt.AlignVCenter)
                self.lineEdit = QtWidgets.QLineEdit(self.widget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
                self.lineEdit.setSizePolicy(sizePolicy)
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                self.lineEdit.setFont(font)
                self.lineEdit.setStyleSheet("#lineEdit{\n"
        "    margin: 12 40 12 40;\n"
        "    padding: 8;\n"
        "    background-color: #88a6c3;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "    border-radius: 10;\n"
        "}")
                self.lineEdit.setMaxLength(12)
                self.lineEdit.setFrame(False)
                self.lineEdit.setObjectName("lineEdit")
                self.verticalLayout_3.addWidget(self.lineEdit)
                self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                self.lineEdit_2.setFont(font)
                self.lineEdit_2.setStyleSheet("#lineEdit_2{\n"
        "    margin: 5 40 5 40;\n"
        "    padding: 8;\n"
        "    background-color: #88a6c3;\n"
        "    color: white;\n"
        "    font-weight: bold;\n"
        "    border-radius: 10;\n"
        "}")
                self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.verticalLayout_3.addWidget(self.lineEdit_2)
                self.pushButton = QtWidgets.QPushButton(self.widget)
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                self.pushButton.setFont(font)
                self.pushButton.setStyleSheet("#pushButton{\n"
        "    margin: 12 120 12 120;\n"
        "    padding: 8 10 8 10;\n"
        "    color: white;\n"
        "    background-color: #185791;\n"
        "    font-weight: bold;\n"
        "}")
                self.pushButton.setObjectName("pushButton")
                self.verticalLayout_3.addWidget(self.pushButton)
                self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.verticalLayout.addWidget(self.frame)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 956, 22))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)

                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.label.setText(_translate("MainWindow", "Login"))
                self.label_3.setText(_translate("MainWindow", "User"))
                self.lineEdit.setPlaceholderText(_translate("MainWindow", "Teléfono"))
                self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Contraseña"))
                self.pushButton.setText(_translate("MainWindow", "Iniciar sesión"))

        def __iniciar_sesion(self):
                connection = mysql.connector.connect(
                        user="u119126_pollos2LaVengazaDelPollo",
                        host="174.136.28.78",
                        port="3306",
                        password="$ShotGunKin0805",
                        database="u119126_pollos2LaVengazaDelPollo"
                )



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
