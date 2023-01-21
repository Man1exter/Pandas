import pandas as pd
from PySide6.QtWidgets import QApplication, QFileDialog, QTableView
import os

app = QApplication()
file_path, _ = QFileDialog.getOpenFileName()

# Input validation
if not file_path:
    print("No file selected")
    exit()

# File type check
if not file_path.endswith('.csv'):
    print("Invalid file type")
    exit()

# File size check
file_size = os.path.getsize(file_path)
if file_size > 1000000:
    print("File too large")
    exit()

# File path sanitation
file_path = os.path.abspath(file_path)

# Exception handling
try:
    data = pd.read_csv(file_path)
except Exception as e:
    print("An error occurred while reading the file:", e)
    exit()
table = QTableView()
table.setModel(data)
table.show()
app.exec_()





