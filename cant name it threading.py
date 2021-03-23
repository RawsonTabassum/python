import threading

class messenger (threading.Thread):
    def run (self):
        for _ in range(200):
            print(threading.currentThread().getName())


x = messenger(name = 'sending')
y = messenger(name = 'receiving')
x.start()
y.start()