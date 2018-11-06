from PyQt5.QtCore import QDate, QTime , QDateTime , Qt


now = QDate.currentDate()

print (now.toString(Qt.ISODate)) # Current Date
print (now.toString(Qt.DefaultLocaleLongDate)) # Current Date in spelling

datetime = QDateTime.currentDateTime()
print(datetime.toString()) # Current time , system Time

time = QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))
