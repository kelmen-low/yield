from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Set the Title
        self.setWindowTitle("Yield Wine Bar")
        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        #Create the label
        label = QLabel("Pass")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)

        # Create a widget to hold the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

        # Set the button
        self.button = QPushButton("Submit")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.toggle_button_text)

        layout.addWidget(self.button)

        # Set the input box for wines
        self.wine1 = QLineEdit("Enter the wine name")
        self.wine1.setClearButtonEnabled(True)

        layout.addWidget(self.wine1)

    def toggle_button_text(self):

        # Access the layout from the central widget
        layout = self.centralWidget().layout()

        # Access the button from the layout
        button = layout.itemAt(1).widget()

        # Check if the button is checked
        if button.isChecked():
            button.setText("Pressed")
        else:
            button.setText("Submit")


app = QApplication(sys.argv)

app.setStyleSheet("QPushButton { margin: 10ex; }")

window = MainWindow()
window.show()

app.exec_()
