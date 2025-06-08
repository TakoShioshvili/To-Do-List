import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from design import Ui_MainWindow

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tasks = []

        self.addpushButton.clicked.connect(self.add_task)
        self.deletepushButton.clicked.connect(self.clear)

    def add_task(self):
        text = self.taskinput.text()
        priority = self.comboBox.currentText()
        task = QCheckBox(f'{text} ({priority} priority)')
        task.stateChanged.connect(self.label_status)
        task.setStyleSheet("color: rgb(255, 85, 127);")
        self.layout.addWidget(task)
        self.tasks.append({'Task': text, 'Completed': False})
        self.taskinput.clear()

    def clear(self):
        layout = self.layout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
        self.tasks_left.setText('0 Tasks completed')

    def label_status(self):
        checked = 0
        total = self.layout.count()
        for i in range(total):
            item = self.layout.itemAt(i)
            if item.widget().isChecked():
                checked += 1

        self.tasks_left.setText(f'{checked} Tasks Completed')





app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())
