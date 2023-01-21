import pandas as pd
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.select_file_button = QPushButton("Select CSV file", self)
        self.select_file_button.clicked.connect(self.select_file)
        self.setCentralWidget(self.select_file_button)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Select CSV file", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            df = pd.read_csv(file_name)
            df.to_excel("converted_files/{}.xlsx".format(file_name.split("/")[-1].split(".")[0]), index=False)

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()
