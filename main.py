__author__ = 'Abraham Aondowase Yusuf <bb6xt@yahoo.com>'

__all__ = ["QMongoClientApplication",]

import sys

from PySide import QtGui
import qmongoclient

class QMongoClientApplication(QtGui.QApplication):

    def __init__(self):
        super(QMongoClientApplication, self).__init__(sys.argv)
        self.setOrganizationName("BB6XT Inc")

        qMongoClient = qmongoclient.QMongoClient()
        qMongoClient.show()

        self.exec_()

if __name__ == '__main__':
    QMongoClientApplication()