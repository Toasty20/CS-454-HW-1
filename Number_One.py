import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, index, left_chopstick, right_chopstick):
        threading.Thread.__init__(self)
        self.index = index
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
 
    def run(self):
        while True:
            print(f'Philosopher {self.index} is thinking')
            time.sleep(1)
            print(f'Philosopher {self.index} is hungry')
            self.left_chopstick.acquire()
            self.right_chopstick.acquire()
            print(f'Philosopher {self.index} is eating')
            time.sleep(1)
            self.left_chopstick.release()
            self.right_chopstick.release()
            print(f'Philosopher {self.index} is done eating')



chopsticks = []
philosophers = [] 
for i in range(5): 
    chopsticks.append(threading.Lock()) 

for i in range(5): 
    if i == 4:
       philosophers.append(Philosopher(i, chopsticks[i], chopsticks[(0)])) 
    else:
        philosophers.append(Philosopher(i, chopsticks[i], chopsticks[(i+1)])) 

for philosopher in philosophers:
    philosopher.start()
