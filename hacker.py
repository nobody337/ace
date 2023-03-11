import time

def Hacker():
    print("Enter the target you want to hack: ")
    target = input()
    print(f"Connecting to {target}...")
    time.sleep(2)
    print(f"Connected to {target}!")
    print("Initiating brute force attack...")
    time.sleep(5)
    print("Brute force attack successful!")
    print("Access granted.")
