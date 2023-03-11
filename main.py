from ETH import EthMiner
from bruteforce import BruteForce
from hacker import Hacker

def main():
    print("Welcome to the Termux Tool!")
    print("Choose a tool to use:")
    print("1. ETH wallet miner and checker")
    print("2. Brute force")
    print("3. Hollywood hacking")
    choice = input("Enter your choice: ")
    if choice == "1":
        EthMiner()
    elif choice == "2":
        BruteForce()
    elif choice == "3":
        Hacker()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
