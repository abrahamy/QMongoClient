from views import qmongoclient

__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

__all__ = ["QMongoClientApplication",]

import sys

from PySide import QtGui

class QMongoClientApplication(QtGui.QApplication):

    def __init__(self):
        super(QMongoClientApplication, self).__init__(sys.argv)
        self.setOrganizationName('Sleekbums Inc')
        self.setOrganizationDomain("bb6xt.herokuapp.com")
        self.setApplicationName("QMongoClient")

        client = qmongoclient.QMongoClient()
        client.show()

        self.exec_()

if __name__ == '__main__':
    QMongoClientApplication()