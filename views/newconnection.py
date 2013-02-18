__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

__all__ = ["NewConnection",]

from PySide import QtCore, QtGui
from pymongo import MongoClient

from views.ui.ui_newconnectiondlg import Ui_NewConnectionDlg
from models import config

class NewConnection(QtGui.QDialog, Ui_NewConnectionDlg):

    def __init__(self, parent=None):
        super(NewConnection, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.lineEditPort.setValidator(QtGui.QIntValidator())

    @QtCore.Slot(result=None)
    def on_pushButtonOpenKeyFile_clicked(self):
        keyFile = QtGui.QFileDialog.getOpenFileName(self, QtCore.QDir().homePath())

    @QtCore.Slot(result=None)
    def on_pushButtonTestConnection_clicked(self):
        try:
            params = {'host': self.lineEditServer.text(),
                           'port': int(self.lineEditPort.text())}
            client = MongoClient(**params)
            msg = 'Successful!'
        except Exception as e:
            msg = e.message

        QtGui.QMessageBox.information(self, 'Connection Test', msg)

    @QtCore.Slot(result=None)
    def on_pushButtonSave_clicked(self):
        db_connection = config.DBConnection(self.lineEditConnectionName.text(), server=self.lineEditServer.text(),
            port=self.lineEditPort.text(),user=self.lineEditUsername.text(), passwd=self.lineEditPassword.text(),
            dbnames=self.lineEditDatabases.text().split()
        )

        config.ConnectionStore().push(db_connection)
        self.accept()

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