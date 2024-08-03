import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox, QWidget, QLabel, QDialog, QDialogButtonBox

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")
        layout = QVBoxLayout()

        label = QLabel("To-Do List Application\nCreated by Sachin Rohilla")
        layout.addWidget(label)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

        self.setLayout(layout)
        self.setFixedSize(200, 100)

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tasks = load_tasks()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('To-Do List Application')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        self.add_button = QPushButton('Add Task')
        self.add_button.clicked.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.update_button = QPushButton('Update Task')
        self.update_button.clicked.connect(self.update_task)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton('Delete Task')
        self.delete_button.clicked.connect(self.delete_task)
        layout.addWidget(self.delete_button)

        self.about_button = QPushButton('About')
        self.about_button.clicked.connect(self.show_about)
        layout.addWidget(self.about_button)

        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_list.clear()
        for task in self.tasks:
            status = "Done" if task['completed'] else "Not Done"
            self.task_list.addItem(f"{task['task']} [{status}]")

    def add_task(self):
        task, ok = QInputDialog.getText(self, 'Add Task', 'Enter task description:')
        if ok and task:
            self.tasks.append({'task': task, 'completed': False})
            save_tasks(self.tasks)
            self.refresh_tasks()

    def update_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'Update Task', 'Select a task to update.')
            return

        item = selected_items[0]
        index = self.task_list.row(item)
        self.tasks[index]['completed'] = not self.tasks[index]['completed']
        save_tasks(self.tasks)
        self.refresh_tasks()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, 'Delete Task', 'Select a task to delete.')
            return

        item = selected_items[0]
        index = self.task_list.row(item)
        self.tasks.pop(index)
        save_tasks(self.tasks)
        self.refresh_tasks()

    def show_about(self):
        dialog = AboutDialog(self)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
