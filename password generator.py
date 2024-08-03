import sys
import random
import string
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
                             QLabel, QSpinBox, QMessageBox, QDialog, QDialogButtonBox)

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 250)  # Adjusted height for the new button
        
        # Set up the central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Create and add widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Create and add a label for password length input
        self.length_label = QLabel("Password Length:")
        self.main_layout.addWidget(self.length_label)
        
        # Create and add a spin box for length input
        self.length_input = QSpinBox()
        self.length_input.setMinimum(1)
        self.length_input.setMaximum(100)  # Set a reasonable maximum length
        self.main_layout.addWidget(self.length_input)
        
        # Create and add a button to generate the password
        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.main_layout.addWidget(self.generate_button)
        
        # Create and add a label to display the generated password
        self.password_label = QLabel("Your generated password will appear here.")
        self.main_layout.addWidget(self.password_label)
        
        # Create and add an 'About' button
        self.about_button = QPushButton("About")
        self.about_button.clicked.connect(self.show_about_dialog)
        self.main_layout.addWidget(self.about_button)
    
    def show_about_dialog(self):
        # Create a dialog to show about information
        dialog = QDialog(self)
        dialog.setWindowTitle("About")
        layout = QVBoxLayout()
        
        # Add label with about information
        about_info = QLabel("Password Generator\n\nCreated by Sachin Rohilla")
        layout.addWidget(about_info)
        
        # Add OK button to close the dialog
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(dialog.accept)
        layout.addWidget(button_box)
        
        dialog.setLayout(layout)
        dialog.exec()
    
    def generate_password(self):
        length = self.length_input.value()
        if length < 1:
            QMessageBox.warning(self, "Input Error", "Password length must be at least 1.")
            return
        
        # Generate the password
        password = self._generate_password(length)
        self.password_label.setText(f"Generated Password: {password}")
    
    def _generate_password(self, length):
        # Define the characters that will be used in the password
        characters = string.ascii_letters + string.digits + string.punctuation
        # Randomly select characters from the above set
        return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())
