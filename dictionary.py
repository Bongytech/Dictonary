import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def find(inp):
    with open(resource_path("dictionary.arc"), "r+") as file:
        fil = file.read()
        dictionary = fil.split("\n")
        num = 0
        for word in dictionary:
            dic = word.replace('"', "")
            first_word = dic.split(" ")[0]
            inp = inp.strip("")
            if inp.lower() == first_word.lower().strip():
                print(first_word)
                num += 1
                answer = dic.replace("n.", "noun ")
                answer = answer.replace("v.", "verb")
                answer = answer.replace("adv.", "adverb")
                answer = answer.replace("pl.", "plural")
                answer = answer.replace("prep.", "preposition")
                answer = answer.title()
                return answer.replace(".", "\n")

class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(467, 520)
        App.setStyleSheet("#App {\n""    background-color: rgb(61, 56, 70);\n""}")

        self.input = QLineEdit(App)
        self.input.setGeometry(QRect(10, 10, 251, 31))
        self.input.setStyleSheet("#input {\n""    background-color: rgb(36, 31, 49);\n""    color: rgb(255, 255, 255);\n""}\n""")
        self.input.setPlaceholderText("")
        self.input.setObjectName("input")

        self.search = QPushButton(App)
        self.search.setGeometry(QRect(260, 10, 101, 31))
        self.search.setStyleSheet("#search {\n""    background-color: rgb(36, 31, 49);\n""    color: white;\n""}")
        self.search.clicked.connect(self.writ)
        self.search.setObjectName("search")
        
        self.output = QTextEdit(App)
        self.output.setGeometry(QRect(0, 50, 461, 461))
        self.output.setStyleSheet("#output {\n""    background-color: rgb(36, 31, 49);\n""    color: white;\n""}\n""")
        self.output.setReadOnly(True)
        self.output.setObjectName("output")

#        self.speak = QPushButton(App)
#        self.speak.setGeometry(QRect(400, 50, 61, 31))
#        self.speak.setStyleSheet("#speak {\n""    background-color: rgb(36, 31, 49);\n""    color: white;\n""}")
#        self.speak.setObjectName("speak")
#        self.speak.clicked.connect(self.sp)


        self.retranslateUi(App)
        QMetaObject.connectSlotsByName(App)

    def writ(self):
        word = self.input.text()
        diction = find(word).__str__()
        if diction != "None":
            self.output.setFontPointSize(9.0)
            self.output.setText(diction.replace('"', "\n\n").replace('.', "\n\n"))
        else:
            self.output.setText("********************")
            self.output.setText("Cannot find word....")

    def sp(self):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        word = self.output.toPlainText() 
        engine.say(word)
        engine.runAndWait()

    def retranslateUi(self, App):
        _translate = QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Dialog"))
        self.search.setText(_translate("App", "search"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_App()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
