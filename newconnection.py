__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

__all__ = ["NewConnection",]

from PySide import QtCore, QtGui

from ui.ui_newconnectiondlg import Ui_NewConnectionDlg

class NewConnection(QtGui.QDialog, Ui_NewConnectionDlg):

    def __init__(self, parent=None):
        super(NewConnection, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    @QtCore.Slot(result=None)
    def on_pushButtonOpenKeyFile_clicked(self):
        keyFile = QtGui.QFileDialog.getOpenFileName(self, QtCore.QDir().homePath())

    @QtCore.Slot(result=None)
    def on_pushButtonTestConnection_clicked(self):
        pass

    @QtCore.Slot(result=None)
    def on_pushButtonSave_clicked(self):
        pass

    @QtCore.Slot(result=None)
    def on_lineEditConnectionName_textChanged(self):
        self.enableTestSave()

    @QtCore.Slot()
    def on_lineEditServer_textChanged(self):
        self.enableTestSave()

    def enableTestSave(self):
        if self.lineEditConnectionName.text() and self.lineEditServer.text():
            shouldEnable = True
        else:
            shouldEnable = False

        map(lambda x: x.setEnabled(shouldEnable), (self.pushButtonTestConnection, self.pushButtonSave))