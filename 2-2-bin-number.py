import time
import RPi.GPIO as GPIO


dac = [8, 11, 7, 1, 0, 5, 12, 6]
#bit_number = [0, 1, 0, 1, 0, 1, 1, 0]
numbers = [0, 5, 32, 64, 127, 255, 256] 

volt = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def make_bit_number(number):
    number_8 = number % 256
    bin_number_list = [0 for i in range(8)]

    bin_number = bin(number_8)
    i = -1
    while bin_number[i] != 'b':
        bin_number_list[i] = int(bin_number[i])
        i -= 1
        
    print(number, bin(number_8)[2:], sep = ' -> ')
    
    GPIO.output(dac, bin_number_list)
    now = float(input())
    volt.append(now)

for number in numbers:
    make_bit_number(number)

print(volt)

GPIO.output(dac, 0)
GPIO.cleanup()

