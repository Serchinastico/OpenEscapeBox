import serial
import os


def main():
    connection = serial.Serial('/dev/ttyACM0', 57600)
    connection.open()
    connection.write("d13=1")
    connection.close()


main()
