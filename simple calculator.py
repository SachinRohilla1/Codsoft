import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox,
    QMessageBox, QTextEdit, QWidget, QMenuBar
)
from PyQt6.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 400, 300)
        
        # Set window icon
        self.setWindowIcon(QIcon('icon.png'))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        self.label1 = QLabel('Enter your first number:')
        layout.addWidget(self.label1)
        
        self.input1 = QLineEdit(self)
        layout.addWidget(self.input1)
        
        self.label2 = QLabel('Enter your second number:')
        layout.addWidget(self.label2)
        
        self.input2 = QLineEdit(self)
        layout.addWidget(self.input2)
        
        self.label3 = QLabel('Choose an operation:')
        layout.addWidget(self.label3)
        
        self.combo = QComboBox(self)
        self.combo.addItem("Addition")
        self.combo.addItem("Subtraction")
        self.combo.addItem("Multiplication")
        self.combo.addItem("Division")
        self.combo.addItem("Modulus")
        layout.addWidget(self.combo)
        
        self.button = QPushButton('Calculate', self)
        self.button.clicked.connect(self.calculate)
        layout.addWidget(self.button)
        
        # Result section
        self.result_label = QLabel('Result:')
        layout.addWidget(self.result_label)

        self.result_display = QTextEdit()
        self.result_display.setPlaceholderText('Results will appear here...')
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        central_widget.setLayout(layout)
        
        # Menu bar
        menu_bar = self.menuBar()
        about_menu = menu_bar.addMenu('Help')
        
        # Adding 'About' directly to the menu bar
        about_action = about_menu.addAction('About')
        about_action.triggered.connect(self.show_about)
        
    def calculate(self):
        try:
            a = int(self.input1.text())
            b = int(self.input2.text())
            operation = self.combo.currentText()
            
            if operation == "Addition":
                result = a + b
            elif operation == "Subtraction":
                result = a - b
            elif operation == "Multiplication":
                result = a * b
            elif operation == "Division":
                if b != 0:
                    result = a // b
                else:
                    QMessageBox.warning(self, 'Error', 'Division by zero is not allowed')
                    return
            elif operation == "Modulus":
                if b != 0:
                    result = a % b
                else:
                    QMessageBox.warning(self, 'Error', 'Division by zero is not allowed')
                    return
            else:
                result = 'Invalid choice'
            
            self.result_display.setText(f'Result: {result}')
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Please enter valid numbers')
            self.result_display.setText('')

    def show_about(self):
        QMessageBox.about(self, 'About Calculator', 'This is a simple calculator application built with PyQt6.\n'
                                                     'It supports addition, subtraction, multiplication, division, and modulus operations.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
