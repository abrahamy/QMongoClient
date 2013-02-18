__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

__all__ = ["ConnectionManager",]

from PySide import QtCore, QtGui

from views.ui.ui_connectionmanagerdlg import Ui_ConnectionManagerDlg
from views.newconnection import NewConnection
from models import config

class ConnectionManager(QtGui.QDialog, Ui_ConnectionManagerDlg):

    def __init__(self, parent=None):
        super(ConnectionManager, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

        self.update_listView()

    @QtCore.Slot(result=None)
    def on_pushButtonAddConnection_clicked(self):
        dialogResult = NewConnection(self).exec_()

        if dialogResult == QtGui.QDialog.DialogCode.Accepted:
            self.update_listView()

    @QtCore.Slot(result=None)
    def on_pushButtonRemoveConnection_clicked(self):
        pass

    @QtCore.Slot(result=None)
    def on_pushButtonModifyConnection_clicked(self):
        pass

    @QtCore.Slot(result=None)
    def on_pushButtonConnect_clicked(self):
        pass

    def update_listView(self):
        cnames = config.ConnectionStore().names
        if cnames:
            model = QtGui.QStringListModel()
            model.setStringList([i for i in cnames])
            self.listViewAvailableConnections.setModel(model)