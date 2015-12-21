# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import time
import lol
import json
import webbrowser
import os

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(462, 253)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.idInput = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idInput.sizePolicy().hasHeightForWidth())
        self.idInput.setSizePolicy(sizePolicy)
        self.idInput.setObjectName(_fromUtf8("idInput"))
        self.horizontalLayout.addWidget(self.idInput)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.pwInput = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwInput.sizePolicy().hasHeightForWidth())
        self.pwInput.setSizePolicy(sizePolicy)
        self.pwInput.setObjectName(_fromUtf8("pwInput"))
        self.horizontalLayout_2.addWidget(self.pwInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(u'2015년도엔 롤을 얼마나 했을까')
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">사용법</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">롤에 접속할때 사용하는 아이디와 비밀번호를 입력한 후</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">로그인 버튼을 누르면 잠시후 브라우져에 결과창이 뜹니다</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">------</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">해킹당할까봐 무서우신분들은 여기(http://링크) 에서</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">소스파일을 다운받을수 있으니 주변 컴공과학생에게</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">체크해달라고 말해보세요</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">------</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. 완료! 표시가 떳는데 반응이없으면 폴더에있는 result.html을 더블클릭하세요.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. 전적은 최대 2000개까지 가져옵니다.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. 전적을 얻어오는 방식으로 비공식적인 방법을 사용하고있어서 어느날 갑자기 작동이 안될수도 있습니다.</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "상태메세지", None))
        self.label_2.setText(_translate("MainWindow", "id  ", None))
        self.label_3.setText(_translate("MainWindow", "pw", None))
        self.pushButton.setText(_translate("MainWindow", "로그인", None))
        self.label.setText(_translate("MainWindow", "제작자: anch0vy", None))

    def myInit(self):
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.login)
        self.pwInput.setEchoMode(QtGui.QLineEdit.Password)


    def setStatusLabel(self,msg):
        self.label_4.setText(msg)

    def login(self):
        id = self.idInput.text()
        pw = self.pwInput.text()
        id = str(id)
        pw = str(pw)
        if not all([id,pw]):
            self.label_4.setText(u"아이디, 또는 비밀번호가 공란입니다.")
            return
        else:
            self.thread = loginThread(id, pw)
            self.thread.signalChangeStatusLabel.connect(self.setStatusLabel)
            self.thread.start()


class loginThread(QtCore.QThread):
    signalChangeStatusLabel = QtCore.pyqtSignal(str)
    def __init__(self, id, pw):
        QtCore.QThread.__init__(self)
        self.id = id
        self.pw = pw

    def run(self):
        self.signalChangeStatusLabel.emit(u'데이터 받아오는중...(좀 오래걸림)')
        games = lol.getHistory(self.id, self.pw)
        if games is None:
            self.signalChangeStatusLabel.emit(u'로그인에 실패했습니다')
            return
        self.signalChangeStatusLabel.emit(u'데이터 분석중...')
        countdic = {}
        playtime = 0
        for game in games:
            timestamp = game['gameCreation']/1000
            if timestamp > 1420070400: #2015
                countdic[str(timestamp)] = 1
                playtime += game['gameDuration']

        baseHTML = open('base.html').read()
        sec = playtime
        min = sec / 60
        hour = min / 60
        day = hour / 24
        sec %= 60
        min %= 60
        hour %= 24
        baseHTML = baseHTML.replace('%countdic%', json.dumps(countdic))
        baseHTML = baseHTML.replace('%day%', str(day))
        baseHTML = baseHTML.replace('%hour%', str(hour))
        baseHTML = baseHTML.replace('%min%', str(min))
        baseHTML = baseHTML.replace('%sec%', str(sec))
        savePath = '%s_result.html' % self.id
        open(savePath,'w').write(baseHTML)
        path = os.path.abspath(savePath)
        self.signalChangeStatusLabel.emit(u'완료!')
        url = 'file://%s'%path
        webbrowser.open(url)





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.myInit()
    MainWindow.show()
    sys.exit(app.exec_())

