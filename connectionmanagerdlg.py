__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

__all__ = ["ConnectionManager",]

from PySide import QtCore, QtGui

from ui.ui_connectionmanagerdlg import Ui_ConnectionManagerDlg
from newconnection import NewConnection

class ConnectionManager(QtGui.QDialog, Ui_ConnectionManagerDlg):

    def __init__(self, parent=None):
        super(ConnectionManager, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    @QtCore.Slot(result=None)
    def on_pushButtonAddConnection_clicked(self):
        dialogResult = NewConnection(self).exec_()

    @QtCore.Slot(result=None)
    def on_pushButtonRemoveConnection_clicked(self):
        pass

    @QtCore.Slot(result=None)
    def on_pushButtonModifyConnection_clicked(self):
        pass

    @QtCore.Slot(result=None)
    def on_pushButtonConnect_clicked(self):
        pass
