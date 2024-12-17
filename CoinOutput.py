from gpiozero import Motor
from time import sleep
import threading

class CoinOutput():
    motor10 = Motor(forward=17, backward=18)
    motor1 = Motor(forward=19, backward=20)
    
    def __init__(self):
        pass

    def Output10(self, count):
        print(count)
        for i in range(count):
            self.motor10.forward()
            sleep(0.3)
            self.motor10.backward()
            sleep(0.3)
        self.motor10.stop()
        pass

    def Output1(self, count):
        print(count)
        for i in range(count):
            self.motor1.forward()
            sleep(0.3)
            self.motor1.backward()
            sleep(0.3)
        self.motor1.stop()

    def OutputByValue(self, value):
        coin10 = value // 10
        coin1 = value % 10

        thread10 = threading.Thread(target=self.Output10, args=(coin10,))
        thread1 = threading.Thread(target=self.Output1, args=(coin1,))

        thread10.start()
        thread1.start()

        thread10.join()
        thread1.join()






CoinOutput().OutputByValue(30)