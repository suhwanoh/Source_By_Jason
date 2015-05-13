import threading

class JasonsMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


x = JasonsMessenger(name='Sending out messages')
y = JasonsMessenger(name='Receiving several message at the same time')

# start() method just kicks off the method 'run' in classes.

x.start()
y.start()
