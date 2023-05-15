# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ASL-Display.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

#from capstone_speech_to_text_copy2 import google_api
#import capstone_speech_to_text_copy2 as caps
#from certifi.__main__ import args


class Ui_Dialog(object):
    def __init__(self, text):
        self.text = text

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
       # Dialog.resize(878, 314)
        Dialog.resize(900, 400)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        Dialog.setLayout(QtWidgets.QVBoxLayout())  # Use a QVBoxLayout as the layout for the Dialog
        Dialog.layout().addWidget(self.centralwidget)  # Add the central widget to the layout
        #self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_1 = QtWidgets.QLabel(Dialog)
        #self.label_1.setGeometry(QtCore.QRect(50, 50, 281, 391))
        self.label_1.setGeometry(QtCore.QRect(20, 20, 180, 280)) #20,20,141,261
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Dialog)
        #self.label_2.setGeometry(QtCore.QRect(200, 50, 200, 200))
        self.label_2.setGeometry(QtCore.QRect(180, 20, 180, 280)) #180,20,141,261
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        #self.label_3.setGeometry(QtCore.QRect(200, 50, 200, 200))
        self.label_3.setGeometry(QtCore.QRect(360, 20, 180, 280)) #360, 20, 141, 261
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        #self.label_4.setGeometry(QtCore.QRect(200, 250, 200, 200))
        self.label_4.setGeometry(QtCore.QRect(530, 20, 180, 280)) #530, 20, 141, 261
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        #self.label_5.setGeometry(QtCore.QRect(200, 250, 200, 200))
        self.label_5.setGeometry(QtCore.QRect(710, 20, 180, 280)) #710, 20, 141, 261
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        """# **Number 0-9 links**"""

        one = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0160.png"
        two = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0165.png"
        three = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0170.png"
        four = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0175.png"
        five = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0180.png"
        six = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0185.png"
        seven = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0190.png"
        eight = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0195.png"
        nine = "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0200.png"

        alphabet = {
            'a': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0010.png",
            'b': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0020.png",
            'c': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0031.png",
            'd': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0040.png",
            'e': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0045.png",
            'f': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0050.png",
            'g': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0055.png",
            'h': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0060.png",
            'i': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0065.png",
            'j': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0070.png",
            'k': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0080.png",
            'l': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0085.png",
            'm': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0090.png",
            'n': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0095.png",
            'o': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0100.png",
            'p': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0105.png",
            'q': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0110.png",
            'r': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0115.png",
            's': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0120.png",
            't': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0125.png",
            'u': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0130.png",
            'v': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0135.png",
            'w': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0140.png",
            'x': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0145.png",
            'y': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0150.png",
            'z': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0155.png"
        }
        numbers ={'one': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0160.png",
                  'two': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0165.png",
                  'three': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0170.png",
                  'four': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0175.png",
                  'five': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0180.png",
                  'six': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0185.png",
                  'seven': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0190.png",
                  'eight': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0195.png",
                  'nine': "/Users/enocgonzalez/Desktop/asl-app/Renders/ASLChFrame_0200.png"
                  }

        word = self.text
        word = word.lower()

        for i, letter in enumerate(word):
            if i >= 5:
                break
            if letter in alphabet:
                pixmap = QtGui.QPixmap(alphabet[letter])
                label = getattr(self, f"label_{i + 1}")
                label.setPixmap(pixmap)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_1.setText(_translate("Dialog", "TextLabel"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "TextLabel"))
        self.label_5.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
