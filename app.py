import sys
from PyQt5 import QtWidgets, uic
import random 
import clipboard
import string 

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('app.ui', self)
        self.handle_buttons()
        self.show()

    def generate_password(self):

        password = []
        length = self.get_length()

        upper_case = string.ascii_uppercase # use to store uper case alphabets e.g 'A','B','C'...
        lower_case = string.ascii_lowercase # use to store lower case alphabets e.g 'a','b','c'...
        digit = string.digits # use to store digits 1,2,3,4,5
        string.punctuation = string.punctuation # use to store punctuation like ?@[\\]^_`{|}~

        flag = False
        if self.includeNumber.isChecked():
            password.extend(digit)
            flag = True
        if self.includeUppercase.isChecked():
            password.extend(upper_case)
            flag = True
        if self.includeLowercase.isChecked():
            password.extend(lower_case)
            flag = True
        if self.includeSymbols.isChecked():
            password.extend(string.punctuation)
            flag = True

        if flag == False:
            self.errorLabel.setText("Select your type")
            
        random.shuffle(password)

        self.passOutput.setText("".join(password[0:length]))

    def copy(self):
        clipboard.copy(self.passOutput.text())
        self.copyButton.setToolTip("Password is copied")

    def get_length(self):
        value = self.getLength.text()
        value = int(value)
        return value

    def handle_buttons(self):
        self.generatePassword.clicked.connect(self.generate_password)
        self.copyButton.clicked.connect(self.copy)
        

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()