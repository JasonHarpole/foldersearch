from PyQt4 import QtCore, QtGui
import sys
import os
from os.path import expanduser

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


class Folder_Find(object):
    def file_read(self, fname, searchfor):
        matchlist = []
        searchfor = str(searchfor)
        with open(fname) as f:
            content_list = f.readlines()
            matching = [s for s in content_list if searchfor in s]
            filename = ""
            if matching:
                print(fname)
                print matching
                a = Ui_FolderSearch()
                FolderSearch = QtGui.QDialog()
                ui = Ui_FolderSearch()
                filename = '''"<font size=" 3" color="red">"''' + fname + '''"</font>"'''
                matchlist.append("<br/>")
                matchlist.append(filename)
                matchlist.append(matching)
                matchlist.append("<br/>")
        resultsstr = ''.join(str(e) for e in matchlist)
        return resultsstr

    def search(fname, searchfor):
        startingDir = 'C:'
        dialog = QtGui.QFileDialog()
        dialog.setFileMode(QtGui.QFileDialog.FileMode())
        foldername = dialog.getExistingDirectory(None, 'Open working directory',
                                                 startingDir)
        print foldername
        results = ""
        resultslist = []
        for fname in os.listdir(foldername):
            if os.path.isfile(fname):
                instance = Folder_Find()
                results = str(instance.file_read(fname, searchfor))
                resultslist.append(results)

        resultsstr = ''.join(str(e) for e in resultslist)
        return(resultsstr)


class Ui_FolderSearch(object):

    def setupUi(self, FolderSearch):
        FolderSearch.setObjectName(_fromUtf8("FolderSearch"))
        FolderSearch.resize(544, 528)
        self.FolderDialog = QtGui.QPushButton(FolderSearch)
        self.FolderDialog.setGeometry(QtCore.QRect(360, 20, 75, 23))
        self.FolderDialog.setObjectName(_fromUtf8("FolderDialog"))
        self.Cancelbutton = QtGui.QPushButton(FolderSearch)
        self.Cancelbutton.setGeometry(QtCore.QRect(450, 20, 75, 23))
        self.Cancelbutton.setObjectName(_fromUtf8("Cancelbutton"))
        self.textBrowser = QtGui.QTextBrowser(FolderSearch)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 521, 461))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.lineEdit = QtGui.QLineEdit(FolderSearch)
        self.lineEdit.setGeometry(QtCore.QRect(150, 20, 191, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.FolderDialog.raise_()
        self.Cancelbutton.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(FolderSearch)
        QtCore.QMetaObject.connectSlotsByName(FolderSearch)

    def retranslateUi(self, FolderSearch):
        FolderSearch.setWindowTitle(_translate("FolderSearch", "Folder Search", None))
        self.FolderDialog.setText(_translate("FolderSearch", "Folder Search", None))
        self.Cancelbutton.setText(_translate("FolderSearch", "Cancel", None))

        def wrapper():
            sys.exit()

        def wrapper2():
            searchfor = self.lineEdit.text()
            print dir(self)
            b = Folder_Find()
            results = str(b.search(searchfor))
            self.textBrowser.insertHtml(results)
        self.Cancelbutton.clicked.connect(wrapper)
        self.FolderDialog.clicked.connect(wrapper2)


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    FolderSearch = QtGui.QDialog()
    ui = Ui_FolderSearch()
    ui.setupUi(FolderSearch)
    FolderSearch.show()
    sys.exit(app.exec_())


