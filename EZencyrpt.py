import time
import random
primes = [2,3,5,7,11,13,17,23]

alan_detector = random.choice(primes)


def decrypt():
    out = ""
    decrpyt_text=input("enter Text to be decrpyted:")
    key = int(input("Enter the key Used:"))


    for a in decrpyt_text:
        x = ((((ord(a) - 10) // alan_detector) -10000) - key)
        x = chr(x)
        out += x
    print(out)
    time.sleep(5)
    menu()

def encrypt():
    out = ""
    plain = input("Enter Text to be encypted (it's super secure) (no data leaks for 2 days):")
    key = int(input("enter the key you would like to use:"))

    for a in plain:
        x = (((ord(a) + key + 10000) * alan_detector) +10)
        x = chr(x)
        out += x

    print(out)
    time.sleep(5)
    menu()
def menu():
    print("""

MENU
----
[1] Encrypt
[2] Decrypt
[3] Exit

""")
    choice = int(input("Choice:"))
    if choice == 1:
     encrypt()
    if choice == 2:
     decrypt()
    if choice == 3:
     exit()
    else:
     print("It was so simple...")
     exit()
    
menu()