import fakeduino
import os
import pty
import threading

master_fd, slave_fd = pty.openpty()
slave_tty_name = os.ttyname(slave_fd)

print('Connect to Fakeduino/Bitlash on ' + slave_tty_name)

arduino = fakeduino.Fakeduino()
arduino.attach(fakeduino.ButtonComponent(), 'd12')
arduino.attach(fakeduino.LedComponent(), 'd13')

bitlash = fakeduino.bitlash.Bitlash(master_fd, arduino)
bitlash_thread = threading.Thread(target=bitlash.run, args=())
bitlash_thread.daemon = True
bitlash_thread.start()

arduino.run()
