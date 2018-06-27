#1.Create a threading process such that it sleeps for 5 seconds and then prints out a message. 

import time
import threading
#from threading import Thread

class Sample(threading.Thread):
    def run(self):
        time.sleep(2)
        print(self.name," Let's know about threading in python")


thread_one = Sample(name = "thread_one").start()
print("\n")
print("*"*25)
print("\n")

#2. Make a thread that prints numbers from 1-10, waits for 1 sec between

import time
import threading

class Print_range(threading.Thread):
    def run(self):
      
        for i in range (1,11):
            time.sleep(1)
            print(i)


thread_two = Print_range(name = "thread_two").start()
print("\n")
print("*"*25)
print("\n")

#3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec .

import time
import threading

list_one = [ 10, 20, 30 , 40, 50]
class Delay(threading.Thread):
    def run(self):
        for i in range(1,6):
            time.sleep(i*2)
            print(list_one[i-1])
thread_three = Delay(name = "thread_three").start()
print("\n")
print("*"*25)
print("\n")'

#4. Call factorial function using thread.

import time
import threading
from threading import Thread

class Cal(threading.Thread):
    def __init__(self,n):
        Thread.__init__(self)
        self.n = 1

    def factorial(self):
        self.res = 1
        for i in range(1,self.n+1):
            self.res = self.res*i
        print(self.res)


    def run(self):
        self.factorial()
       

thread_four = Cal(5).start()
