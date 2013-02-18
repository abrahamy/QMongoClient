__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

__all__ = ["QMongoClient",]

from PySide import QtCore, QtGui

from views.ui.ui_qmongoclient import Ui_QMongoClient
from views.connectionmanagerdlg import ConnectionManager

class QMongoClient(QtGui.QMainWindow, Ui_QMongoClient):

    def __init__(self, parent=None):
        super(QMongoClient, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)

    @QtCore.Slot(result=None)
    def on_actionFileConnect_activated(self):
        dialogResult = ConnectionManager(self).exec_()

    @QtCore.Slot(result=None)
    def on_actionServerOverview_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionServerAddDatabase_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionServerDisconnect_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionServerStatus_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBOverview_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBProfilingLevel_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBAddCollection_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBAddStoredJavaScript_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBImportFromMySQL_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBImportFromMicrosoftSQLServer_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBImportFromPostgreSQL_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBCopyCollectionsToDifferentServer_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBDrop_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionDBStats_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionView_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionFind_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionFind2_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionUpdate_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionGroup_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionMapReduce_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionRemove_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionInsertDocument_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionAddIndex_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionCompact_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionDuplicate_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionCopyToDifferentServer_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionRemoveAll_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionDrop_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionCollectionStats_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionIndexDrop_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionIndexProperties_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionJavaScriptEdit_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionJavaScriptDrop_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionToolsServerMonitoring_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionToolsPreferences_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionWindowsClose_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionWindowsCloseAll_triggered(self):
        pass

    @QtCore.Slot(result=None)
    def on_actionHelpAbout_triggered(self):
        pass
