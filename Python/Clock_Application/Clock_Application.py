from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5 import QtCore
import datetime

class WinClock(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Python/Clock_Application/clock_win.ui", self)
        #current time
        self._time = QtCore.QTimer(self)
        self._time.timeout.connect(self.Start_Time)
        #stopwatcher
        self._Sw = QtCore.QTimer(self)
        self._Sw.timeout.connect(self.Start_Sw)
        #timer
        self._Timer = QtCore.QTimer(self)
        self._Timer.timeout.connect(self.Start_Timer)
        #main buttons
        self.time_btn.clicked.connect(self.ShowTime)#current time
        self.Sw_btn.clicked.connect(self.ShowSw)#stopwatcher
        self.timer_btn.clicked.connect(self.ShowTimer)#timer
        #secondary stopwatch buttons
        self.Sw_Start_btn.clicked.connect(self.Start_Sw)
        self.Sw_Stop_btn.clicked.connect(self.Stop_Sw)
        #secondary timer buttons
        self.Timer_Start_btn.clicked.connect(self.Start_Timer)
        self.Timer_Stop_btn.clicked.connect(self.Stop_Timer)
        self.Plus_btn.clicked.connect(self.Plus_Timer)
        self.Min_btn.clicked.connect(self.Min_Timer)
        #global app variables
        self.Increment = 0
        self.Decrement = 0
        #------------------------------
        self.time_btn.setEnabled(False)
        self.Sw_number.display("0:00:00")
        self.Sw_Stop_btn.setEnabled(False)
        self.Timer_number.display("0:00:00")
        self.Timer_Stop_btn.setEnabled(False)

        self.ShowTime()

    #function that enables current time
    def ShowTime(self):
        #enabled and disabled
        self.time_btn.setEnabled(False)
        self.Sw_btn.setEnabled(True)
        self.timer_btn.setEnabled(True)
        self._time.start(100)
        #hide and show
        self.Sw_Start_btn.hide()
        self.Sw_Stop_btn.hide()
        self.Sw_number.hide()
        self.Timer_number.hide()
        self.Timer_Start_btn.hide()
        self.Timer_Stop_btn.hide()
        self.Plus_btn.hide()
        self.Min_btn.hide()
        self.Time_number.show()

    #function that enables stopwatch
    def ShowSw(self):
        #enabled and disabled
        self.Sw_btn.setEnabled(False)
        self.time_btn.setEnabled(True)
        self.timer_btn.setEnabled(True)
        self.Sw_Timer = True
        #hide and show
        self.Time_number.hide()
        self.Timer_number.hide()
        self.Timer_Start_btn.hide()
        self.Timer_Stop_btn.hide()
        self.Plus_btn.hide()
        self.Min_btn.hide()
        self.Sw_Start_btn.show()
        self.Sw_Stop_btn.show()
        self.Sw_number.show()

    #function that enables the timer
    def ShowTimer(self):
        #enabled and disabled
        self.timer_btn.setEnabled(False)
        self.time_btn.setEnabled(True)
        self.Sw_btn.setEnabled(True)
        self.Sw_Timer = False
        #hide and show
        self.Time_number.hide()
        self.Sw_number.hide()
        self.Sw_Start_btn.hide()
        self.Sw_Stop_btn.hide()
        self.Timer_Start_btn.show()
        self.Timer_Stop_btn.show()
        self.Timer_number.show()
        self.Plus_btn.show()
        self.Min_btn.show()
    
    #function to calculate current time
    def Start_Time(self):
        currentTime = QtCore.QTime.currentTime()
        timeText = currentTime.toString('hh:mm:ss')
        self.Time_number.display(timeText)

    #function to start stopwatch   
    def Start_Sw(self):
        self._Sw.start(1000)
        self.Sw_Stop_btn.setText("Pause")
        SwText = datetime.timedelta(seconds=self.Increment)
        self.Sw_number.display(str(SwText))
        self.Sw_Start_btn.setEnabled(False)
        self.Sw_Stop_btn.setEnabled(True)
        self.Increment += 1            

    #function to pause or restart the stopwatch
    def Stop_Sw(self):
        if self.Sw_Stop_btn.text() == "Pause":
            self.Sw_Start_btn.setEnabled(True)
            self._Sw.stop()
            self.Sw_Stop_btn.setText("Stop")

        elif self.Sw_Stop_btn.text() == "Stop":
            self.Increment = 0
            self.Sw_Stop_btn.setText("Pause")
            self.Sw_Stop_btn.setEnabled(False)
            self.Sw_number.display("0:00:00")

    #function to start the timer
    def Start_Timer(self):
        if self.Decrement == 0:
            self.Timer_Stop_btn.setText("Stop")
            self._Timer.stop()
            self.Timer_number.display("0:00:00")
        else:
            self.Plus_btn.setEnabled(False)
            self.Min_btn.setEnabled(False)
            self._Timer.start(1000)
            self.Timer_Stop_btn.setText("Pause")
            TimerText = datetime.timedelta(seconds=self.Decrement)
            self.Timer_number.display(str(TimerText))
            self.Timer_Start_btn.setEnabled(False)
            self.Timer_Stop_btn.setEnabled(True)
            self.Decrement -= 1
    
    #funcion para pausar o reiniciar el temporizador
    def Stop_Timer(self):
        if self.Timer_Stop_btn.text() == "Pause":
            self.Timer_Start_btn.setEnabled(True)
            self._Timer.stop()
            self.Timer_Stop_btn.setText("Stop")

        elif self.Timer_Stop_btn.text() == "Stop":
            self.Decrement = 0
            self.Timer_Stop_btn.setText("Pause")
            self.Timer_Stop_btn.setEnabled(False)
            self.Timer_number.display("0:00:00")
            self.Timer_Start_btn.setEnabled(True)
            self.Plus_btn.setEnabled(True)
            self.Min_btn.setEnabled(True)
    
    #function to add minutes to the timer
    def Plus_Timer(self):
        self.Decrement += 300
        TimerText = datetime.timedelta(seconds=self.Decrement)
        self.Timer_number.display(str(TimerText))

    #function to subtract minutes to the timer
    def Min_Timer(self):
        if self.Decrement != 0:
            self.Decrement -=300
            TimerText = datetime.timedelta(seconds=self.Decrement)
            self.Timer_number.display(str(TimerText))


        
app = QApplication([])

win = WinClock()
win.show()

app.exec_()