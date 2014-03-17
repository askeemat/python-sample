import serial
import threading
import sys


class SerialThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=None)
        
    def run(self):
        while True:
            str = self.ser.readline()
            print str ,

    def __del__(self):
        self.ser.close()


class AdbInputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            for line in sys.stdin:
                print line ,


ser_th = SerialThread()
adb_th = AdbInputThread()
ser_th.start()
adb_th.start()
