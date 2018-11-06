from PyQt5.QtCore import QDateTime , Qt

now = QDateTime.currentDateTime()

print("Local datetime : ",now.toString(Qt.ISODate))
print("Universal datetime: ",now.toUTC().toString(Qt.ISODate))

