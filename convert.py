from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QTextDocument


file = QFile("plik.csv")
file.open(QFile.ReadOnly | QFile.Text)
stream = QTextStream(file)
csv_data = stream.readAll()
file.close()

document = QTextDocument()
document.setHtml(csv_data)
html_data = document.toHtml()

file = QFile("plik.html")
file.open(QFile.WriteOnly | QFile.Text)
stream = QTextStream(file)
stream << html_data
file.close()