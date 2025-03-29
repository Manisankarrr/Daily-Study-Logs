#multithreading - Used to perform multiple tasks concurrently (multitasking)
# Good for I/0 bound tasks like reading files or fetching data from APIs
# threading. Thread (target=my _ function)

import threading
import time
def walk_dog(name,namee):
    print(f"Walking {name}...")
    time.sleep(5)
    print(f"{namee} walked!")
    

def trash():
    time.sleep(3)
    print("Taking out the trash...")

def get_mail():
    time.sleep(1)
    print("Getting the mail...")

chore1 = threading.Thread(target=walk_dog, args=("tommy","nigga"))#to pass as tuple add comma so py will recognise it is tuple
chore2 = threading.Thread(target=trash)
chore3 = threading.Thread(target=get_mail)

chore1.start()
chore2.start()
chore3.start()

# wait for all threads to finish execution before moving on
chore1.join()
chore2.join()
chore3.join()

print("All chores complete!")
# everything work concurrently compare with time to check it
