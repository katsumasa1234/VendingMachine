from CoinOutput import CoinOutput
import CoinDetect
import cv2
from gpiozero import Button, Buzzer
import time

button = Button(27)
buzzer = Buzzer(22)
coinOutput = CoinOutput()

def buzzer_warning():
    buzzer.on()
    time.sleep(1)
    buzzer.off()

def buzzer_complete():
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.1)
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.3)
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()
    time.sleep(0.1)
    buzzer.on()
    time.sleep(0.1)
    buzzer.off()

def capture_loop(price):
    while True:
        value = CoinDetect.detect_coin()

        cv2.waitKey(10)
        if not button.is_active:
            change = value - price
            if (change >= 0):
                coinOutput.OutputByValue(change)
                buzzer_complete()
                break
            else:
                buzzer_warning()
    cv2.destroyAllWindows()

while True:
    command = input("cmd > ")
    if (command == "exit"):
        break
    else:
        try:
            command = int(command)
            if (command < 0):
                raise ValueError()
            capture_loop(command)
        except ValueError:
            print("入力が不正です。")